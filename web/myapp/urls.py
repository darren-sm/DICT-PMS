from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report, name='report'),
    path('form/', views.inputdata, name='inputdata'), 
    path('record/<category>/<str:hashed_id>', views.record, name='record'),
    path('delete_record/<category>/<str:hashed_id>', views.delete_record, name='delete_record'),
    path('<category>/<method>', views.form, name='form'),
    path('<category>/<method>/<str:hashed_id>', views.form, name='form')
]
