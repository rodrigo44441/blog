from .models import Post
from django.views.generic import DetailView, ListView

class PostView(DetailView):
	model = Post
	template_name = 'post/post_detail.html'
	context_object_name = 'post'

class PostsView(ListView):
	model = Post
	template_name = 'post/index.html'
	context_object_name = 'posts'


# def index(request):
# 	posts = Post.objects.all().order_by('-created')[:6]
# 	return render(request, 'post/index.html', {'posts':posts})
