from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from blog.models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('author', 'category')
    

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ArchivesPageView(TemplateView):
    template_name = 'pages/archives.html'

class CoursesPageView(TemplateView):
    template_name = 'pages/courses.html'

class ProjectsPageView(TemplateView):
    template_name = 'pages/projects.html'

class NewsPageView(TemplateView):
    template_name = 'pages/news.html'
    
class FormationsPageView(TemplateView):
    template_name = 'pages/formations.html'

class ContactPageView(View):
    def get(self, request):
        return render(request, 'pages/contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(name, email, message)  
        return HttpResponse("✅ Your message has been sent successfully! Thank you for reaching out.")
    
class WebDevPageView(TemplateView):
    template_name = 'pages/web_dev.html'

class DjangoAdvPageView(TemplateView):
    template_name = 'pages/django_adv.html'

class PythonDataPageView(TemplateView):
    template_name = 'pages/python_data.html'

class UIUXPageView(TemplateView):
    template_name = 'pages/uiux.html'
