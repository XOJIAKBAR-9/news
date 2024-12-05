import requests

from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from main.models import *


class HomeView(View):
    def get(self, request):
        top5_categories = [
            Article.objects.filter(category__name='Jahon')[:6],
            Article.objects.filter(category__name='Jamiyat')[:6],
            Article.objects.filter(category__name='USA')[:6],
            Article.objects.filter(category__name='Sport')[:6],
            Article.objects.filter(category__name='Fan-texnika')[:6],
        ]

        context = {
            "top4_articles": Article.objects.filter(published=True).order_by('views')[:4],
            "top9_articles": Article.objects.filter(published=True).order_by('views')[:9],
            "latest_articles": Article.objects.filter(published=True).order_by('-created_at')[:10],
            "top5_categories": top5_categories,
            "top5_category_names": ['Jahon', 'Jamiyat', 'USA', 'Sport', 'Fan-texnika', ],
            "galleries": Gallery.objects.order_by('created_at')
        }
        return render(request, "index.html", context)

    def post(self, request):
        email = request.POST.get('email')
        if email is not None:
            NewsLetter.objects.create(email=email)
        return redirect('home')


class DetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        likes = Article.objects.filter(category=article.category).filter(published=True).order_by('created_at')[:2]
        comments=Article.objects.filter(comments=article.comments).filter(published=True).order_by('created_at')[:1]
        context = {
            'article': article,
            'likes': likes,
            "comments":comments,
        }
        return render(request, "detail-page.html", context)

    def post(self, request):
        image = request.POST.get('image')
        if image is not None:
            Comment.objects.create(image=image)
        return redirect('detail')
