from django.shortcuts import render


# Create your views here.
def pokemon_list(request):
    return render(request, template_name='pokemon/list.html')


def pokemon_details(request, id):
    return render(request, template_name='pokemon/details.html')


def pokemon_type(request, id):
    return render(request, template_name='pokemon/list.html')