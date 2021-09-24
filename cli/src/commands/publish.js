'use strict';

const { resolve, join, relative, isDirectory } = require('path');
const fs = require('fs');
const { gray, green, yellow, red } = require('chalk');
const IPFS = require("ipfs");
const glob = require('glob')
const fsPromises = require("fs/promises")



const DEFAULTS = {
    buildPath: ""
};

const publish = async ({
    buildPath = DEFAULTS.buildPath
} = {}) => {

    const {
        PRIVATE_KEY,
        ETH_RPC_URL,
        NETWORK,
        IPFS_NODE_URL
    } = process.env;

    // const ipfs = await IPFS.create({
    //     config: {
    //         Addresses: null,
    //         Discovery: null,
    //         Bootstrap: ['/ip4/tcp/127.0.0.1/5001'],
    //         Swarm: { ConnMgr: { LowWater: 200, HighWater: 500 } },
    //         Identity: {
    //             PeerID: 'QmYprvCu9nGeDcWkfJo8jmzuBA1cZfAC3GoT6VpetKAMmv',
    //             PrivKey: 'CAASpwkwggSjAgEAAoIBAQDK+rWtaupdr6MDD2IbMpANCA+A/mnF1nu3LnogP951gwX5kzK5XE6VXZwYuVp1DVwCfB2xz0yNiNS9EYoVyEMcgkNLDslX4eIvDPqJdMOhev+QQkvGbe1zKq+tX2H8WHDhNSOS2VuW1YdPTtyAgwpqs14+KxnPqlRdwFZYo3W1a3ysOCJETWH9gK7QFgUUpdEyFQy96Wc9emum+h121Sj3KZDuQeIpmi07Y4O2DzN2aKlcvRXunBt9Bj+W8JaOcw2vMRh3zasFuORgOkINl4mWL+LJLL36d0jFFKtWiyoqpqNXhXLTS/Xnmvx//ZIiWVuMgL7i8AV+5KPDqcFYB5lFAgMBAAECggEATAeEraRyjQ0Q3kCQ2uchlgAC7qpdLEGerYq3LAVAanvdbRJ52Xx94uzhX1FuVJHgeP3MkaG4Zvtt1DQRqP8OREt2sVKkkEqH0l/mKD6YWJAd0gdDItxiKNVAYIxtw3vNLE4fOQ45hFIPEOHVLj3nVPhCwL6cOHDwkP1OWn0/xegF4LnNM/yXuUzoG2Ii4gsZPqN133dNMU/j9X5TfRg0gogtjX4DDlHztGAi5uOscv+RgzAk3j6Owtx9LKo016b3McxLRjcf/oM71Wj8qixxD9aPzqUy48yVHNITXCdKEKwSNxFiLqVwIw1cRtpEPdnDb7YlQH4/WUKVARG07ar3AQKBgQD08e+ABmOTZQuzuCXzdkWKaFv8sQMASwLZCg+zsK2kmvdpoo9JtykJ5KfHxXf45NjIYJlptuZqznSz2U7hMkx65Uuq0cTIImLuuoW7GgYI2qnwNsB5HmCYbH9caSGqEX6BLD38gkFO6Kf5qIOvnuZEpBRRXz48+ig/LtXly4YeVQKBgQDUI+hLqo9fqGKcpkjwKXjlM0tOrLHgiaDF6C+bVieqysXnf015fdxykk2IZCdmYeHs4u08MKqAEfCHWUYWnjpbonCeDXX80TK6crjNVQBNwT3z2j6IwpCm0hA895AQGJea+3qXOo/GZs1O98cwz06I0GEyVhB55HMpLxmf53GfMQKBgBOGVXj3CWjuXQhuXVgSzWhC+VIjKgIT+J4kVywToUPFtoMNGi7eEr9fIqCh9PY6B62xRYlPsv5AhrzvTYJV6BLDxExRfEYXt5sf8xj+8gwyoekr9BuzeC+uNli/aJeN3W+efzJpj5sioIEeFaEiIWjHS3dRCD0EE8E1kodGueIhAoGADSRcU7OxRh/MXCABDL/E+Y3/8FPKgTqFdz03Fcx0kKQXNowwZIJjkcV2gCiUOEeAE4jLYZsyNNTnrbreGLCctOiPSXtT/+GF3v8Ua8QETMzX5a9ziE1lYLBKyTwc9KJRYgyKP6wlFAlyVp4K/P8awmcGXnPueV6ps7dzQvC3nUECgYEAsNmN+JYD+jRI+UgsSKdJzlAUb94Vuex/u2wdIZi6BFuDng9SVPH6JIMCae2UsR81gs8NUX8MmMMv2BCMNmbDtz2xub1ivBXXnHzsr6PjVblwk1566GD7S3vJKiLvVJQDQN3jr/TK+RpZRmUk/kK4l3eSRBS0hl62s8alL6ZONwo='
    //         },
    //         // datastore: { Spec: { type: 'mount', mounts: [] } },
    //         Keychain: {
    //             dek: {
    //                 keyLength: 64,
    //                 iterationCount: 10000,
    //                 salt: 'AVDWQ/MAqe4Ocz7qJC3KrMuM',
    //                 hash: 'sha2-512'
    //             }
    //         }
    //     }
    // });

    const { create, urlSource } = require('ipfs-http-client')
    const ipfs = create("http://127.0.0.1:5001")

    const version = await ipfs.version();
    console.log("IPFS Version:", version.version);
    // console.log(await ipfs.config.getAll())

    console.log(yellow(`Uploading build from path `) + `${buildPath}`)


    // fs.readdirSync(resolve(buildPath)).forEach(file => {
        
    // });

    
    const paths = glob.sync(join(buildPath, "/**/*"), {})
    console.log(paths)
    
    const files = await Promise.all(paths.map(async path => {
        const basePath = '/' + relative(buildPath, path);
        console.log(basePath)
        // return

        if (fs.statSync(path).isDirectory()) {
            await ipfs.files.mkdir(path, { parents: true })
            return
        }
        
        await ipfs.files.write(basePath, await fsPromises.readFile(path), { create: true, parents: true })
        
        const stats = await ipfs.files.stat(basePath)
        console.log(stats)

        console.log(
            `${basePath} http://127.0.0.1:8080/ipfs/${stats.cid.toString()}`
        )
    }))

    const stats = await ipfs.files.stat('/')
    console.log(
        `/ http://127.0.0.1:8080/ipfs/${stats.cid.toString()}`
    )

    // const files = [{
    //     path: '/tmp/myfile.txt',
    //     content: 'ABC'
    // }]
    // console.log(files)

    // const { globSource } = IPFS

    // //options specific to globSource
    // const globSourceOptions = {
    //     recursive: true
    // };

    // //example options to pass to IPFS
    // const addOptions = {
    //     pin: true,
    //     wrapWithDirectory: true,
    //     timeout: 10000
    // };

    // for await (const file of ipfs.addAll(globSource(resolve(buildPath), globSourceOptions), addOptions)) {
    //     console.log(file)
    // }

    

    // for await (const file of ipfs.addAll(streamFiles(), {
    //     wrapWithDirectory: true,
    //     // this is just to show the interleaving of uploads and progress events
    //     // otherwise we'd have to upload 50 files before we see any response from
    //     // the server. do not specify this so low in production as you'll have
    //     // greatly degraded import performance
    //     fileImportConcurrency: 1,
    //     progress: (bytes, file) => {
    //         showStatus(`File progress ${file} ${bytes}`, COLORS.active)
    //     }
    // })) {
    //     console.log(`Added file: ${file.path} ${file.cid}`)
    // }

    // IPFS hash the directory.
    // Upload it to hosting service.
    // Now pay for pinning in some way.

    
    // ipfs hash directory
    // call Dapploy.deploy(bundleId)
    // Dapployments.deploy(bundleId)

};

module.exports = {
    publish,
    DEFAULTS,
    cmd: program =>
        program
            .command('publish')
            .description('Publish build to the Dapploy network')
            .option('-b, --build-path <value>', 'Build path for built files', DEFAULTS.buildPath)
            .action(publish)
};