from django.urls import path
from .views import (
    HomePageView, AboutPageView, ArchivesPageView,
    CoursesPageView, ProjectsPageView, NewsPageView, ContactPageView,FormationsPageView,WebDevPageView,
    DjangoAdvPageView, PythonDataPageView, UIUXPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('archives/', ArchivesPageView.as_view(), name='archives'),
    path('courses/', CoursesPageView.as_view(), name='courses'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('formations/', FormationsPageView.as_view(), name='formations'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('formations/web-development/', WebDevPageView.as_view(), name='web_dev'),
    path('formations/advanced-django/', DjangoAdvPageView.as_view(), name='django_adv'),
    path('formations/python-data-science/', PythonDataPageView.as_view(), name='python_data'),
    path('formations/uiux-design/', UIUXPageView.as_view(), name='uiux'), 

]
