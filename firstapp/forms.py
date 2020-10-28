from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'tags')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-control'})
            # 'title': forms.TextInput(),  # attrs=({'class':'add-field'})),
            # 'author': forms.Select(),  # attrs=({'class':'add-field'})),
            # 'body': forms.TextInput(),  # attrs=({'class':'add-field'})),
            # 'tags': forms.Select(),  # attrs=({'class':'add-field'}))
        }