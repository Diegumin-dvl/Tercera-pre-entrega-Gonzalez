from django.urls import path
from AppPreEntreg3 import views
#from django.contrib.auth.views import LogoutView 
from django.urls import path
#from .views import custom_logout
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('login',views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='Logout'),
    path('aboutMe', views.aboutme, name="Aboutme"),  
    path('remeras', views.remeras, name="Remeras"),
    path('buzos', views.buzos, name="Buzos"),
    path('pantalones', views.pantalones, name="Pantalones"),
    path('remerasForm', views.remerasForm, name="remerasForm"),
    path('buzosForm', views.buzosForm, name="buzosForm"),
    path('pantalonesForm', views.pantalonesForm, name="pantalonesForm"),
    path('busquedaRemera',views.busquedaRemera,name="BusquedaRemera"),
    path('buscarRem/',views.buscarRem),
    path('busquedaBuzo',views.busquedaBuzo,name="BusquedaBuzo"),
    path('buscarBuzo/',views.buscarBuzo),
    path('busquedaPantalon',views.busquedaPantalon,name="BusquedaPantalon"),
    path('buscarPant/',views.buscarPant),
    path('editarRem/<remera_nombre>/', views.editarRem, name="EditarRemera"),
    path('editarBuzo/<buzo_nombre>/', views.editarBuzo, name="EditarBuzo"),
    path('editarPant/<pantalon_nombre>/', views.editarPant, name="EditarPantalon"),
    path('eliminarRem/<remera_nombre>/', views.eliminarRem, name="EliminarRemera"),
    path('eliminarBuzo/<buzo_nombre>/', views.eliminarBuzo, name="EliminarBuzo"),
    path('eliminarPant/<pantalon_nombre>/', views.eliminarPant, name="EliminarPantalon"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path("logout/", views.custom_logout, name='Logout')
]  