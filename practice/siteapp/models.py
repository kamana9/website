from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    image=models.ImageField(upload_to="media")
    author=models.ForeignKey("Member",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"

class Member(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    desc=models.TextField()
    image=models.ImageField(upload_to="media")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Member"    
        verbose_name_plural="Members"