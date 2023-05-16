async function main() {
    const CBA = await ethers.getContractFactory("ABC");
    const FED = await CBA.deploy();
    console.log("Contract Deployed to Address:", FED.address);
  }
  main()
    .then(() => process.exit(0))
    .catch(error => {
      console.error(error);
      process.exit(1);
    });
  