from pybo.models import Answer
from django import forms
from django.forms import widgets
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model   = Question
        fields  = ['subject', 'content']
        # widgets = {
        #             'subject' : forms.TextInput(attrs={'class':'form-control'}),
        #             'content' : forms.Textarea(attrs={'class':'form-control', 'rows' : 10})
        # } 
        labels  = {
                    'subject' : '제목',
                    'content' : '내용'

        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model  = Answer
        fields = ['content']
        label  = {
                    'content' : '답변내용'
        }