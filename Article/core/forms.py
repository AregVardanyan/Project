from django import forms
from core.models import ArticleField


class ArtCreateForm(forms.ModelForm):
    class Meta:
        model = ArticleField
        fields = "__all__"