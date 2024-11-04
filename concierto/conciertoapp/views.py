from django.shortcuts import render
from conciertoapp.models import Persona, Entrada, Concierto
from conciertoapp.forms import PersonaForm, EntradaForm, ConciertoForm

# ---- Vistas de Persona ----

def index(reuqest):
    return render (reuqest, 'index.html')

def persona_list(request):
    personas = Persona.objects.all()
    data= {'personas': personas}
    return render(request, 'personas.html', data)

def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            personas = Persona.objects.all()
            return render(request, 'persona_list.html', {'personas': personas, 'message': 'Persona creada exitosamente'})
    else:
        form = PersonaForm()
    return render(request, 'persona_form.html', {'form': form})

def persona_update(request, pk):
    try:
        persona = Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
        return render(request, 'error.html', {'message': 'La persona no existe'})

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            personas = Persona.objects.all()
            return render(request, 'persona_list.html', {'personas': personas, 'message': 'Persona actualizada exitosamente'})
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'persona_form.html', {'form': form})

def persona_delete(request, pk):
    try:
        persona = Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
        return render(request, 'error.html', {'message': 'La persona no existe'})

    if request.method == 'POST':
        persona.delete()
        personas = Persona.objects.all()
        return render(request, 'persona_list.html', {'personas': personas, 'message': 'Persona eliminada exitosamente'})
    
    return render(request, 'persona_confirm_delete.html', {'object': persona})


# ---- Vistas de Entrada ----

def entrada_list(request):
    entradas = Entrada.objects.all()
    return render(request, 'entrada_list.html', {'entradas': entradas})

def entrada_create(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            entradas = Entrada.objects.all()
            return render(request, 'entrada_list.html', {'entradas': entradas, 'message': 'Entrada creada exitosamente'})
    else:
        form = EntradaForm()
    return render(request, 'entrada_form.html', {'form': form})

def entrada_update(request, pk):
    try:
        entrada = Entrada.objects.get(pk=pk)
    except Entrada.DoesNotExist:
        return render(request, 'error.html', {'message': 'La entrada no existe'})

    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            entradas = Entrada.objects.all()
            return render(request, 'entrada_list.html', {'entradas': entradas, 'message': 'Entrada actualizada exitosamente'})
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'entrada_form.html', {'form': form})

def entrada_delete(request, pk):
    try:
        entrada = Entrada.objects.get(pk=pk)
    except Entrada.DoesNotExist:
        return render(request, 'error.html', {'message': 'La entrada no existe'})

    if request.method == 'POST':
        entrada.delete()
        entradas = Entrada.objects.all()
        return render(request, 'entrada_list.html', {'entradas': entradas, 'message': 'Entrada eliminada exitosamente'})
    
    return render(request, 'entrada_confirm_delete.html', {'object': entrada})


# ---- Vistas de Concierto ----

def concierto_list(request):
    conciertos = Concierto.objects.all()
    return render(request, 'concierto_list.html', {'conciertos': conciertos})

def concierto_create(request):
    if request.method == 'POST':
        form = ConciertoForm(request.POST)
        if form.is_valid():
            form.save()
            conciertos = Concierto.objects.all()
            return render(request, 'concierto_list.html', {'conciertos': conciertos, 'message': 'Concierto creado exitosamente'})
    else:
        form = ConciertoForm()
    return render(request, 'concierto_form.html', {'form': form})

def concierto_update(request, pk):
    try:
        concierto = Concierto.objects.get(pk=pk)
    except Concierto.DoesNotExist:
        return render(request, 'error.html', {'message': 'El concierto no existe'})

    if request.method == 'POST':
        form = ConciertoForm(request.POST, instance=concierto)
        if form.is_valid():
            form.save()
            conciertos = Concierto.objects.all()
            return render(request, 'concierto_list.html', {'conciertos': conciertos, 'message': 'Concierto actualizado exitosamente'})
    else:
        form = ConciertoForm(instance=concierto)
    return render(request, 'concierto_form.html', {'form': form})

def concierto_delete(request, pk):
    try:
        concierto = Concierto.objects.get(pk=pk)
    except Concierto.DoesNotExist:
        return render(request, 'error.html', {'message': 'El concierto no existe'})

    if request.method == 'POST':
        concierto.delete()
        conciertos = Concierto.objects.all()
        return render(request, 'concierto_list.html', {'conciertos': conciertos, 'message': 'Concierto eliminado exitosamente'})
    
    return render(request, 'concierto_confirm_delete.html', {'object': concierto})


# Create your views here.
