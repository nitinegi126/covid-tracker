from django.shortcuts import render, redirect, HttpResponse
from users.forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from location.models import UserLocation, NearByUser
from django.core.serializers import serialize


# Create your views here.
def home(request):
    return render(request, 'users/home.html')


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} '
                                      f'Verify your Email')
            return redirect('tracker-login')
        else:
            context = {'form': form}
    else:
        form = UserSignupForm()
        context = {'form': form}
    return render(request, 'users/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('tracker-login')


@login_required
def profile(request):
    current_user = request.user
    profile1 = Profile.objects.get(user=current_user.id)
    location = UserLocation.objects.get(user=current_user.id)
    nu = NearByUser.objects.all().filter(main=current_user.id)
    context = {
        "profile1": profile1,
        "location": location,
        "nu": nu,

    }

    return render(request, 'users/profile.html', context)


@login_required
def checkin(request):
    points = serialize('geojson', UserLocation.objects.all())
    return HttpResponse(points, content_type='json')
