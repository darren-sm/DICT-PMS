from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report, name='report'),
    path('form/', views.inputdata, name='inputdata'),
    path('form/cpms/', views.cpms_create_view, name='cpms_form'),
    path('form/examinees/', views.examinees_create_view, name='examinees_form'),
    path('form/ojt-input/', views.ojt_input_create_view, name='ojt_input_form'),    
    path('record/<category>/<primary_key>', views.record, name='record')
]
