from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'tags')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'input'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'ckeditor'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-control'})
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'tags')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-control'})
        }