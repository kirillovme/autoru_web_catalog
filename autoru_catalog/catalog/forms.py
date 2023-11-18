from django import forms
from catalog.models import Mark


class MarkForm(forms.Form):
    """Форма для выбора марки автомобиля."""
    mark = forms.ModelChoiceField(
        queryset=Mark.objects.all().order_by('name'),
        label='Выберите марку:',
        empty_label='--------',
        required=False
    )
