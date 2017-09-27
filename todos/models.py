from django.db import models

class TodoSet(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class Todo(models.Model):
    todo_set = models.ForeignKey(TodoSet,
                                 null=True, blank=True)
    owner = models.ForeignKey('users.User')

    text = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    edited_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
