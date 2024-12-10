from xml.sax.handler import all_properties

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from.models import Property

from django.core.mail import send_mail
from django.contrib import messages
from .models import Question
from .forms import PropertyForm
from.models import Agent


def  index(request):


    context = {'message': 'welcome to home page!'}
    return render(request, 'index.html', context)

def about(request):
    context = {'message': 'about!'}
    return render(request, 'about us.html', context)

def contact(request):
    context = {'message': 'contact!'}
    return render(request, 'contact_us.html', context)



def properties(request):
    all_properties = property.objects.all()
    return render(request, 'properties.html', {'properties': all_properties})




def property_detail(request, pk):
    property = get_object_or_404(Property,id=property_detail)
    return render(request, 'properties/property_detail.html', {'property': property})


def properties_view(request):
    all_properties = Property.objects.all()
    return render(request, 'properties.html', {'properties': all_properties})




def contact_us(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')


        send_mail(
            'New Question from ' + name,
            f'Question: {question}\n\nContact Info: {name}, {email}',
            'info@bluepeakrealty.com',
            ['agents@bluepeakrealty.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your question has been submitted successfully. Our agents will get back to you shortly!')
        return redirect('contact_us')

    return render(request, 'contact_us.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')

        Question.objects.create(name=name, email=email, question=question)

        messages.success(request, 'Your question has been submitted successfully. Our agents will get back to you shortly!')
        return redirect('contact_us')

    return render(request, 'contact_us.html')



def property_details_view(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_details.html', {'property': property})


def create_property(request):
    if request.method == 'POST' and request.FILES:
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property-list')
    else:
        form = PropertyForm()
    return render(request, 'create_property.html', {'form': form})


def agents_view(request):
    agents = Agent.objects.all()  # Fetch all agents from the database
    return render(request, 'agents.html', {'agents': agents})