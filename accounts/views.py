from django.shortcuts import render,redirect,Http404
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    try:

        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exists')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Emaily already exists')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    messages.info(request,'Your Accout created Successfully..!')
                    return redirect('login')
            else:
                messages.info(request,'Password do not matched..!')
                return redirect('signup')
            return redirect('/')
        else:
            return render(request,'accounts/register.html')
    except:
        raise Http404("Page doesn't Exist")


def login(request):
    try:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user  = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request,'Invalid credentials')
                return redirect('login')
                
        else:
            return render(request,'accounts/login.html')
    except:
        raise Http404("Page doesn't Exist")

@login_required
def logout(request):
    try:
        auth.logout(request)
        return redirect('home')
    except:
        raise Http404("Page doesn't Exist")


