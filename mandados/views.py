from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mandado
from login_registro.models import Usuario 

@csrf_exempt
def crear_mandado(request):
    if request.method == 'POST':
        usuario_id = request.session.get('usuario_id')
        print(f"DEBUG - ID desde sesión: {usuario_id} (tipo: {type(usuario_id)})")

        if not Usuario.objects.filter(id=usuario_id).exists():
            return JsonResponse({'success': False, 'mensaje': 'Usuario no válido.'})

        usuario = Usuario.objects.get(id=usuario_id)

        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        costo = request.POST.get('costo')
        numContacto = request.POST.get('numContacto')

        if not all([titulo, descripcion, costo, numContacto]):
            return JsonResponse({'success': False, 'mensaje': 'Todos los campos son obligatorios.'})

        try:
            mandado = Mandado.objects.create(
                idUsuario=usuario,  # Aquí pasamos el objeto, no el ID
                titulo=titulo,
                descripcion=descripcion,
                costo=costo,
                numContacto=numContacto
            )
            return JsonResponse({'success': True, 'mensaje': 'Mandado creado exitosamente.'})
        except Exception as e:
            return JsonResponse({'success': False, 'mensaje': f'Error al crear mandado: {str(e)}'})

    return JsonResponse({'success': False, 'mensaje': 'Método no permitido.'})

def aceptar_mandado(request, mandado_id):
    mandado = get_object_or_404(Mandado, id=mandado_id)

    usuario_id = request.session.get('usuario_id')
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if mandado.repartidor is None:
        mandado.repartidor = usuario
        mandado.save()

    return redirect('seguimiento', repartidor_id=usuario.id)
