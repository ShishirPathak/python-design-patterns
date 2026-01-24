"""Pattern: Bridge
Category: Structural
Problem it solves: Separates abstraction from implementation so they can vary independently.
When to use: You want to mix and match abstractions and implementations.
When not to use: There is only one implementation and no need for flexibility.
"""

from abc import ABC, abstractmethod

#implementor
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str, to: str) -> str:
        pass

# concrete implementors
class EmailSender(NotificationSender):
    def send(self, message: str, to: str) -> str:
        return f"Email to {to}: {message}"

class SMSSender(NotificationSender):
    def send(self, message: str, to: str) -> str:
        return f"SMS to {to}: {message}"

class PUSHSender(NotificationSender):
    def send(self, message: str, to: str) -> str:
        return f"Push to {to}: {message}"


# Abstraction

class Notification(ABC):
    def __init__(self, sender: NotificationSender):
        self.sender = sender
    
    @abstractmethod
    def notify(self, to: str) -> str:
        pass    

class AlertNotification(Notification):
    def notify(self, to: str) -> str:
        return self.sender.send("Security alert detected ", to)

class OTPNotification(Notification):
    def notify(self, to: str) -> str:
        return self.sender.send("Your OTP is 43524836", to)

class ReminderNotification(Notification):
    def notify(self, to: str) -> str:
        return self.sender.send("Meeting at 5 PM", to)

# Demo

def demo():
    
    sms = SMSSender()
    email = EmailSender()
    
    otp_sms = OTPNotification(sms)
    alert_email = AlertNotification(email)
    
    print(otp_sms.notify("+1 - 774 -503-88**"))
    print(alert_email.notify("user@gmail.com"))
    
if __name__ == "__main__":
    demo()
