from django.shortcuts import render
from .models import Blog
from .forms  import BlogForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

def blogs(request):
	blog=Blog.objects.all()
	# context_dict = {'blog': blog}
	return render(request, 'blogs.html', {'blog':blog})

def blog_detail(request, pk):
	blog=Blog.objects.get(id=pk)
	blogs=Blog.objects.all()
	context_dict = {'blog': blog, 'blogs':blogs}
	return render(request, 'blog_detail.html', context_dict)

def contact(request):
	return render(request, 'contactme.html')

def portfolio(request):
	return render(request, 'portfolio.html')

def services(request):
	return render(request, 'services.html')

def about(request):
	return render(request, 'aboutme.html')

def add_blog(request):
	form = BlogForm()
	if request.method == 'POST':
		
		form = BlogForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')

	context_dict = {'form': form}
	return render(request, 'add_blog.html', context_dict)