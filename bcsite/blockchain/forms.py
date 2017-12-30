from django import forms

from .models import Post
from .models import File


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class UploadFiles(forms.ModelForm):

    class Meta:
        model = File
        fields = ('file_no', 'file_name', 'file_content', 'file_path',)
