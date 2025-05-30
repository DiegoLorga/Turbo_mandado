from mandados.models import Mandado
from django.shortcuts import render

def dashboard_view(request):
    usuario_id = request.session.get('usuario_id')
    usuario_nombre = request.session.get('usuario_nombre')

    # Solo mostrar mandados que no tienen repartidor asignado
    mandados = Mandado.objects.filter(repartidor__isnull=True).order_by('-fecha')

    context = {
        'usuario_id': usuario_id,
        'usuario_nombre': usuario_nombre,
        'mandados': mandados,
    }
    return render(request, 'dashboard/dashboard.html', context)