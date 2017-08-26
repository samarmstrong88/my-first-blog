# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render (request, 'blog/post_list.html', {'posts':posts})

def detail_list(request, post_id):
    post = Post.objects.get(pk=post_id)
    latest_comment_list = post.comment_set.order_by('created_date')[:5]
    return render (request, 'blog/detail_list.html', {
                                'post':post,
                                'lcl':latest_comment_list})
