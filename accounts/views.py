from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .models import User  # Your User model
from hume.models import thumb
from videos.models import Video
from .models import User  # Your User model
from django.contrib.auth import logout

# Signup view
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])  # Encrypt the password

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('signup')

        # Create the new user
        user = User(username=username, email=email, password=password)
        user.save()

        # Show success message
        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login')

    return render(request, 'signup.html')


# Login view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # Set session to keep the user logged in
                request.session['user_id'] = user.id
                return redirect('/')  # Redirect to homepage after successful login
            else:
                messages.error(request, 'Incorrect password.')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist. Please register first.')
            return redirect('login')

    return render(request, 'login.html')

# Homepage view (after successful login)
# def homepage(request):
#     humeData = thumb.objects.all().order_by('?')
#     return render(request, 'index.html', {'humeData': humeData})


# # Index view (Only accessible to logged-in users)
# def index(request):
#     # Check if the user is logged in by checking the session for a user_id
#     if 'user_id' in request.session:
#         return render(request, 'index.html')  # Render the index page for logged-in users
#     else:
#         return redirect('login')  # Redirect to login page if not logged in


# Index view (Only accessible to logged-in users)   
def homepage(request):
    # Fetch all the video data
    humeData = thumb.objects.all().order_by('?') 
    # Check if the user is logged in by checking the session for a user_id
    if 'user_id' in request.session:
        return render(request, 'index.html', {'humeData': humeData})  # Render the index page for logged-in users
    else:
        return render(request, 'index.html', {'humeData': humeData})
    
#     # Homepage view (after successful login)
# def homepage(request):
#     humeData = thumb.objects.all().order_by('?')
#     return render(request, 'index.html', {'humeData': humeData})



def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout