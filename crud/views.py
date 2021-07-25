from django.forms.forms import Form
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BasicDetailsForm, EducationForm
from .models import BasicDetails, Education

# Create your views here.
def add(request):
    form = BasicDetailsForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'add.html',{'form': form})

def show(request):
    s = BasicDetails.objects.all()
    return render(request, 'show.html', {'s': s})

def update(request, id):
    s = BasicDetails.objects.get(id=id)
    form = BasicDetailsForm(request.POST, instance= s)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'s': s})

def delete(request, id):
    form = BasicDetails.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')


def education(request, id):
   
    s = Education.objects.all()
    return render(request, 'education.html', {'s': s})
    


