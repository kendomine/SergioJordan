from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import View
from .models import Blog



def index(request):
	blog = Blog.objects.all()[:10]

	context ={
		'title': 'Latest Announcements',
		'blog': blog
	}
	return render(request,'blog/index.html',context)


def details(request, id):

	blog = Blog.objects.get(id=id)

	context ={

		'blog' : blog
	}

	return render(request,'blog/details.html', context)	

