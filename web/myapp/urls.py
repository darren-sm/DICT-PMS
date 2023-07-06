from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report, name='report'),
    path('cpms_form/', views.cpms_create_view, name='cpms_form'),
    path('examinees_form/', views.examinees_create_view, name='examinees_form'),
    path('ojt_input_form/', views.ojt_input_create_view, name='ojt_input_form'),


]
