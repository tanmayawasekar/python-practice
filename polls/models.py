# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible 

# Create your models here.


def explain(self):
        from django.db.models.query import QuerySet
        from django.db import connections
        cursor = connections[self.db].cursor()
        cursor.execute('explain %s' % str(self.query))
        return cursor.fetchall()

class QuestionManager(models.Manager):
    def explain(self):
        from django.db.models.query import QuerySet
        from django.db import connections
        cursor = connections[self.db].cursor()
        cursor.execute('explain %s' % str(self.query))
        return cursor.fetchall()

class Topic(models.Model):
    # Types of topics
    science = 'science'
    art = 'art'
    types_of_topics = (
        (science, science),
        (art, art)
    )

    # Model fields
    topic_name = models.CharField(max_length=100)
    topic_type = models.CharField(
        max_length=100,
        choices=types_of_topics
    )

class SearchManager(models.Manager):
    def search_text_from_model(self, search_text, search_field):
        return Question.objects.filter(**{search_field: search_text})
    

class Question(models.Model):
    objects = QuestionManager()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_topic = models.ForeignKey(Topic, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=[
                'question_text'
            ])
        ]
    def __str__(self):
        return self.question_text + str(self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    integer_field = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class NewModelObject(models.Manager):
    def add_new_object(self, object_props):
        return self.__class__(
            **object_props
        )

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    
