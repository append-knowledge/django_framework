from django.urls import path
from owner import views
urlpatterns=[
    path("",views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('mobile/add',views.addmobile,name="addmobile")
]