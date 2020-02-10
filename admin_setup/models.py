from django.db import models
import uuid


# Create your models here.
class Entity(models.Model):
    app_name = models.CharField(max_length=255)
    # app_key =

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.app_name


class Survey(models.Model):
    survey_identifier = models.CharField(max_length=255)
    survey_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='survey_entity')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.survey_identifier


class SurveyQuestion(models.Model):
    question_short_title = models.CharField(max_length=255)
    question_content = models.TextField(max_length=255)

    question_survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='question_survey')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.question_short_title
