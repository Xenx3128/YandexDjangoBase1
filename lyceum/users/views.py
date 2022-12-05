from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileForm, SignUpForm
from .models import User


def register(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('homepage:home')
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
    else:
        form = ProfileForm(instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('homepage:home')
    context = {
        'form': form,
    }
    return render(request, 'users/profile.html', context)


def user_list(request):
    users = User.objects.filter(is_active=True)
    context = {
        'users': users,
    }
    return render(request, 'users/user_list.html', context)


def user_detail(request, pk):
    user = get_object_or_404(
        User,
        pk=pk,
        is_active=True
    )
    context = {
        'user': user,
    }
    return render(request, 'users/user_detail.html', context)
