from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Tag
from .forms import PostForm, UpdateForm

# Create your views here.
def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-publication_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        obj = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = obj.likes.filter(id=self.request.user.id).exists()
        context['total_likes'] = obj.total_likes()
        context['liked'] = liked
        return context

class TagPostsView(ListView):

    template_name = 'tag_posts.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.args[0])
        return Post.objects.filter(tags__in=[self.tag])

    def get_context_data(self, **kwargs):
        context = super(TagPostsView,self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    obj = get_object_or_404(Post, id=request.POST.get('post_id'))
    if obj.likes.filter(id=request.user.id).exists():
        obj.likes.remove(request.user)
    else:
        obj.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))