from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, ProfileForm
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
    return render(request, template_name='users/signup.html', context=context)


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
    return render(request, template_name='users/profile.html', context=context)


def user_list(request):
    users = User.objects.filter(is_active=1)
    context = {
        'users': users,
    }
    return render(request, template_name='users/user_list.html',
                  context=context)


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk, is_active=True)
    context = {
        'user': user,
    }
    return render(request, template_name='users/user_detail.html',
                  context=context)
