from django import forms
from django.forms import ModelForm, widgets

from .models import Project, Review

# when creating a form based on a particular model,
# name the class the name of the model and then append Form
class ProjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add title'})
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})


    class Meta:
        model = Project
        # this selects all the fields from the selected model 
        # fields = '__all__'  # based on documentation, it is better to list out the fields to avoid accidentally exposing fields that should not be exposed
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']
        # widgets allows us to set what kind of widget (HTML element) should represent which field in the model
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})
    
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote', 
            'body': 'Add a comment with your vote'
        }