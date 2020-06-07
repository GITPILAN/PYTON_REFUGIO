from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index,mascota_view,mascota_list,mascota_edit,mascota_delete,\
MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete


urlpatterns = [
     path('', index, name='index'),
     path('nuevo', login_required(MascotaCreate.as_view()), name='mascota_crear'),
     # path('/listar', mascota_list, name='mascota_listar'),
     path('listar/', login_required(MascotaList.as_view()), name='mascota_listar'),
     # path('/editar/<int:id_mascota>/', mascota_edit, name='mascota_editar'),
     path('editar/<pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
     # path('eliminar/<int:id_mascota>/', mascota_delete, name='mascota_eliminar'),
     path('eliminar/<pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
]



