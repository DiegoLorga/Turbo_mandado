from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def login_view(request):
    return render(request,"login/login.html")

def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        if nombre and apellidos and correo and password:
            if Usuario.objects.filter(correo=correo).exists():
                context = {'error': "Este correo ya está registrado."}
                return render(request, 'login.html', context)
            else:
                usuario = Usuario.objects.create(
                    nombre=nombre,
                    apellidos = apellidos,
                    correo=correo,
                    password=make_password(password),
                )
                print('usuaio creado')
                # Loguear automáticamente al usuario
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                #return redirect('menu_principal')
    return render(request, 'login/login.html')

def login_usuario(request):
    context = {}

    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(correo=correo)
            if check_password(password, usuario.password):
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                #return redirect('menu_principal')
            else:
                context['error_login'] = "Contraseña incorrecta."
        except Usuario.DoesNotExist:
            context['error_login'] = "Este usuario no tiene una cuenta registrada."

    return render(request, 'login/login.html', context);