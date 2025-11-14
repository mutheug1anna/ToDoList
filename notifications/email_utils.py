from django.core.mail import send_mail
from django.conf import settings 

def send_welcome_email(email, username):
    """
    Sends a simple welcome email upon user registration.
    """
    subject = "Welcome to ToDo App!"
    message = f"Hello {username},\n\nWelcome to our To-Do List app! We are happy to have you 😊."

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  
        [email],
        fail_silently=False
    )
    # Add a print statement for debug confirmation
    print(f"DEBUG: Attempted to send welcome email to {email}")

