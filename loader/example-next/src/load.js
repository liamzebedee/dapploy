async function run() {
    const bundleId = 'Qmaw976qWUcc8XAhsEkE9YEB9q3tfvMZFbE33D8AQqGMED'
    const ipfsNode = `http://127.0.0.1:8080/ipfs/`

    const url = `${ipfsNode}${bundleId}`
    const data = await fetch(url)
    const htmlTxt = await data.text()

    const parser = new DOMParser();
    const htmlDoc = parser.parseFromString(htmlTxt, 'text/html');
    // const htmlDoc = document.createElement("html")
    // document.body.insertAdjacentHTML('beforebegin', htmlTxt)
    console.log(htmlDoc)

    // window.htmlDoc = htmlDoc
    // document.head.append(...htmlDoc.head.children)
    // document.body.append(...htmlDoc.body.children)

    // document.head.insertAdjacentElement('afterbegin', htmlDoc.head)
    // document.body.insertAdjacentElement('afterbegin', htmlDoc.body)
    function copyElementAttributes(destinationElement, sourceElement) {
        for (const { name, value } of array(sourceElement.attributes)) {
            destinationElement.setAttribute(name, value)
        }
    }
    function replaceElementWithElement(fromElement, toElement) {
        const parentElement = fromElement.parentElement
        if (parentElement) {
            return parentElement.replaceChild(toElement, fromElement)
        }
    }

    // replaceElementWithElement(document.head, htmlDoc.head)

    // replaceElementWithElement(document.body, htmlDoc.body)
    // document.documentElement.replaceWith(htmlDoc)


    // For some reason * doesn't trigger reflow.

    // document.head.innerHTML += '<style>*{display:1}</style>'
    // document.head.innerHTML += '<style>*{display:block}</style>' 
    const head = htmlDoc.getElementsByTagName('head')[0]
    const body = htmlDoc.getElementsByTagName('body')[0]
    console.log(head.childNodes)
    // htmlDoc.head.childNodes


    // document.body.append(
    //     ...htmlDoc.body.children
    // )
    // document.body.innerHTML = htmlDoc.body.innerHTML
    
    // for (let el of body.childNodes) {
    //     if(el.tagName == 'SCRIPT') {
    //         const el2 = document.createElement('script')
    //         el2.src = el.src
    //         document.head.append(el2)
    //     }
    // }

    // for (let el of head.childNodes) {
    //     if (el.tagName == 'LINK') {
    //         const el2 = document.createElement('link')
    //         el2.href = el.href
    //         el2.rel = el.rel
    //         document.head.append(el2)
    //     }
    // }

    // // document.head.prepend(
    // //     ...htmlDoc.head.children
    // // )






    // document.documentElement.innerHTML = htmlTxt

    // const shadowRoot = document.body.attachShadow({ mode: 'open' })
    // shadowRoot.innerHTML = htmlTxt

    // document.body.app

    // window.requestAnimationFrame(() => {
    //     console.log('window.requestAnimationFrame()')

    //     var link = document.createElement("link");
    //     link.href = '/_next/static/css/687795e492ea17b9905c.css'
    //     link.type = "text/css";
    //     link.rel = "stylesheet";

    //     document.getElementsByTagName("body")[0].appendChild(link);
    // })

    // document.body.insertAdjacentElement('afterbegin', htmlDoc.body)

    const iframe = document.createElement('iframe')
    iframe.src = url
//     console.log(htmlDoc.outerHTML)

//     iframe.src = 'data:text/html,' + encodeURIComponent(htmlTxt) + encodeURIComponent(`<script id='serviceworker'>
//     navigator.serviceWorker.register('./sw.js', { scope: '/' })
//             .then((reg) => {
//                 // registration worked
//                 console.log('Registration succeeded. Scope is ' + reg.scope);
//             }).catch((error) => {
//                 // registration failed
//                 console.log('Registration failed with ' + error);
//             });
//     </script>
// `)
    iframe.height = window.innerHeight
    iframe.width = window.innerWidth
    document.body.append(iframe)
}

// document.addEventListener('load', () => run())
window.onload = run