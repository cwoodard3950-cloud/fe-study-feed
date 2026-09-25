// FE Study Feed — service worker
// Caches the app shell + card data so the feed keeps working (mostly) offline.
// Fonts/MathJax load from CDNs and are best-effort only: cached opportunistically,
// but not guaranteed offline since they're cross-origin.

const CACHE_NAME = "fe-study-feed-v2";
const CORE_ASSETS = [
  "./",
  "./index.html",
  "./manifest.json",
  "./cards.json",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./icons/apple-touch-icon.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(CORE_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

function putInCache(request, response) {
  if (response && response.status === 200 && request.url.startsWith(self.location.origin)) {
    const clone = response.clone();
    caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
  }
}

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;

  // Page navigations and index.html: network-first, so updates (like this one)
  // reach the installed app right away instead of hiding behind a stale cache.
  const isPageRequest = event.request.mode === "navigate" || event.request.url.endsWith("/index.html");
  if (isPageRequest) {
    event.respondWith(
      fetch(event.request)
        .then((response) => { putInCache(event.request, response); return response; })
        .catch(() => caches.match(event.request).then((cached) => cached || caches.match("./index.html")))
    );
    return;
  }

  // Everything else (icons, cards.json, fonts/MathJax): cache-first, revalidate in background.
  event.respondWith(
    caches.match(event.request).then((cached) => {
      const networkFetch = fetch(event.request)
        .then((response) => { putInCache(event.request, response); return response; })
        .catch(() => cached);
      return cached || networkFetch;
    })
  );
});
