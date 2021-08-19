from django.db import models


class ArticleField(models.Model):
    heading = models.CharField(max_length=50)
    article = models.TextField()
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.heading} {self.created_at}"
