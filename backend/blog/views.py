from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import BlogPost, Category

PER_PAGE = 6


def _sidebar_context():
    return {
        "categories": Category.objects.all(),
        "recent_posts": BlogPost.objects.filter(is_published=True)[:5],
    }


def _page(request, queryset):
    return Paginator(queryset, PER_PAGE).get_page(request.GET.get("page"))


def post_list(request):
    posts = BlogPost.objects.filter(is_published=True).select_related("category")
    query = request.GET.get("q", "").strip()
    if query:
        posts = posts.filter(
            Q(title__icontains=query)
            | Q(excerpt__icontains=query)
            | Q(content__icontains=query)
        )
    page_obj = _page(request, posts)
    context = {
        "posts": page_obj,
        "page_obj": page_obj,
        "search_query": query,
        # Artikel unggulan hanya di daftar utama (tanpa pencarian) halaman pertama.
        "show_featured": not query and page_obj.number == 1 and page_obj.paginator.count > 0,
        **_sidebar_context(),
    }
    return render(request, "blog/list.html", context)


def posts_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = (BlogPost.objects.filter(is_published=True, category=category)
             .select_related("category"))
    page_obj = _page(request, posts)
    context = {
        "posts": page_obj,
        "page_obj": page_obj,
        "active_category": category,
        **_sidebar_context(),
    }
    return render(request, "blog/list.html", context)


def post_detail(request, slug):
    post = get_object_or_404(
        BlogPost.objects.select_related("category"), slug=slug, is_published=True
    )

    # Artikel terkait: kategori sama dulu, dilengkapi artikel lain bila kurang.
    published = BlogPost.objects.filter(is_published=True).exclude(pk=post.pk)
    related = []
    if post.category:
        related = list(published.filter(category=post.category)
                       .select_related("category")[:3])
    if len(related) < 3:
        extra = (published.exclude(pk__in=[r.pk for r in related])
                 .select_related("category")[: 3 - len(related)])
        related += list(extra)

    context = {
        "post": post,
        "related_posts": related,
        "categories": Category.objects.all(),
    }
    return render(request, "blog/detail.html", context)
