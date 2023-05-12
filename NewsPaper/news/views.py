from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post
from .filters import PostFilter
from django_filters.views import FilterView
from .forms import NewsEditForm, NewsAddForm, ArticleAddForm

# Create your views here.
class PostsList(ListView):
    model = Post
    template_name ='news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-time_create')
    paginate_by = 10


class PostDetail(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()

class PostEdit(UpdateView):
    model = Post
    template_name = 'news_edit.html'
    form_class = NewsEditForm



class Search(FilterView):
    model = Post
    context_object_name = 'search'
    template_name = 'search.html'
    filterset_class = PostFilter

class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('')

class PostCreate(CreateView):
    model = Post
    template_name = 'news_add.html'
    form_class = NewsAddForm



class CreateAR(CreateView):
    model = Post
    template_name = 'news_add.html'
    form_class = ArticleAddForm

    def form_valid(self, form):
            post = form.save(commit=False)
            post.post_type = 'AR'
            return super().form_valid(form)
