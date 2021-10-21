from django.shortcuts import render


def home(request):
    data = {'imoveis': [
        {'id': '1', 'titulo': 'Casa Bonita', 'descricao': 'É bonita mesmo!',
         'imagem': 'https://cdn.vistahost.com.br/belloltd14835/vista.imobi/fotos/2738/i01olh71MA77Tz56gq_27386149f08337d06.jpg'},
        {'id': '2', 'titulo': 'Casa Feia', 'descricao': 'É feia mesmo!',
         'imagem': 'https://cdn.vistahost.com.br/belloltd14835/vista.imobi/fotos/2444/iT4Y6m5876I_24445e502fdb3d125.jpg'}
    ]}
    return render(request, 'index.html', data)
