from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .form import *
from mysite.models import *


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'mysite/base.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'mysite/detail.html', {'post': post})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')


def categories(request, cat_id):
    return HttpResponse(f"Def cats, cat_id = {cat_id}")
