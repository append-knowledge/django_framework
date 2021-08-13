from django.urls import path
from owner import views
urlpatterns=[
    path('',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('books/add',views.books_add,name="addbook"),
    path('books/edit',views.books_edit,name="editbook"),
    path('books/remove',views.books_delete,name="removebook"),

    path("books/home",views.home,name="bookhome")
]