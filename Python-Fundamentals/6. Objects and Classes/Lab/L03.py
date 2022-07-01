class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
emails = []
while command != "Stop":
    info = command.split()
    sender = info[0]
    receiver = info[1]
    content = info[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

sent_emails_num = list(map(int, input().split(", ")))

for index in sent_emails_num:
    emails[index].send()

for current_mail in emails:
    print(current_mail.get_info())