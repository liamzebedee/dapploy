const hre = require("hardhat");

async function main() {
  const Dapploy = await hre.ethers.getContractFactory("Dapploy");
  const dapploy = await Dapploy.deploy();
  console.log(await dapploy.deployed())
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
