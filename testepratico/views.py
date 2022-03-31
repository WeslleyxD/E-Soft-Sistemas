from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib import messages
from .api import api
from django.core.paginator import Paginator

# Create your views here.

def cadastrar(request):

    #Chamando a API
    lista_api = api()

    #Tratando o json da API
    nome = f'{lista_api[0]} {lista_api[1]}'
    sobrenome = lista_api[2]

    #Passando o nome e sobrenome no context para ser utilizado no template
    context = {
        'nome' : nome,
        'sobrenome' : sobrenome,
    }

    #Verifica se o metodo é POST e pega o post do form cadastro
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        idade = request.POST.get('idade')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        apelido = request.POST.get('apelido')
        observacao = request.POST.get('observacao')

        #Verifica se os campos obrigatórios não foram preenchidos, caso não estejam preechidos, aparece uma mensagem de erro.
        if not nome or not sobrenome or not email or not idade or not data_nascimento or not email:
            messages.error(request, 'Preencha todos os campos obrigatórios os quais são identificados com o sinal de " * " (Asterisco).')

            return render(request, 'cadastrar.html', context)

        #Cria um Usuarios com os argumentos recebidos do form cadastro
        usuario = Usuarios.objects.create(nome=nome, sobrenome=sobrenome, idade=idade, data_nascimento=data_nascimento, email=email,
        apelido=apelido, observacao=observacao)

        usuario.save()

        return redirect('listar_cadastros')

    return render(request, 'cadastrar.html', context)



def listar_cadastros(request):
    #Obtém o model Usuarios
    usuarios = Usuarios.objects.all()

    #Seção de busca por meio do nome
    if request.method == "POST":

        #Obtém o post do form buscar e se for vazio redireciona para listar_cadastros
        buscar = request.POST.get('buscar')
        if buscar == "":
            return redirect('listar_cadastros')

        #Filtra no campo (nome) do model Usuarios se existe o argumento recebido do form buscar
        usuarios = Usuarios.objects.filter(nome__icontains=buscar)
    
        context = {
                'buscar' : buscar,
                'usuarios' : usuarios,
        }

        return render(request, 'listar_cadastros.html', context)

    #Paginação
    paginator = Paginator(usuarios, 5) #Mostra 5 por página

    page = request.GET.get('p')
    usuarios = paginator.get_page(page)

    context = {
        'usuarios' : usuarios,
    }

    return render(request, 'listar_cadastros.html', context)



def editar_cadastro(request, usuario_id):
    #Obtém o um único usuario do model Usuarios por meio do id recebido do template.
    usuario = Usuarios.objects.get(id=usuario_id)

    context =  {
        'usuario' : usuario,
    }

    #Verifica se o metodo é POST e pega o post do form editar
    if request.method=="POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        idade = request.POST.get('idade')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        apelido = request.POST.get('apelido')
        observacao = request.POST.get('observacao')

        #Atualiza os dados do usuario do model Usuarios por meio do argumento recebido do form editar
        usuario = Usuarios.objects.filter(id=usuario_id).update(nome=nome, sobrenome=sobrenome, idade=idade, data_nascimento=data_nascimento, email=email,
        apelido=apelido, observacao=observacao)

        return redirect('listar_cadastros')
    
    return render(request, 'editar_cadastro.html', context)



def excluir_cadastro(request, usuario_id):
    #Obtém o um único usuario do model Usuarios por meio do id recebido do template.
    usuario = Usuarios.objects.get(id=usuario_id)

    context =  {
        'usuario' : usuario,
    }

    #Verifica se o metodo é POST e deleta o usuario selecionado
    if request.method == 'POST':
        usuario.delete()
        return redirect ('listar_cadastros')

    return render(request, 'excluir_cadastro.html', context)