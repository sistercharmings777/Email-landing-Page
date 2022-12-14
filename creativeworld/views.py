from django.conf import settings
from django.shortcuts import redirect, render

from creativeworld.models import Contact, ContactAdmin, Subscription

from django.contrib import messages
from django.core.mail import send_mail

# from dotenv import load_dotenv
# load_dotenv


def index(request):

    admincontacts = ContactAdmin.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
    #check whether email exixsts in db
        clientemail = email
        useremail = Contact.objects.filter(email=email)
        if useremail.exists():
            messages.error(request, "Email already exists")
            return redirect('/')
       
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        
        # Contact Admin
        subject = "Enquiry"
        message = f"An enquiry was made from {clientemail}\n\n Visit admin site to see more.\n\n Thank You!."
        from_email = clientemail
        to_list = ["sistercharmings@gmail.com"]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
    context = {
            'admincontacts': admincontacts
    }

    return render(request, 'pages/index.html', context)


def subscription(request):

    if request.method == "POST":
        email = request.POST.get('email')

        usermail = Subscription.objects.filter(mail=email)
        if usermail.exists():
            messages.error(request, 'This email has already subcribed')
            return redirect('index')
        
        mail = Subscription(mail=email)
        mail.save()
        

        #Email message
        subject = "Welcome to Creative World"
        message = "Thank you for subscribing to creativeminds"
        from_email = settings.EMAIL_HOST_USER
        to_list = [mail]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

    return render(request, 'pages/index.html')

