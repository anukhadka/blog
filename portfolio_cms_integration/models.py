from django.db import models

# Create your models here.
# from django.db import models
from cms.models import CMSPlugin
from portfolio_app.models import Blog


class BlogPluginModel(CMSPlugin):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title