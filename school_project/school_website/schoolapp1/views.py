from django.shortcuts import render, redirect
from .forms import UserForm

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return redirect('schoolapp1:success')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def success(request):
    return render(request,'success.html')
