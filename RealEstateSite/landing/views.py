from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Enquiry, Contact_us, BrochureRequest
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')  # or render with context

def submit_enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Enquiry.objects.create(name=name, phone=phone, message=message)
        messages.success(request, "Enquiry submitted successfully!")
        return redirect(request.META.get('HTTP_REFERER'))
    
def submit_contact_us(request):
    if request.method == 'POST':
        Contact_us.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            message=request.POST.get('message'),
        )
        return redirect('/')



def save_brochure_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        message = request.POST.get('message')

        BrochureRequest.objects.create(
            name=name,
            email=email,
            phone=phone,
            city=city,
            message=message
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)