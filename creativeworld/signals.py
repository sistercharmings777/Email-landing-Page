from django.db.models.signals import post_save
from .models import Contact
from .models import Subscription
from django.dispatch import receiver

from django.core.mail import send_mail

@receiver(post_save, sender=Subscription)
def messageadmin(sender, instance, created, **kwargs):
    if created:
        #Contact client
        subject = "Received"
        message = f"Dear Admin, A new subcription was made on CreativeMinds \n\n Thank You!!"
        from_email = "sistercharmings@gmail.com"
        to_list = ["asnteprince777@gmail.com", "khofi.ronald@gmail.com"]
        send_mail (subject, message, from_email, to_list, fail_silently=True)
        

@receiver(post_save, sender=Contact)
def messageclient(sender, instance, created, **kwargs):
    if created:
        subject = "Received"
        message = f"Dear {instance.name}, your enquire was recorded. \n\n Thanks You!!"
        from_email = "sistercharmings@gmail.com"
        to_list = [instance.email]
        send_mail (subject, message, from_email, to_list, fail_silently=True)
        