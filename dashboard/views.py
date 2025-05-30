from django.shortcuts import render

def dashboard_view(request):
    usuario_id = request.session.get('usuario_id')
    usuario_nombre = request.session.get('usuario_nombre')
    context = {
        'usuario_id': usuario_id,
        'usuario_nombre': usuario_nombre,
    }
    return render(request, 'dashboard/dashboard.html', context)

