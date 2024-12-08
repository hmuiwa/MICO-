
from django.contrib import admin
from django.urls import path
from careproapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('treatment/', views.treatment, name='treatment'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

]
