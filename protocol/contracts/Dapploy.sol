pragma solidity ^0.5.16;

contract Dapploy {
    string public server = "localhost:99420";

    constructor() public {}

    function deploy(bytes32 ensNamehash, bytes32 ipfsCID) public {
        emit Deployment(ensNamehash, ipfsCID);
    }

    function setServer(string _server) public {
        server = _server;
    }

    event Deployment(bytes32 indexed ensNamehash, bytes32 indexed ipfsCID);
}