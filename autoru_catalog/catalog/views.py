from catalog.forms import MarkForm
from catalog.models import Mark, Model
from catalog.parser import parse_autoru
from django.db import transaction
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


def update_autoru_catalog(request: HttpRequest) -> JsonResponse:
    """Вью для пути заполнения базы."""
    with transaction.atomic():
        Mark.objects.all()
        marks_data = parse_autoru()
        mark_objects = [Mark(name=mark_name) for mark_name, _ in marks_data]
        Mark.objects.bulk_create(mark_objects)
        mark_objects = {mark.name: mark for mark in Mark.objects.all()}
        model_objects = []
        for mark_name, model_names in marks_data:
            mark = mark_objects[mark_name]
            model_objects.extend([Model(name=model_name, mark_id=mark) for model_name in model_names])
        Model.objects.bulk_create(model_objects)
    return JsonResponse({'status': 'success'})


def index(request: HttpRequest) -> HttpResponse:
    """Вью для главной страницы."""
    models = None
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            print('From is valid')
            selected_mark = form.cleaned_data['mark']
            models = Model.objects.filter(mark_id=selected_mark).order_by('name')
    else:
        form = MarkForm()
    return render(request, 'index.html', {'form': form, 'models': models})
