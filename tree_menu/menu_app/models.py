from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.SlugField(max_length=50,
                            unique=True)
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(MenuItem, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('index', kwargs={'menu_name': self.name})

    def get_children(self):
        return MenuItem.objects.filter(parent=self).select_related('parent')

    def __str__(self):
        return f'[Name: {self.name}; Parent: {self.parent}]'
