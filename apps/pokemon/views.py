from django.http import Http404
from django.shortcuts import render
import requests


# Create your views here.
def pokemon_list(request):
    # https://pokeapi.co/api/v2/pokemon/?limit=10
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=10'
    response = requests.get(url, [])
    if response.ok:
        payload = response.json()
        items = payload.get('results', [])
        for item in items:
            url = item.get('url')
            response = requests.get(url)
            if response.ok:
                item_details = response.json()
                item['sprites'] = item_details.get('sprites')
                item['id'] = item_details.get('id')
        return render(request, template_name='pokemon/list.html', context={'items': items})
    else:
        raise Http404("No hay elementos")


def pokemon_details(request, id):
    # https://pokeapi.co/api/v2/pokemon/{id or name}/
    return render(request, template_name='pokemon/details.html')


def pokemon_type(request, id):
    # https://pokeapi.co/api/v2/type/{id or name}/
    return render(request, template_name='pokemon/list.html')