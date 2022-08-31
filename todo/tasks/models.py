from django.db import models
class User(models.Model):
    login = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)

class task(models.Model):
    title = models.CharField(max_length = 255)
    color = models.CharField(max_length = 20)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Subtask(models.Model):
    title = models.CharField(max_length = 255)
    head_id = models.ForeignKey(task, on_delete=models.CASCADE)



# Create your models here.
