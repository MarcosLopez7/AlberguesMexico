from django.conf import settings
from django.db import models


class Refuge(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=140)
    coordinate_x = models.DecimalField(max_digits=24, decimal_places=12, null=True)
    coordinate_y = models.DecimalField(max_digits=24, decimal_places=12, null=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=25)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='refuge')

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Post(models.Model):

    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    enable_beds = models.IntegerField()
    refuge = models.OneToOneField(Refuge)

    class Meta:
        ordering = ['update', ]

    def __str__(self):
        return '{0} post'.format(self.refuge.name)


class Need(models.Model):

    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    post = models.ForeignKey(Post, related_name='needs', on_delete=models.CASCADE)

    def __str__(self):
        return '{0}, de {1}'.format(self.product, self.post.refuge.name)
