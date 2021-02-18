from key import verify_signature

class Transaction:
    
    def __init__(self, amount, sender, receiver, timestamp=0,  number=None):
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.timestamp = timestamp
        self.number = number
        
        
    def __repr__(self):
        string = "Transaction number : " + str(self.number) + "\n" + \
            "Sender: " + str(self.sender) + "\n" + \
            "Receiver: " + str(self.receiver) + "\n" + \
            "Amount: " + str(self.amount) + "\n" + \
            "Timestamp: " + str(self.timestamp) + "\n"
        return string
    
    
    def to_dict(self):
        tx_dict = {}
        tx_dict["number"] = self.number
        tx_dict["sender"] = self.sender
        tx_dict["receiver"] = self.receiver
        tx_dict["amount"] = self.amount
        tx_dict["timestamp"] = self.timestamp
        return tx_dict

