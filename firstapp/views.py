from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

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
