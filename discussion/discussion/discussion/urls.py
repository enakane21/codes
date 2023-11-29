from django.contrib import admin
# Using the import keyword allows access to include function to allow use of the URL's/routes created in the previous step
# The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLcof for further processing
from django.urls import include, path

urlpatterns = [
    path('todolist/', include('todolist.urls')),
    path('admin/', admin.site.urls),
]
