from django.http import Http404
from django.shortcuts import render
import requests


# Create your views here.
def pokemon_list(request):
    # https://pokeapi.co/api/v2/pokemon/?limit=10
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=10'
    try:
        response = requests.get(url, timeout=4)
    except requests.exceptions.ReadTimeout:
        raise Http404("Error de conexion: Tiempo excedido")
    if response.ok:
        payload = response.json()
        items = payload.get('results', [])
        for item in items:
            url = item.get('url')
            try:
                response = requests.get(url, timeout=4)
            except requests.exceptions.ReadTimeout:
                raise Http404("Error de conexion: Tiempo excedido")
            if response.ok:
                item_details = response.json()
                item['sprites'] = item_details.get('sprites')
                item['id'] = item_details.get('id')
        return render(request, template_name='pokemon/list.html', context={'items': items, 'title': "Listado"})
    else:
        raise Http404("No hay elementos")


def pokemon_details(request, id):
    # https://pokeapi.co/api/v2/pokemon/{id or name}/
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id)
    try:
        response = requests.get(url, timeout=4)
    except requests.exceptions.ReadTimeout:
        raise Http404("Error de conexion: Tiempo excedido")
    if response.ok:
        payload = response.json()
        for type in payload.get('types',[]):
            type_id = type.get('type').get('url')
            type['id'] = type_id[31:-1]
        return render(request, template_name='pokemon/details.html', context={'details': payload})
    else:
        raise Http404("No hay elementos")


def pokemon_type(request, id):
    # https://pokeapi.co/api/v2/type/{id or name}/
    url = 'https://pokeapi.co/api/v2/type/{}/'.format(id)
    try:
        response = requests.get(url, timeout=4)
    except requests.exceptions.ReadTimeout:
        raise Http404("Error de conexion: Tiempo excedido")
    if response.ok:
        payload = response.json()
        items = payload.get('pokemon', [])
        list = []
        for item in items:
            url = item.get('pokemon').get('url')
            try:
                response = requests.get(url, timeout=4)
            except requests.exceptions.ReadTimeout:
                raise Http404("Error de conexion: Tiempo excedido")
            if response.ok:
                item_details = response.json()
                pokemon = {
                    'id': item_details.get('id'),
                    'sprites': item_details.get('sprites'),
                    'name': item.get('pokemon').get('name'),
                }
                list.append(pokemon)
                """
                Limitado a 10 resultados, en la api no hay forma de limitar cuando se filtra por tipo
                En ocasiones se devuelven mas de 100 pokemons y se harian el mismo numero de consultas 
                """
                if len(list) >= 10:
                    break
        return render(request, template_name='pokemon/list.html', context={'items': list, 'title': 'Listado '+payload.get('name')})
    else:
        raise Http404("No hay elementos")