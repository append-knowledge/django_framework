from django.shortcuts import render

# Create your views here
from maths import forms


def home(request):
    return render(request, 'index.html')


def add_num(request):
    form = forms.CalculationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 + num2
            context = {}
            context['result'] = res
            print(res)
            return render(request, 'add_num.html', context)
    return render(request, 'add_num.html', context)


def sub_num(request):
    form = forms.CalculationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 - num2
            context = {}
            context['result'] = res
            return render(request, 'sub_num.html', context)

    return render(request, 'sub_num.html', context)


def mul_num(request):
    form = forms.CalculationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 * num2
            context = {}
            context['result'] = res
            return render(request, 'mul_num.html', context)
    return render(request, 'mul_num.html', context)


def div_num(request):
    form=forms.CalculationForm()
    context={'form':form}
    if request.method=='POST':
        form=forms.CalculationForm(request.POST)
        if form.is_valid():
            num1=form.cleaned_data['num1']
            num2=form.cleaned_data['num2']
            res=num1/num2
            context={'result':res}
            return render(request,'div_num.html',context)
    return render(request,'div_num.html',context)


def cube_num(request):
    form = forms.Cube()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.Cube(request.POST)
        if form.is_valid():
            num = form.cleaned_data['num']
            res = num ** 3
            context = {}
            context['result'] = res
            return render(request, 'cube_num.html', context)
    return render(request, 'cube_num.html', context)
