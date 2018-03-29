from django import forms
from . import models

class newQuestion(forms.Form):

    pub_date = forms.DateField(required=True, label="Date")
    question_text = forms.CharField(max_length=200, strip=True, required=True)
    choice1 = forms.CharField(max_length=200, strip=True, required=False)
    choice2 = forms.CharField(max_length=200, strip=True, required=False)
    choice3 = forms.CharField(max_length=200, strip=True, required=False)


class NewQuestionTopic(forms.Form):
    topic_name = forms.CharField(max_length=100, strip=True, required=True)
    topic_type = forms.CharField(max_length=100, strip=True, required=True)