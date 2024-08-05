from . import views
from django.urls import path


urlpatterns = [

	path('', views.sign_up, name='sign_up'), 
	path('login/', views.login_view, name = 'login'),
	path('logout/', views.logout_user, name = 'logout'),
	path('create-post/', views.create_post, name = 'create-post'),
	

]
	
	