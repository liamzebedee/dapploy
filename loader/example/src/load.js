async function run() {
    const bundleId = 'QmcnU8Vgm4FF3UXnjZMcFH8fzxAVzKVdcZdcr8YPdhJ8xK'
    const ipfsNode = `http://127.0.0.1:8080/ipfs/`

    const iframe = document.createElement('iframe')
    iframe.src = `http://${window.location.host}/.dapploy/by-ipfs/${bundleId}`
    iframe.height = '100%'
    iframe.width = '100%'
    iframe.style = `
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    width: 100%;
    height: 100%;
    `
    document.body.append(iframe)
}

window.onload = run