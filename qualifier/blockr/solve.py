# Check source code of contract using explorer 
from web3 import Web3

# Helper function to pad bytes with leading zeros
def pad_bytes(value: bytes, length: int) -> bytes:
    if len(value) >= length:
        return value
    padding = b'\x00' * (length - len(value))
    return padding + value

# Connect to the Rinkeby network using Alchemy as the provider
w3 = Web3(Web3.HTTPProvider("https://eth-sepolia.g.alchemy.comn"))  # Replace <your_alchemy_api_key> with your Alchemy API key

# Set the contract address and ABI
contract_address = Web3.to_checksum_address('0xe4C9Dcc9ea468C9BaB4C7B2fe4bc3b9b97796055')
contract_abi = [
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "GHI",
                "type": "bytes32"
            }
        ],
        "name": "DEF",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Create the contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Get the last 5 block number on Rinkeby
latest_block_number = w3.eth.block_number
block_hash = w3.eth.get_block(latest_block_number - 5).hash

# Call the contract function
result = contract.functions.DEF(block_hash).call()

# Print the result
print(result)

