from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def home(request):
    return render(request,'core/index.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = list(User.objects.filter(email=email))
        print(email,password)
        # assert email == 'amnsns17@gmail.com'
        print(user)
        if len(user) and email==user[0].email and password == user[0].password:
            return render(request,'core/Dashboard.html', {'user':user[0]})
    return render(request,'core/Login.html')

def register(request):
    if request.method == 'POST':
        form = userf(request.POST)
        print("hi")
        if form.is_valid():
            # print(form)
            comment = form.save()
        return render(request, 'core/Login.html')
    else:
        form = userf
        return render(request,'core/Register.html',{'form':form})