from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages

# We must comment out the import that relies on the "tasks" app,
# which is currently causing the "ModuleNotFoundError".
# from tasks.models import Task  # <-- COMMENTED OUT

# We must also comment out the listener function because it uses the Task model
# as its sender, which is now commented out.

# @receiver(post_save, sender=Task) 
# def task_created_notification(sender, instance, created, **kwargs):
#  if created:
#         # Add a temporary message to the instance
#         # We need the request to show a browser popup
#         request = getattr(instance, '_request', None)
#         if request:
#             messages.success(request, f"Task '{instance.title}' added successfully!")