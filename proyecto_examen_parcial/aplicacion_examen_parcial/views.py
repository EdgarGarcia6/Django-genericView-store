from django.shortcuts import render
from .models import Libros as c
from .models import Canciones as d
from .models import Videojuegos as e
from .models import Peliculas as f
from .models import Series as g
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class Index(TemplateView):
	template_name='index.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['all_books'] = c.objects.all()
		context['all_songs'] = d.objects.all()
		context['all_games'] = e.objects.all()
		context['all_movies'] = f.objects.all()
		context['all_series'] = g.objects.all()
		return context
	#model=c
	#model2=d
	#context_object_name='all_books'
	#context_object_name2='all_songs'

class Index2(ListView):
	model=d
	context_object_name='all_songs'
	template_name='index.html'
	
#CRUD LIBROS-------------------------------------------------------
class Create_book(CreateView):
	model=c
	template_name='create_book.html'
	fields='__all__'
	success_url=reverse_lazy('list')
class Read_detail_book(DetailView):
	model=c
	template_name='read_book.html'
	context_object_name='object'
class Update_book(UpdateView):
	model=c
	template_name='update_book.html'
	context_object_name='object'
	fields='__all__'
	def get_success_url(self):
		return reverse_lazy('detail_book',kwargs={'pk':self.object.id})
class Delete_book(DeleteView):
	model=c
	template_name='delete_book.html'
	success_url=reverse_lazy('list')
	#CRUD CANCIONES-------------------------------------------------------
class Create_song(CreateView):
	model=d
	template_name='create_song.html'
	fields='__all__'
	success_url=reverse_lazy('list')
class Read_detail_song(DetailView):
	model=d
	template_name='read_song.html'
	context_object_name='object'
class Update_song(UpdateView):
	model=d
	template_name='update_song.html'
	context_object_name='object'
	fields='__all__'
	def get_success_url(self):
		return reverse_lazy('detail_song',kwargs={'pk':self.object.id})
class Delete_song(DeleteView):
	model=d
	template_name='delete_song.html'
	success_url=reverse_lazy('list')
	#CRUD VIDEOJUEGOS-------------------------------------------------------
class Create_videogames(CreateView):
	model=e
	template_name='create_videogames.html'
	fields='__all__'
	success_url=reverse_lazy('list')
class Read_detail_videogames(DetailView):
	model=e
	template_name='read_videogames.html'
	context_object_name='object'
class Update_videogames(UpdateView):
	model=e
	template_name='update_videogames.html'
	context_object_name='object'
	fields='__all__'
	def get_success_url(self):
		return reverse_lazy('detail_videogames',kwargs={'pk':self.object.id})
class Delete_videogames(DeleteView):
	model=e
	template_name='delete_videogames.html'
	success_url=reverse_lazy('list')
	#CRUD PELICULAS-------------------------------------------------------
class Create_movie(CreateView):
	model=f
	template_name='create_movies.html'
	fields='__all__'
	success_url=reverse_lazy('list')
class Read_detail_movie(DetailView):
	model=f
	template_name='read_movies.html'
	context_object_name='object'
class Update_movie(UpdateView):
	model=f
	template_name='update_movies.html'
	context_object_name='object'
	fields='__all__'
	def get_success_url(self):
		return reverse_lazy('detail_movies',kwargs={'pk':self.object.id})
class Delete_movie(DeleteView):
	model=f
	template_name='delete_movies.html'
	success_url=reverse_lazy('list')
#CRUD SERIES-------------------------------------------------------
class Create_serie(CreateView):
	model=g
	template_name='create_series.html'
	fields='__all__'
	success_url=reverse_lazy('list')
class Read_detail_serie(DetailView):
	model=g
	template_name='read_series.html'
	context_object_name='object'
class Update_serie(UpdateView):
	model=g
	template_name='update_series.html'
	context_object_name='object'
	fields='__all__'
	def get_success_url(self):
		return reverse_lazy('detail_series',kwargs={'pk':self.object.id})
class Delete_serie(DeleteView):
	model=g
	template_name='delete_series.html'
	success_url=reverse_lazy('list')