from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return '%s %s' % (self.name, self.email)

    # class Meta:
    #     verbose_name = 'My Subscriber'
    #     verbose_name_plural = 'A lot of subscribers'