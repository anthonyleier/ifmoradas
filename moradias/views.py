from django.forms.widgets import DateTimeBaseInput
from django.shortcuts import redirect, render
from moradias.forms import MoradiaForm, ImagemForm
from moradias.models import Moradia, Imagem
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def erro(request, mensagem):
    if not request.user.is_authenticated: return redirect('telaLogin')
    data = {}
    data['erro'] = mensagem
    return render(request, 'erro.html', data)


def home(request):
    if not request.user.is_authenticated: return redirect('telaLogin')
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
    try:
        data['recente'] = Moradia.objects.order_by('-id')[0]
        data['imagemRecente'] = Imagem.objects.filter(imovel=data['recente'].id).order_by('-id')[0]
    except:
        print("Erro")
    imagens = []
    for moradia in data['moradias']:
        try:
            imagens.append(Imagem.objects.filter(imovel=moradia.id).order_by('-id')[0])
        except:
            print("Erro")
    data['imagens'] = imagens 
    return render(request, 'index.html', data)


def novo(request):
    if not request.user.is_authenticated: return redirect('telaLogin')
    data = {}
    data['form'] = MoradiaForm()
    return render(request, 'form.html', data)


def telaImagem(request, pk):
    if not request.user.is_authenticated: return redirect('telaLogin')
    data = {}
    data['form'] = ImagemForm()
    data['imovel'] = pk
    return render(request, 'imagem.html', data)


def novaImagem(request):
    if not request.user.is_authenticated: return redirect('telaLogin')
    try:
        nova_imagem1 = Imagem(arquivo=request.FILES['imagem1'], imovel=request.POST['imovel'])
        nova_imagem1.save()
        nova_imagem2 = Imagem(arquivo=request.FILES['imagem2'], imovel=request.POST['imovel'])
        nova_imagem2.save()
        nova_imagem3 = Imagem(arquivo=request.FILES['imagem3'], imovel=request.POST['imovel'])
        nova_imagem3.save()
        nova_imagem4 = Imagem(arquivo=request.FILES['imagem4'], imovel=request.POST['imovel'])
        nova_imagem4.save()
    except:
        print("Erro")

    return redirect('home')


def create(request):
    if not request.user.is_authenticated: return redirect('telaLogin')
    form = MoradiaForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
        retorno = form.save()
        return redirect("telaImagem", retorno.id)
    else:
        return erro(request, form)


def detalhes(request, pk):
    if not request.user.is_authenticated: return redirect('telaLogin')
    data = {}
    # Pega o imóvel escolhido
    data['imovel'] = Moradia.objects.get(pk=pk)

    # Seleciona os 5 imoveis mais recentes
    data['moradias'] = Moradia.objects.order_by('-id')[:4]

    # Pega as últimas 5 fotos desse imóvel
    data['fotos'] = Imagem.objects.filter(imovel=pk).order_by('-id')[1:3]

    data['principal'] = Imagem.objects.filter(imovel=pk).order_by('-id')[0]
    print(data['imovel'].dono)
    data['dono'] = User.objects.filter(id=data['imovel'].dono)[0]
    
    imagens = []
    for moradia in data['moradias']:
        try:
            imagens.append(Imagem.objects.filter(imovel=moradia.id).order_by('-id')[0])
        except:
            print("Erro")

    data['imagens'] = imagens
    return render(request, 'detalhes.html', data)


def editar(request, pk):
    if not request.user.is_authenticated: return redirect('telaLogin')
    data = {}
    data['moradias'] = Moradia.objects.get(pk=pk)
    data['form'] = MoradiaForm(instance=data['moradias'])
    return render(request, 'form.html', data)


def update(request, pk):
    if not request.user.is_authenticated: return redirect('telaLogin')
    data = {}
    data['moradias'] = Moradia.objects.get(pk=pk)
    if request.user.id == data['moradias'].dono: form = MoradiaForm(request.POST or None, instance=data['moradias'])
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return erro(request, form.errors)


def remover(request, pk):
    if not request.user.is_authenticated: return redirect('telaLogin')
    db = Moradia.objects.get(pk=pk)
    if request.user.id == db.dono: db.delete()
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
        return erro(request, "Não foi possível realizar o login utilizando essas credenciais.")


def deslogar(request):
    if not request.user.is_authenticated: return redirect('telaLogin')
    logout(request)
    return redirect('home')


def telaRegistro(request):
    return render(request, 'register.html')


def registrar(request):
    usuario = User.objects.create_user(
        request.POST['email'], request.POST['email'], request.POST['password'])
    usuario.first_name = request.POST['first_name']
    usuario.last_name = request.POST['last_name']
    usuario.save()
    return redirect('home')

def meusImoveis(request):
    if not request.user.is_authenticated: return redirect('telaLogin')
    data = {}

    data['moradias'] = Moradia.objects.filter(dono=request.user.id)

    if len(data['moradias']) > 0:
        paginator = Paginator(data['moradias'], 8)
        pages = request.GET.get('page')
        data['moradias'] = paginator.get_page(pages)

    imagens = []
    for moradia in data['moradias']:
        try:
            imagens.append(Imagem.objects.filter(imovel=moradia.id).order_by('-id')[0])
        except:
            print("Erro")
    data['imagens'] = imagens 
    
    return render(request, 'proprio.html', data)
