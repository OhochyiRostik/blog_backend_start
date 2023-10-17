from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Desc')
    author = models.CharField(max_length=255, verbose_name='Author')
    date = models.DateField(verbose_name='Date')
    image = models.ImageField(verbose_name="Image", upload_to="photo/%Y/%m/%d/")

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = "Coment"
        verbose_name_plural = 'Coments'


class Likes(models.Model):
    ip = models.CharField(max_length=100)
    pos = models.ForeignKey(Post, on_delete=models.CASCADE)