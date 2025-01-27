from django.views import generic

from blog.models import Post

# class PostView(generic.View):
# 	def get(self, request, *args, **kwargs):
# 		return HttpResponse('Hello, World!')

class PostView(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by("-created_on")
	template_name = "index.html"

class PostDetail(generic.DetailView):
	model = Post
	template_name = "post_deital.html"