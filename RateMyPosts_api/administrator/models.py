from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField()

    class Meta:
        db_table = 'tag'

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Post(models.Model):
    images = models.ManyToManyField('Image')
    description = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'post'


