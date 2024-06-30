from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name = 'Lessons', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

