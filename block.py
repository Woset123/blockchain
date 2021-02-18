import hashlib
import time
from transaction import Transaction
from key import verify_signature


class Block:

# =============================================================================
#         
# =============================================================================
    def __init__(self, index, previousHash, nonce=0, timestamp=0, transactions=[], hashVal=None, minerName=None):
        self.index = index
        self.previousHash = previousHash
        self.hashVal = hashVal
        self.timestamp = timestamp
        self.nonce = nonce
        self.transactions = []
        for elem in transactions:
            self.transactions.append(Transaction(elem["amount"], elem['sender'], elem['receiver'], elem['timestamp'], elem["number"]))
        self.minerName = minerName
        
# =============================================================================
# 
# =============================================================================
    def hashFunction(self, nonce):
        sha = hashlib.sha256()
        data=""
        data = str(self.index) + str(self.timestamp) + str(nonce) + str(self.previousHash)
        for elt in self.transactions:
            data += str(elt.amount) +str(elt.sender) + str(elt.receiver)
        sha.update(data.encode())
        return sha.hexdigest()
    
# =============================================================================
#     
# =============================================================================
    def addTransaction(self, newTransaction):
        t = newTransaction
        t.number = len(self.transactions)
        self.transactions.append(t)
      
# =============================================================================
#         
# =============================================================================
    def __repr__(self):
        string = "Block number : " + str(self.index) + "\n" + \
            "Nonce: " + str(self.nonce) + "\n" + \
            "Timestamp: " + str(self.timestamp) + "\n" + \
            "Miner: " + str(self.minerName) + "\n" + \
            "Transactions: " + str(self.transactions) + "\n" + \
            "Previous Hash: " + str(self.previousHash) + "\n" + \
            "Hash: " + str(self.hashVal) + "\n"
        return string
# =============================================================================
# 
# =============================================================================
    def miningFunction(self, difficulty):
        self.timestamp = time.time()
        nonce = 0
        prefix = "0" * difficulty
        hashRes = self.hashFunction(nonce)
    
        while(hashRes.startswith(prefix)==False):
            nonce+=1
            hashRes = self.hashFunction(nonce)
        
        self.hashVal = hashRes
        self.nonce = nonce
        self.minerName = "Eric"
        
        return nonce
    
# =============================================================================
#                 
# =============================================================================
    def hashVerification(self, nonce):
        computedHash = self.hashFunction(nonce)
        if computedHash != self.hashVal:
            return False
        return True
        
# =============================================================================
#     
# =============================================================================
    def to_dict(self):
        block_dict = {}
        block_dict["index"] = self.index
        block_dict["nonce"] = self.nonce
        block_dict["timestamp"] = self.timestamp
        block_dict["minerName"] = self.minerName
        block_dict["transactions"] = []
        for elt in self.transactions:
            block_dict["transactions"].append(elt.to_dict())
        block_dict["previousHash"] = self.previousHash
        block_dict["hashVal"] = self.hashVal
        return block_dict

    