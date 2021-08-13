from django.shortcuts import render,redirect
from owner import forms

# Create your views here.
def signup(request):
    form=forms.SignUp()
    context={'form':form}
    if request.method=='POST':
        form=forms.SignUp(request.POST)
        if form.is_valid():
            return redirect('signin')

    return render(request,'signup.html',context)

def signin(request):
    form=forms.SignIn()
    context={'form':form}
    if request.method=='POST':
        form=forms.SignIn(request.POST)
        if form.is_valid():
            return redirect('addmobile')
    return render(request,'signin.html',context)


def addmobile(request):
    form=forms.AddMobile()
    context={'form':form}
    if request.method=='POST':
        form=forms.AddMobile(request.POST)
        if form.is_valid():
            company=form.cleaned_data['company']
            model_name=form.cleaned_data['model_name']
            colour=form.cleaned_data['colour']
            price=form.cleaned_data['price']
            available_pieces=form.cleaned_data['available_pieces']
            context={'company':company,'model':model_name,'colour':colour,'price':price,'available_pieces':available_pieces}
            return render(request,'add_mobile.html',context)
    return render(request,'add_mobile.html',context)
