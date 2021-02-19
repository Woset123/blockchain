import time
import json
import copy
from block import Block
from transaction import Transaction


class Blockchain:
  
# =============================================================================
#     
# =============================================================================
    def __init__(self, difficulty, blockList=[], blockReward=50):
       
        self.blockList = []
        for elt in blockList:
            block = Block(elt["index"],elt["previousHash"],elt["signature"], elt["nonce"], elt["timestamp"], elt["transactions"], elt["hashVal"], elt["minerName"])
            self.blockList.append(block)
        self.transactionPool = []
        self.difficulty = difficulty
        self.blockReward = blockReward

# =============================================================================
#     
# =============================================================================
    def createGenesisBlock(self, wallet):
        
        blk = Block(0,"")
        transaction = Transaction(self.blockReward, wallet.to_address(), "network", time.time())
        blk.addTransaction(transaction, wallet)
        nonce = blk.miningFunction(self.difficulty, wallet)
        self.blockList.append(blk)

        
# =============================================================================
# 
# =============================================================================
    def mineNewBlock(self, wallet):
        
        lastBlock = self.blockList[-1]
        index = lastBlock.index + 1
        previousHash = lastBlock.hashVal
        blk = Block(index, previousHash)
        # Fill with transactions
        for t in self.transactionPool:
            blk.addTransaction(t, wallet)
        # Clear waiting Transactions
        self.transactionPool.clear()
        
        transaction = Transaction(self.blockReward, wallet.to_address(), "network", time.time())
        blk.addTransaction(transaction, wallet)
        nonce = blk.miningFunction(self.difficulty, wallet)
        self.blockList.append(blk)
        
    
# =============================================================================
# 
# =============================================================================
    def addBlockFromPeer(self, block):
        
        lastBlock = self.blockList[-1]
        
        # Check conditions
        if (block.timestamp < lastBlock.timestamp):
            print("Timestamp received : " + str(block.timestamp))
            print("Timestamp last block : " + str(lastBlock.timestamp))
            raise ValueError("Error timestamp is before timestamp of last block !")
        if(block.index != lastBlock.index+1):
            print("Index received : " + str(block.index))
            print("Index expected : " + str(lastBlock.index + 1))
            raise ValueError("Error in indexing")
        if(block.previousHash!=lastBlock.hashVal):
            print("Previous Hash received : " + str(block.previousHash))
            print("Previous Hash expected : " + str(lastBlock.hashVal))
            raise ValueError("Block not aligned in the chain !")
        if(block.hashVerification(block.nonce)==False):
            raise ValueError("Block not valid !")
        
        # Add block
        self.blockList.append(block)
        
# =============================================================================
# 
# =============================================================================
    def addTransaction(self, receiver, wallet, amount):
        
        transaction = Transaction(amount, wallet.to_address(), receiver, time.time())
        self.transactionPool.append(transaction)
        

# =============================================================================
# 
# =============================================================================
    def verifyChain(self, wallet):
        

        # Check Genesis Block
        if self.blockList[0].index!=0 or self.blockList[0].previousHash!="":
            return False
        
        #  Check Hash
        for blk in self.blockList:
            if blk.hashVerification(blk.nonce)==False:
                return False
     
        # Check Signature 
        for blk in self.blockList:
            if blk.verifyBlockSignature()==False:
                return False
            
        return True 
                
# =============================================================================
# 
# =============================================================================
    def __repr__(self):
        
        string = "Block List : " + str(self.blockList) + "\n" + \
            "Transaction Pool: " + str(self.transactionPool) + "\n" + \
            "Difficulty: " + str(self.difficulty) + "\n" + \
            "Block Reward: " + str(self.blockReward) + "\n"
        return string
    
# =============================================================================
#     
# =============================================================================
    def to_dict(self):
        
        chain_dict=[]
        for elem in self.blockList:
            chain_dict.append(elem.to_dict())
        return chain_dict
