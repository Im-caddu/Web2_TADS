from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def submit_register(request):
    if request.method == 'POST':
        nome = request.POST.get('registerName')
        email = request.POST.get('registerEmail')
        senha = request.POST.get('registerPassword')
        return HttpResponse(f"Nome: {nome}, Email: {email}, Senha: {senha}")
    return HttpResponse("Requisição inválida")