from django.shortcuts import redirect, render
from .models import Detail, Project
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
        message_body = 'Name: ' + name + '. Email: ' + email + '. Message' + message
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
                subject,
                message_body,
                'rockerdeula@gmail.com',
                [admin_email],
                fail_silently=False,
                )
        return redirect('home')
        
    else:   
        details = Detail.objects.all()
        projects = Project.objects.all()
        data = {
            'details':details,
            'projects': projects,
        }
        return render(request, 'pages/home.html', data)