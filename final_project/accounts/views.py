from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    messages.success(request, "Demo message")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("accounts:log_in")
    context = {'form': form}
    return render(request, "accounts/sign-up.html", context)