from django.db.models import Prefetch, QuerySet

from tabom.models import Article, Like


def get_an_article(article_id: int) -> Article:
    article = Article.objects.filter(id=article_id).get()
    return article


def get_article_list(user_id: int, offset: int, limit: int) -> QuerySet[Article]:
    return (
        Article.objects.order_by("-id")
        .prefetch_related("like_set")
        .prefetch_related(Prefetch("like_set", queryset=Like.objects.filter(user_id=user_id), to_attr="my_likes"))[
            offset : offset + limit
        ]
    )
