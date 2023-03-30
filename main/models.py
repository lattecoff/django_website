from django.db import models

# Create your models here.
class Task(models.Model):
	class Meta:
		verbose_name = "Задача"
		verbose_name_plural = "Задачи"
	
	title = models.CharField("Название", max_length=50)
	task = models.TextField("Описание")

	def __str__(self):
		return self.title

