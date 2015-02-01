from django import forms
from course.models import Post

class PostForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
    anonymous = forms.BooleanField( required=False )

class TopicForm(forms.Form):
    title = forms.CharField( max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}) )
    body = forms.CharField(widget=forms.Textarea)
    anonymous = forms.BooleanField( required=False )
