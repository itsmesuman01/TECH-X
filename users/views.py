from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# Create - Add a new user
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/add_user.html', {'form': form})

# Read - List all users
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# Update - Edit an existing user
def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/update_user.html', {'form': form})

# Delete - Delete a user
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('user_list')
