from django.db import models

# Create your models here.
class Reviews(models.Model):
    username = models.CharField(max_length=20)
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Відгук від користувача {self.username}: {self.text}, опублікований {self.date}.'