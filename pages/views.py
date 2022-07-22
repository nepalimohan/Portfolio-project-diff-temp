from django.shortcuts import render
from .models import Detail, Project

# Create your views here.
def home(request):
    details = Detail.objects.all()
    projects = Project.objects.all()
    data = {
        'details':details,
        'projects': projects,
    }
    return render(request, 'pages/home.html', data)