from django.forms import ModelForm
from .models import Project, Review
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [ 'body']

        labels = {
            'body': 'Добавьте свой комментарий'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input'})


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input'})