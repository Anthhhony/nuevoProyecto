from django.shortcuts import render

def vista1(request):
    data = {
        'personaje1' : 'Marcianito',
        'descripcion1' : 'Personaje insano de otro planeta',
        'personaje2' : 'insecto',
        'descripcion2' : 'Personaje insano de otro planeta',
        'personaje3' : 'pinguino',
        'descripcion3' : 'Personaje insano de otro planeta',
    }
    
    return render(request, 'templatesApp/index.html', data)


def vista2(request):
    data = {
        'personaje1' : 'Marcianito',
        'descripcion1' : 'Personaje insano de otro planeta',

    }
    
    return render(request, 'templatesApp/descripcion.html', data)

def vista2(request):
    data = {

        'personaje2' : 'insecto',
        'descripcion2' : 'Insecto con chupalla girando',

    }
    
    return render(request, 'templatesApp/descripcion.html', data)

def vista2(request):
    data = {
        'personaje3' : 'pinguino',
        'descripcion3' : 'Personaje insano de otro planeta',
    }
    
    return render(request, 'templatesApp/descripcion.html', data)

# Create your views here.
