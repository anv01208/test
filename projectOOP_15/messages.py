class Message:

    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text

    def __str__(self):
        return f"{self.sender.username} -> {self.recipient.username}: {self.text}"


