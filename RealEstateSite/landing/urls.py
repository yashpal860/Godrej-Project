# landing/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('submit-contact_us/', views.submit_contact_us, name='submit_contact_us'),
    path('submit-enquiry/', views.submit_enquiry, name='submit_enquiry'),
    path('save-brochure/', views.save_brochure_request, name='save_brochure'),
    
     
]
