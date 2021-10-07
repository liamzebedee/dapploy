pragma solidity ^0.5.16;

contract Dapploy {
    constructor() public {}

    function deploy(bytes32 ensNamehash, bytes32 ipfsCID) public {
        emit Deployment(ensNamehash, ipfsCID);
    }

    function setServer(string _server) public {
        server = _server;
    }

    function get(string ensName) public returns (bytes32 ipfsCID, bytes32 node1, bytes32 node2, bytes32 node3, bytes32 node4) {
        // namehash
        
    }

    event Deployment(bytes32 indexed ensNamehash, bytes32 indexed ipfsCID);
}