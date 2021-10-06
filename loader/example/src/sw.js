// require('dapploy').get('kwenta.eth');

/**
 * Proxy request using cache-first strategy
 *
 * @param {Cache} caches
 * @param {Request} request
 * @returns {Promise}
 */
function proxyRequest(caches, request) {
    return fetch(request.clone())
        .then(function (networkResponse) {
            if (networkResponse.type !== "opaque" && networkResponse.ok === false) {
                throw new Error("Resource not available");
            }
            console.info("Fetch it through Network", request.url, networkResponse.type);
            return networkResponse;
        }).catch(function () {
            console.error("Failed to fetch", request.url);
            // Placeholder image for the fallback
            return fetch("./placeholder.jpg", { mode: "no-cors" });
        });
}


self.addEventListener("install", function (event) {
    event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate", function (event) {
});

self.addEventListener("fetch", function (event) {
    var request = event.request;
    console.log("Detected request", request.url);

    if (request.method !== "GET") {
        return;
    }

    let urlObj = new URL(request.url)
    if (urlObj.host == self.location.host) {
        // then we intercept the request and serve it from IPFS.
        
    }

    console.log("Accepted request", request.url);

    event.respondWith(
        proxyRequest(caches, request)
    );

});