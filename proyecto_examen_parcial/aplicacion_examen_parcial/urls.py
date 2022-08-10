from aplicacion_examen_parcial import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.Index.as_view(), name='list'),
    #patrones para libros
    path('crear-libro', views.Create_book.as_view(), name='create_book'),
	path('libro/<int:pk>', views.Read_detail_book.as_view(), name='detail_book'),
	path('libro/<int:pk>/update', views.Update_book.as_view(), name='update_book'),
	path('libro/<int:pk>/delete', views.Delete_book.as_view(), name='delete_book'),
    #patrones para canciones
    path('crear-cancion', views.Create_song.as_view(), name='create_song'),
	path('cancion/<int:pk>', views.Read_detail_song.as_view(), name='detail_song'),
	path('cancion/<int:pk>/update', views.Update_song.as_view(), name='update_song'),
	path('cancion/<int:pk>/delete', views.Delete_song.as_view(), name='delete_song'),
    #patrones para videojuegos
    path('crear-videojuego', views.Create_videogames.as_view(), name='create_videogames'),
	path('videojuego/<int:pk>', views.Read_detail_videogames.as_view(), name='detail_videogames'),
	path('videojuego/<int:pk>/update', views.Update_videogames.as_view(), name='update_videogames'),
	path('videojuego/<int:pk>/delete', views.Delete_videogames.as_view(), name='delete_videogames'),
    #patrones para peliculas
    path('crear-pelicula', views.Create_movie.as_view(), name='create_movies'),
	path('pelicula/<int:pk>', views.Read_detail_movie.as_view(), name='detail_movies'),
	path('pelicula/<int:pk>/update', views.Update_movie.as_view(), name='update_movies'),
	path('pelicula/<int:pk>/delete', views.Delete_movie.as_view(), name='delete_movies'),
    #patrones para series
    path('crear-serie', views.Create_serie.as_view(), name='create_series'),
	path('serie/<int:pk>', views.Read_detail_serie.as_view(), name='detail_series'),
	path('serie/<int:pk>/update', views.Update_serie.as_view(), name='update_series'),
	path('serie/<int:pk>/delete', views.Delete_serie.as_view(), name='delete_series'),
    ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)