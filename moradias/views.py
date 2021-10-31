from django.shortcuts import redirect, render
from moradias.forms import MoradiaForm
from moradias.models import Moradia

def home(request):
    data = {}   

    # search = request.GET.get('search')
    # if search:
        # data['db'] = Carro.objects.filter(modelo__icontains=search)
    # else:
    data['db'] = Moradia.objects.all()

    # paginator = Paginator(data['db'], 2)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)

    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = MoradiaForm()
    return render(request, 'form.html', data)

def create(request):
    form = MoradiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def ver(request, pk):
    data = {}
    data['item'] = Moradia.objects.get(pk=pk)
    return render(request, 'ver.html', data)


def editar(request, pk):
    data = {}
    data['db'] = Moradia.objects.get(pk=pk)
    data['form'] = MoradiaForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Moradia.objects.get(pk=pk)
    form = MoradiaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def remover(request, pk):
    db = Moradia.objects.get(pk=pk)
    db.delete()
    return redirect('home')
