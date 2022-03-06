from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from datetime import datetime 
from home.models import contact_table,Add_product,order
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('text')
        con = contact_table(name=name,email = email,phone= phone,decs=msg ,date = datetime.today())
        con.save()
        messages.success(request, 'Your message has been sent !')
    
    return render(request,'Contact.html')

def product(request):
    Add_products = Add_product.objects.all()
    return render(request,'product.html',{'Add_products': Add_products})

def view(request,pk):
    Add_products = Add_product.objects.get(id = pk)
    return render(request,'view.html',{'Add_products': Add_products})


 
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email is already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()   
                return redirect('login')
        else:
            messages.info(request,' Password is not same Please enter correct password')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username,password=password)

        if user is not None:
        # if User.objects.filter(username=username,password=password).exists():
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,"You don't have account with this username or password !")
            return redirect('login')
    else:
        return render(request,'login.html')

def Logout(request):
    auth.logout(request)
    return redirect("/")

def dashboard(request):
    return render(request,'dashboard.html')

def welcome(request):
    if request.method =="POST":
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        quantity = request.POST.get('quantity')
        user_id =request.POST.get('user_id')
        user_name =request.POST.get('user_name')
        product_id =request.POST.get('product_id')
        ord = order(product_name = product_name,product_price = product_price,quantity = quantity,user_id=user_id,product_id=product_id,user_name=user_name1)
        ord.save()
        messages.success(request, 'Your order has been succefully placed !')

    else:
        messages.success(request, 'Your order has not been succefully placed !')
    return render(request,'welcome.html')





   