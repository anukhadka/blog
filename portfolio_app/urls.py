from django.urls import path, include
from . import views
app_name="portfolio_app"
urlpatterns = [
    path('index', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('', views.about, name='about'),
    path('admin-panel/addblog/', views.add_blog, name='addblog'),

]