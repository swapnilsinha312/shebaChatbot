from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
import pyrebase 
import json
import os
 

# Create your views here.



config={ 

	"apiKey": "",
      "authDomain": "",
      "databaseURL": "",
      "projectId": "",
      "storageBucket": "",
      "messagingSenderId": "",
      "appId": "",
      "measurementId": ""
} 
# Initialising database,auth and firebase for further use  
firebase=pyrebase.initialize_app(config) 
authe = firebase.auth() 
database=firebase.database() 

@login_required(login_url='login')
def app(request):
        return render(request, "chatroom.html")

def buy_portal(request): 
    return render(request,'buy_portal.html')

def about(request):
    return render(request,'about.html')

def signIn(request): 
    # print(os.path(BASE_DIR)) 
    return render(request,"accounts/Login.html") 

def home(request): 
    return render(request,"accounts/Home.html") 

def postsignIn(request): 
    email=request.POST.get('email') 
    pasw=request.POST.get('pass') 
    try: 
    # if there is no error then signin the user with given email and password 
        user=authe.sign_in_with_email_and_password(email,pasw) 
    
        session_id=user['idToken'] 
        request.session['uid']=str(session_id)
        
        uid = user['localId']
        utoken = user['idToken']

        read_obj = database.child('names').child(user['localId']).get(utoken)
        name = read_obj.val()['name']
        
        #data = {"name":name,"email":email,"uid":uid,"utoken":utoken}
        # filename="C:/Users/aj240/Downloads/sheba/infofile.json"
        # with open(filename, "w") as outfile:
        #     json.dump(data,outfile)

        #request.POST.set(cookies={"somedata":data})
        return render(request,"chatroom1.html",{"name":name,"uid":uid,"utoken":utoken})  
        #return render(request,"accounts/Home.html",{"email":email}) 

    except: 
        message="Invalid Credentials!"
        return render(request,"accounts/Login.html",{"message":message}) 

def logout(request): 
    try: 
        # data={}
        # filename="C:/Users/aj240/Downloads/sheba/infofile.json"
        # with open(filename, "w") as outfile:
        #     json.dump(data,outfile)
        del request.session['uid'] 
    except: 
        pass
    return render(request,"accounts/Login.html") 
  
def signUp(request): 
    return render(request,"accounts/Registration.html") 

def postsignUp(request): 
     email = request.POST.get('email') 
     passs = request.POST.get('pass') 
     name = request.POST.get('name') 

     try: 
        # creating a user with the given email and password 
        user=authe.create_user_with_email_and_password(email,passs) 
        uid = user['localId'] 
        # idtoken = request.session['uid'] 
        utoken=user["idToken"]
        data={"name":name}
        database.child("names").child(uid).set(data,utoken)
        print(uid) 
        return render(request,"accounts/Login.html")
     except: 
        return render(request, "accounts/Registration.html") 

     