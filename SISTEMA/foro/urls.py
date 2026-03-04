from django.urls import path
from . import views

urlpatterns = [
    # Ruta principal del foro (lista de dudas)
    path('', views.lista_dudas, name='lista_dudas'),
    
    # Ruta para crear una nueva duda (Alta)
    path('nueva/', views.crear_duda, name='crear_duda'),
    
    # Ruta para ver una duda específica y responder
    path('<int:duda_id>/', views.detalle_duda, name='detalle_duda'),
    
    # Ruta para eliminar una duda (Baja)
    path('eliminar/<int:duda_id>/', views.eliminar_duda, name='eliminar_duda'),
]