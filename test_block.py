import time
from transaction import Transaction
from block import Block
from key import BitcoinAccount

wallet = BitcoinAccount()

difficulty = 4

first_block = Block(0, "")

tx = Transaction("mohamed", "justine", 50, time.time())

first_block.addTransaction(tx)
first_block.miningFunction(difficulty)

print("First block is: ")

print(first_block)

last_hash = first_block.hashVal

second_block = Block(1, last_hash)

second_block.miningFunction(difficulty)

print("Second block is: ")

print(second_block)
