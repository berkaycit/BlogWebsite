from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('baslik', 'yazi',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('yazar', 'yazi',)

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('info', 'avatar', 'gender',)