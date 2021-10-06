const ethers = require('ethers')

export default function(ensName) {
    console.log(`loading ${ensName}`)
    // connect to ethers
    const provider = new ethers.JsonRpcProvider('https://mainnet.infura.io/v3/fab0acebc2c44109b2e486353c230998')
    const contract = new ethers.Contract('0x1234', provider)
    const [cid,node1,node2,node3,node4] = await contract.get('kwenta.eth')

    // verifiable loading
    // resources referenced using relative URI's are loaded too

    // so
    // /_next/images/logo.png
    // is loaded and verified.

    /**
     * get kwenta.eth.link
     * starts dapploy.loader
     * dapploy loader finds the best load balancer
     * requests bundle via IPFS
     * requests subresources via ipfs
     *  we can parse the HTML tree to find resources that are to be loaded
     *  but what about JS?
     *  insecure content.
     * what if we bundle the file as a tar.gz
     * and then load the entire file 
     * 
     * we could load things using the serviceworker api
     * https://gist.github.com/dsheiko/8a5878678371f950d37f3ee074fe8031
     * ie. fetch all resources through the ipfs nodes
     * https://github.com/ipfs/js-ipfs/issues/127
     *
     * https://github.com/ipfs/in-web-browsers/issues/128
     * https://github.com/ipfs/ipfs-companion/issues/17
     * 
     */

    /*

    dapp -> IPFS bundle

    loader for dapp

    kwenta.eth -> LOADER_IPFS_HASH

    LOADER_IPFS_HASH = hash(runcode)

    runcode = loader.load(kwenta.eth)

    runcode =
        index.html
        sw.js

            sw.js will load the initial page
            and then intercept everything else

    how do I deploy kwenta.eth?
        build bundle/
        upload bundle/ to ipfs
        build skeleton
            index.html
                loads service worker
            loader.js
                fetches ipfs node to use
                sends it to service worker
                loads initial page
            sw.js
                intercepts any request
                verifies ipfs hash
                loads using ipfs and returns
            


}