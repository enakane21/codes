from django.db import models

# Create your models here.
# [Section] Models
# Each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model

# Each field is represented by an instance of a Field class - e.g. Charfield for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds

# The name of each field instance (e.g task_name or date_created) is the field's name, in machine-friendly format. You'll use this value in your Python Code, and your database will use it as a column name

# Some Field classes have required arguments. Charfield, requires that you give it a max_length.

class ToDoItem(models.Model):
	task_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	status = models.CharField(max_length = 50, default='pending')
	date_created = models.DateTimeField('date created')