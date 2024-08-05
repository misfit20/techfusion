from . import views
from django.urls import path

urlpatterns = [

	path('', views.sign_up, name='sign_up'), 
	path('login/', views.login_view, name = "login"),
	path('logout_user', views.logout_user, name = 'logout'),

]
	
	