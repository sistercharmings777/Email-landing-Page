from django.db.models.signals import post_save
from .models import Contact
from django.dispatch import receiver

from django.core.mail import send_mail

@receiver(post_save, sender=Contact)
def messageadmin(sender, instance, created, **kwargs):
    if created:
        subject = "Client Subcription"
        message = "A client has made a subcription to creative blog"
        from_email = instance.email
        to_email = "sistercharmings@gmail.com"
        send_mail(subject, message, from_email, to_email, fail_silently=True)