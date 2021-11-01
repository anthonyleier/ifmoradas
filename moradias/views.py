from django.shortcuts import redirect, render
from moradias.forms import MoradiaForm
from moradias.models import Moradia
from django.core.paginator import Paginator

def home(request):
    data = {}   

    search = request.GET.get('search')
    if search:
        data['moradias'] = Moradia.objects.filter(modelo__icontains=search)
    else:
        data['moradias'] = Moradia.objects.all()

    if len(data['moradias']) > 0:
        paginator = Paginator(data['moradias'], 10)
        pages = request.GET.get('page')
        data['moradias'] = paginator.get_page(pages)
    
    return render(request, 'index.html', data)

def novo(request):
    data = {}
    data['form'] = MoradiaForm()
    return render(request, 'form.html', data)

def create(request):
    form = MoradiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def detalhes(request, pk):
    data = {}
    data['item'] = Moradia.objects.get(pk=pk)
    return render(request, 'detalhes.html', data)

def editar(request, pk):
    data = {}
    data['moradias'] = Moradia.objects.get(pk=pk)
    data['form'] = MoradiaForm(instance=data['moradias'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['moradias'] = Moradia.objects.get(pk=pk)
    form = MoradiaForm(request.POST or None, instance=data['moradias'])
    if form.is_valid():
        form.save()
        return redirect('home')

def remover(request, pk):
    db = Moradia.objects.get(pk=pk)
    db.delete()
    return redirect('home')
