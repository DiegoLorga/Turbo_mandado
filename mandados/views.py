from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mandado

@csrf_exempt
def crear_mandado(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        costo = request.POST.get('costo')
        numContacto = request.POST.get('numContacto')

        # Validación básica
        if not all([titulo, descripcion, costo, numContacto]):
            return JsonResponse({'success': False, 'mensaje': 'Todos los campos son obligatorios.'})

        try:
            mandado = Mandado.objects.create(
                idUsuario_id=1,  # Siempre será 1 por ahora
                titulo=titulo,
                descripcion=descripcion,
                costo=costo,
                numContacto=numContacto
            )
            return JsonResponse({'success': True, 'mensaje': 'Mandado creado exitosamente.'})
        except Exception as e:
            return JsonResponse({'success': False, 'mensaje': f'Error al crear mandado: {str(e)}'})

    return JsonResponse({'success': False, 'mensaje': 'Método no permitido.'})
