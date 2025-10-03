# Design a system to model different types of notifications that can be sent to users. These - notifications could include email, SMS, and push notifications.
# Consider the following requirements:
# 1. Each notification type has some common properties (e.g., recipient, date) and some specific properties (e.g., email body, SMS message, push notification title and body) -T
# 2. The system should allow sending notifications of different types through a unified interface.
# 3. It should be easy to add new notification types in the future without significantly modifying
# existing code.
# 4. Consider how you would handle the actual sending mechanism

# Discuss your design choices, including the classes you would create, their relationships, and
# how you would address the requirements above using 00P principles.
# What are some potential advantages and disadvantages of your design?
#

from abc import ABC, abstractmethod


class BaseNotification(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def send_notification(self):
        pass


class EmailNotification(BaseNotification):
    def __init__(self):
        super().__init__()

    def send_notification(self):
        pass

class SMSNotification(BaseNotification):
    def __init__(self):
        super().__init__()

    def send_notification(self):
        pass
