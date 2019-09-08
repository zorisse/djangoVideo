# module path
from django.urls import path
from . import views

# liste des routes
urlpatterns = [
    # /movies/ index
    # la racine est defini dans le projet de depart
    path('', views.index, name='movies_index'),
    # params id => <smth_id>
    path('<movie_id>', views.detail, name='movies_detail')
]
