import { useState, useEffect } from 'react'


export default function Index() {
    useEffect(() => {
        if ("serviceWorker" in navigator) {
            window.addEventListener("load", function () {
                navigator.serviceWorker.register("/sw.js").then(
                    function (registration) {
                        console.log("Service Worker registration successful with scope: ", registration.scope);
                    },
                    function (err) {
                        console.log("Service Worker registration failed: ", err);
                    }
                );
            });
        }
    }, [])

    const [src,setSrc] = useState(null)

    async function load() {
        const bundleId = 'Qmaw976qWUcc8XAhsEkE9YEB9q3tfvMZFbE33D8AQqGMED'
        const ipfsNode = `http://127.0.0.1:8080/ipfs/`

        const url = `${ipfsNode}${bundleId}`
        const data = await fetch(url)
        const htmlText = await data.text()

        // const parser = new DOMParser();
        // const htmlDoc = parser.parseFromString(htmlText, 'text/html');

        setSrc(htmlText)
    }

    useEffect(() => {
        load()
    }, [])

    // get html
    // parse it
    // inject the ipfs loader above
    // then conver ti back to a string
    // and set as the iframe src

    return <>
        {src && <iframe width={document.body.clientWidth} height={800} srcDoc={src}/>}
    </>
}