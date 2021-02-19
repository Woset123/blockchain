from key import verify_signature

class Transaction:
    
# =============================================================================
#     
# =============================================================================
    def __init__(self, amount, sender, receiver, timestamp=0, sign=0, number=None):
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.timestamp = timestamp
        self.number = number
        self.sign = sign
# =============================================================================
#         
# =============================================================================
    def __repr__(self):
        string = "Transaction number : " + str(self.number) + "\n" + \
            "Sender: " + str(self.sender) + "\n" + \
            "Receiver: " + str(self.receiver) + "\n" + \
            "Amount: " + str(self.amount) + "\n" + \
            "Timestamp: " + str(self.timestamp) + "\n" + \
            "Signature: " + str(self.sign) + "\n"
        return string
# =============================================================================
#     
# =============================================================================
    def to_dict(self):
        tx_dict = {}
        tx_dict["number"] = self.number
        tx_dict["sender"] = self.sender
        tx_dict["receiver"] = self.receiver
        tx_dict["amount"] = self.amount
        tx_dict["timestamp"] = self.timestamp
        tx_dict["sign"] = self.sign
        return tx_dict
# =============================================================================
#        
# =============================================================================
    def signTransaction(self, wallet):
        msg = str(self.sender) + str(self.receiver) + str(self.amount)
        signature = wallet.sign(msg)
        self.sign = signature.hex()
        return signature
# =============================================================================
#     
# =============================================================================
    def verify(self):
        msg = str(self.sender) + str(self.receiver) + str(self.amount)
        sign = self.sign
        publicKey = self.sender
        return verify_signature(sign, msg, publicKey)
     