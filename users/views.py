from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from users.models import User
#from users.serializers import UserSerializar
from django.views.decorators.csrf import csrf_exempt
from users.forms import UserForm, RegistroFrom
from random import randint, seed
import time

'''
FUNCION index
entrada: Ninguna
Salida: Ninguna
Funcionalidad: Lleva al registro de usuarios o sorteo.
creador: evallejos
'''
def index(request):
    return render(request, 'index.html')

'''
Funcion registro_user
entrada: Ninguna
salida: Ninguna
funcionalidad: Entrega el formulario de registro al usuario y guarda los datos.
creador: evallejos
'''
def registro_user(request):
    mensaje = False
    correo = False
    id = None

    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            id = f.id
            mensaje = 'Registro OK!'
            correo = True
        else:
            mensaje = 'No se pudo registrar'

    datos = {
        'form': form,
        'mensaje': mensaje,
        'correo': correo,
        'id': id,
    }

    return render(request, 'registro.html', datos)


'''
Funcion notificacion
entrada: id del usuario
salida: Ninguna
funcionalidad: Simula el correo que recibe el usuario y lo redirige al ingreso de clave.
creador: evallejos
'''
def notificacion(request, id):

    rec = User.objects.filter(id=id).first()
    datos = {
        'nombre': rec.nombres,
        'apelldios': rec.apellidos,
        'id': id,
    }
    return render(request, 'correo.html', datos)

'''
Funcion registro_user
entrada: id del usuario
salida: Ninguna
funcionalidad: Muestra el formulario que establece las claves del usuario, y lo activa.
creador: evallejos
'''
def activar_cuenta(request, id):
    rec = User.objects.filter(id=id).first()
    mensaje = False

    if request.method != 'POST':
        form = RegistroFrom(instance=rec)
    else:
        form = RegistroFrom(request.POST, instance=rec)
        if form.is_valid():
            f = form.save(commit=False)
            f.validado = True
            f.save()
            mensaje = 'Clave guardada con exito'
        else:
            mensaje = 'Error al guardar. Las claves no coinciden'

    datos = {
        'form': form,
        'mensaje': mensaje,
    }
    return render(request, 'activar.html', datos)


'''
Funcion ver_sorteo
entrada: ninguna
salida: Ninguna
funcionalidad: Entrega la opcion de ver el ganador al usuario mediante un boton.
creador: evallejos
'''
def ver_sorteo(request):
    return render(request, 'sorteo.html')

'''
Funcion ver_sorteo
entrada: Mensaje JSON 
salida: Ninguna
funcionalidad: ENDPOINT que genera un sorteo al azar sobre los usuarios activados con anterioridad
creador: evallejos
'''
@csrf_exempt
def ganador(request):

    if request.method == 'GET':
        a_users = User.objects.filter(validado=True)
        cant_u = len(a_users)

        # Se planta la semilla para los numeros al azar
        seed(time.time())
        #se inicializa de 0 a usuarios -1 para no quedar fuera de la cantidad
        num_ganador = randint(0, cant_u-1)
        ganador = a_users[num_ganador].nombres + ' ' + a_users[num_ganador].apellidos

        #data = JSONParser().parse(request)
        return JsonResponse({'mensaje': 'OK', 'detalle': ganador}, status=200)
    else:
        return JsonResponse({'mensaje': 'error', 'detalle': 'metodo no permitido'}, status=405)
