from django.shortcuts import redirect, render
from moradias.forms import MoradiaForm
from moradias.models import Moradia
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    data = {}

    # Pegar todos os imóveis e fazer páginas
    search = request.GET.get('search')
    if search:
        data['moradias'] = Moradia.objects.filter(nome__icontains=search)
        data['search'] = True
    else:
        data['moradias'] = Moradia.objects.all()

    if len(data['moradias']) > 0:
        paginator = Paginator(data['moradias'], 8)
        pages = request.GET.get('page')
        data['moradias'] = paginator.get_page(pages)

    # Pegar o último imóvel para colocar em destaque
    data['recente'] = Moradia.objects.order_by('-id')[0]

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
    # Pega o imóvel escolhido
    data['imovel'] = Moradia.objects.get(pk=pk)
    # Seleciona os 5 imoveis mais recentes
    data['outros'] = Moradia.objects.order_by('-id')[:4]

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


def telaLogin(request):
    return render(request, 'login.html')


def logar(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('home')


def deslogar(request):
    logout(request)
    return redirect('home')


def telaRegistro(request):
    return render(request, 'register.html')


def registrar(request):
    usuario = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    usuario.first_name = request.POST['first_name']
    usuario.last_name = request.POST['last_name']
    usuario.save()
    return redirect('home')
