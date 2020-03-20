from django.shortcuts import render,redirect
from .form import UserRegForm,ProfileUpdateForm,UserUpdateForm

# Create your views here.


def profile(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request,'user/profile.html',{"title":"Profile","u_form":u_form,"p_form":p_form})

def register(request):
    if request.method== 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')   
    else:
        form = UserRegForm()
    return render(request,'user/register.html',{"title":"register","form":form})



