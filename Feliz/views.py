from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Feliz.forms import EditProfileForm,SellForm
from .models import Customer,Sell
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from myproject import settings





def home(request):
   return render(request, 'feliz/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! please try some other username")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(sername)>10:
            messages.error(request, "Username must be under 10 characters")
            
        if pass1 != pass2:
            messages.error(request,"Password didnt match!")
            
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        obj=myuser.instance

        messages.success(request, "Your Account has been succesfully created.Please check your email to confirm your email address in order to activate your account")
        
        
        #Welcome Email
        
        subject = "Welcome to Feliz Property Management!!"
        message = "Hello " + myuser.first_name + "!! \n" + "We have sent you a confirmation email, please confirm your email address."
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        

        return redirect('signin')

    return render(request, 'feliz/signup.html')

#obj=form.instance
            #return render(request,'Feliz/Sell.html',{"obj":obj})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'Feliz/index.html', {'fname': fname})

        else:
            messages.error(request, "bad credentials")
            return redirect('home')

    return render(request, 'feliz/signin.html')


def aboutus(request):
    return render(request, 'Feliz/about.html')

def contact(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        query = reques.POST['query']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.email = email
        myuser.query = query

        myuser.save()

        messages.success(request, "Your message has been succesfully Received.")

        return redirect('home')

    
    return render(request, 'Feliz/contact.html')

def services(request):
    return render(request, 'Feliz/services.html')

def Apartment(request):
    return render(request, 'Feliz/Apartments.html')

def Profile(request):
    
    return render(request, 'Feliz/Profile.html')
def checkout(request):
    return render(request, 'Feliz/checkout.html') 
def sell(request):
    if request.method == "POST":
        form=SellForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,'Feliz/Sell.html',{"obj":obj})
    else:
        form=SellForm()
    img=Sell.objects.all()
    return render(request,"Feliz/Sell.html",{"img":img,"form":form})
   
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('Profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'Feliz/edit_profile.html', args)
    
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('Profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'Feliz/changepassword.html', args)
    

    
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')




