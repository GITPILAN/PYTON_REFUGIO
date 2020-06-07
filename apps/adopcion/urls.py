from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.adopcion.views import index_adopcion,SolicitudList,SolicitudCreate,SolicitudUpdate,SolicitudDelete
    

urlpatterns = [
    path('', index_adopcion),
    path('listar/', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    path('nueva/', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    path('editar/<pk>/', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    path('eliminar/<pk>/', login_required(SolicitudDelete.as_view()), name='solicitud_borrar')
]
