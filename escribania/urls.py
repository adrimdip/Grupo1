from django.urls import path
from . import views
from .views import EliminarActoJuridico



urlpatterns=[

    # URLs para el Escribano
    path('crear_escribano/', views.crear_escribano, name='crear_escribano'),
    # path('listar_escribanos/', views.listar_escribanos, name='listar_escribanos'),
    # path('actualizar_escribano/<int:pk>/', views.actualizar_escribano, name='actualizar_escribano'),

    #para ActoJuridico
    path('crear_acto_juridico/', views.crear_acto_juridico, name='crear_acto_juridico'),
    path('listar_actos_juridicos/', views.listar_actos_juridicos, name='listar_actos_juridicos'),
    path('actualizar_acto_juridico/<int:pk>/', views.actualizar_acto_juridico, name='actualizar_acto_juridico'),
    path('eliminar_acto_juridico/<int:pk>/', EliminarActoJuridico.as_view(), name='eliminar_acto_juridico'),
]
