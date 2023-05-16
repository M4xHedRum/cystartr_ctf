pragma solidity ^0.8.0;

contract ABC {
    function DEF(string GHI) external view returns (string memory) {
        bytes32 JKL = blockhash(block.number - 5);
        require(GHI == JKL, ":D");
        return "DoHCTF{interact_w_contract}";
    }
}
