from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView,FormView
from django.views.generic.detail import SingleObjectMixin

from .models import Post ,Comment
from .forms import PostForm,CommentForm
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/home_page.html'

class PostNewView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'excerpt','body','photo']
    template_name = 'blog/post_update.html'
    # success_url = reverse_lazy('home')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')



# class PostDetailView(DetailView):
    # model = Post
    # template_name = 'blog/post_detail.html'
class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGetView.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPostView.as_view()
        return view(request, *args, **kwargs)


class CommentGetView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class CommentPostView(SingleObjectMixin,FormView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail',kwargs={'pk':post.pk})