from typing import Any
import requests
import xml.etree.ElementTree as ET


def parse_autoru() -> list[tuple[str, Any]]:
    """Парсер марок и моделей с указанного адреса."""
    url = 'https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml'
    response = requests.get(url)
    root = ET.fromstring(response.content)
    marks = []
    for mark in root.findall('mark'):
        mark_name = mark.get('name')
        marks.append((mark_name, set()))
        for folder in mark.findall('folder'):
            model_name = folder.get('name').split(',')[0]
            marks[-1][1].add(model_name)
    return marks
