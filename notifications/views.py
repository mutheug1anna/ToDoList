from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from notifications.email_utils import send_welcome_email

# ----------------------------
# Signup View
# ----------------------------
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the user

            # ✅ Send the welcome email
            send_welcome_email(user.email, user.username)

            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})

# ----------------------------
# Notifications Page View
# ----------------------------
def notifications_page(request):
    # Example static notifications (replace with dynamic ones later)
    notifications = [
        {"message": "Welcome to your notifications page!", "created_at": "2025-11-14 14:00"},
        {"message": "You have 1 new task pending", "created_at": "2025-11-14 15:00"},
    ]

    # Render the notifications template and pass notifications
    return render(request, "notifications/notifications_page.html", {"notifications": notifications})