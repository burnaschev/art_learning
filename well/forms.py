from django import forms

from well.models import Well, Lesson


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class WellForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Well
        fields = "__all__"


class LessonForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
