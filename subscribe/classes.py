from django.core.mail import EmailMessage
from abc import ABC, abstractmethod
#self is not mandatory it was used because those impl were previously used in models
#Implement ABC(Absctract base class with update method that sends message implementation in class.py)

class Observer(ABC):
    @abstractmethod
    def update(self,subject,message,email):
        pass
#Abstract class for attaching,detaching and notifying observer based on subscribe model
class Subject:
    def register(self, subscribe,observer):
        pass

    def unregister(self,subscribe, observer):
        pass

    def notify(self,subscribe,subject,message):
        pass

#The update method takes subject, message, and email as arguments.
class ConcreteObserver(Observer):
    def update(self,subject,message,email):
        print("email sent to ",email)
        send_email = EmailMessage(subject, message, to=[email])
        send_email.send()

class ConcreteSubject(Subject):
    #Here subscribe is an instance of SubscribeModel and observer is an instance of Account Model
    #The register method takes a SubscribeModel instance and an observer (user) as arguments.
    def register(self,subscribe, observer):
        subscribe.subscribers.add(observer)

    #The unregister method takes a SubscribeModel instance and an observer (user) as arguments.
    def unregister(self,subscribe, observer):
        subscribe.subscribers.remove(observer)

    #Get all subscribers from subscribe(SubscribeModel Instance) and update observer to just send message
        #The notify method takes a SubscribeModel instance, subject object, and message as arguments.
        #It loops through all subscribers of the SubscribeModel instance.
        #For each subscriber, it creates a ConcreteObserver instance and calls its update method with subject, message, and subscriber's email.

    def notify(self,subscribe,subject,message):
        for subscriber in subscribe.subscribers.all():
            observer=ConcreteObserver()
            observer.update(subject,message,subscriber.email)

