from django.shortcuts import render,redirect

from owner import forms
# Create your views here.

def home(request):
    return render(request,"index.html")

# 8000/owner/book/add

def books_add(request):
   form=forms.AddBookForm()
   context={}
   context['form']=form
   if request.method=='POST':
       form=forms.AddBookForm(request.POST)
       if form.is_valid():
           book_name=form.cleaned_data['book_name']
           author=form.cleaned_data['author']
           price=form.cleaned_data['price']
           copies=form.cleaned_data['copies']

           context = {'book author': author, 'book name': book_name, 'price': price, 'copies': copies}
           return render(request,'book_add.html',context)
   return render(request,'book_add.html',context)



def books_edit(request):
    form=forms.EditBook()
    context={}
    context['form']=form
    if request.method=='POST':
        form=forms.EditBook(request.POST)
        if form.is_valid():
            book_id=form.cleaned_data['book_id']
            book_name = form.cleaned_data['book_name']
            price = form.cleaned_data['price']
            copies = form.cleaned_data['copies']
            context={'book id':book_id,'book name':book_name,'price':price,'copies':copies}
            return render(request, 'book_edit.html',context)

    return render(request,'book_edit.html',context)



def books_delete(request):
    form=forms.RemoveBook()
    context={'form':form}
    if request.method=='POST':
        form=forms.RemoveBook(request.POST)
        if form.is_valid():
            book_id=form.cleaned_data['book_id']
            book_name=form.cleaned_data['book_name']
            context={'book id':book_id,'book name':book_name}
            return render(request,'book_delete.html',context)

    return render(request,'book_delete.html',context)

def signup(request):
    form=forms.SignUp
    context={'form':form}
    if request.method=="POST":
        form=forms.SignUp(request.POST)
        if form.is_valid():
            return redirect("signin")
    return render(request,'sign_up.html',context)

def signin(request):
    form=forms.SignIn
    context={'form':form}
    if request.method=="POST":
        form=forms.SignIn(request.POST)
        if form.is_valid():
            return redirect("books/home")
    return render(request,'sign_in.html',context)