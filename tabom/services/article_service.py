from tabom.models import Article


def get_an_article(article_id: int) -> Article:
    article = Article.objects.filter(id=article_id).get()
    return article
