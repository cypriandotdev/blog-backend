from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.text import slugify
from api.models import Category, Series, Article


def home(request):
    return render(request, 'index.html', locals())


def login_user(request):
    error = None
    if request.method == 'POST':
        username = 'admin'
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "password incorrect! try again"
    return render(request, 'login.html', locals())


@login_required()
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required()
def new(request):
    series = Series.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = slugify(request.POST.get('title'))
        tags = [x.strip() for x in request.POST.get('tags').split(",")]
        category = Category.objects.get(name=request.POST.get('category'))
        content = request.POST.get('content')
        try:
            series = Series.objects.get(name=request.POST.get('series'))
            article = Article.objects.create(title=title, slug=slug, tags=tags, series=series, category=category,
                                             content=content)
        except:
            article = Article.objects.create(title=title, slug=slug, tags=tags, category=category,
                                             content=content)
        article.save()
        return redirect('pending_article', article.slug)

    return render(request, 'new.html', locals())


@login_required()
def add_series_or_category(request):
    if request.method == 'POST':
        if request.POST.get("category") == 'category':
            category_name = request.POST.get('name')
            try:
                category = Category.objects.create(name=category_name)
                category.save()
            except:
                pass
        if request.POST.get("series") == 'series':
            series_name = request.POST.get('name')
            try:
                series = Series.objects.create(name=series_name)
                series.save()
            except:
                pass
    return JsonResponse({"success": "200 OK"}, safe=False)


@login_required()
def publish(request):
    if request.method == 'POST':
        if request.POST["publish"]:
            slug = request.POST.get("publish")
            article = Article.objects.get(slug=slug)
            article.published = True
            article.save()
    return JsonResponse({"success": "200 OK"}, safe=False)


@login_required()
def delete(request):
    if request.method == 'POST':
        if request.POST["delete"]:
            slug = request.POST.get("delete")
            article = Article.objects.get(slug=slug)
            article.delete()
    return JsonResponse({"success": "200 OK"}, safe=False)


@login_required()
def pending(request):
    pending = Article.objects.filter(published=False)
    return render(request, 'pending.html', locals())


@login_required()
def published(request):
    published = Article.objects.filter(published=True)
    return render(request, 'published.html', locals())


@login_required()
def pending_article(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'pending_article.html', locals())


@login_required()
def published_article(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'published_article.html', locals())


@login_required()
def edit_article(request, slug):
    return render(request, 'edit_article.html', locals())
