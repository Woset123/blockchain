from chain import Blockchain
from key import BitcoinAccount

wallet = BitcoinAccount()
address = wallet.to_address()
difficulty = 4

blockchain = Blockchain(difficulty)
blockchain.createGenesisBlock()

print("blockchain: ")
# print(blockchain)
print(blockchain.to_dict())

first_block = blockchain.blockList[-1]

print("First block: ")
print(first_block)

blockchain.addTransaction(address, "colas", 10)
blockchain.addTransaction(address, "salim", 30)
blockchain.mineNewBlock()

print("blockchain: ")
# print(blockchain)
print(blockchain.to_dict())
second_block = blockchain.blockList[-1]

print("Second block: ")
print(second_block)
