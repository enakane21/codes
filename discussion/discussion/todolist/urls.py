from django.urls import path

from . import views

# The path function can receive four arguments
# We'll focus on the two arguments that are required, which are "route" and "view" and the third argument "name" which allows us to make global changes to the url patterns of your project while only touching a single file

urlpatterns = [
	path('', views.index, name='index')
]