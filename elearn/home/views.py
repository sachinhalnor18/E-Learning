from django.shortcuts import render,HttpResponse,redirect
from .models import Videos,Contact
from django.contrib import messages    #this for the we using the message user get after they fill form {form filled successfully }
from django.contrib.auth import authenticate,login,logout      # built in function for authentication log in and logout process
from django.contrib.auth.models import User
#from home import Videos
# Create your views here.


def course(request):
    videos=Videos.objects.all()
    context={ 'videos':videos,}

    return render(request, 'courses.html',context)


def home(request):
    videos=Videos.objects.all()
    context={ 'videos':videos,}

    return render(request, 'home.html',context)

def signup(request):
    if request.method =='POST':
        #Get the post parameters
        username=request.POST['username']    # request.post is dictionary in which we are storing value of username 
        fname=request.POST['fname'] 
        lname=request.POST['lname']
        email=request.POST['email']  
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
    
        #checking for error input
        if pass1 != pass2 :
             messages.error(request,"your password is nor matching")
             return redirect(home)

        #create user
        myuser=User.objects.create_user(username,email,pass1)                          #User function inbuilt function used { wwe imported from from django.contrib.auth.models import User }
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account has been successfully created")

        return redirect('home')
    else :
        return HttpResponse('404 - Not Found error')

def userlogin(request):
    if request.method =='POST':
        #Get the post parameters
        loginusername=request.POST['loginusername']    # request.post is dictionary in which we are storing value of username 
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        
        if user is not None:
            login(request , user)
            messages.success(request,"successfully login")
            return redirect('home')
        else:
            messages.error(request,"you entered wrong data")
            return redirect('home')

    
    return HttpResponse("404-Not Found")

    
def userlogout(request):
    
    logout(request)
    messages.success(request,"successfully Logged out")
        
    
    return redirect(home)


def contact(request):

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(f"{name}{email}{phone}{content}")

        if len(name)<2 or len(email)<6 or len(phone)<10 or len(content)<5:
            messages.error(request,"please fill the full form correctly")                    #This  notification display when user not filled the FORM CORRECTLY OR when is  he not filled all sections 
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"your message has been sent")                            #This  notification display after the user will form filled
    
    return render(request, 'contact.html')


def search(request):                      #currently now we are searching with the title name only But we can search with the title of the videos & we can search in both {& union the title search result and content result}
    search=request.GET['search']       # in the query variable searching word is stored
    allPost = Videos.objects.filter(title__icontains=search)
    params = {'allPost': allPost}
    return render(request,'search.html',params)


