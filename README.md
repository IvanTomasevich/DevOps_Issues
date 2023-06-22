# DevOps Center
## Sistema Integral de Gestion de Ticket (SIGT)

Proyecto final curso Python CoderHouse comisión 40440


[![Video](https://img.youtube.com/vi/RoFFtYjT2bk/0.jpg)](https://www.youtube.com/watch?v=RoFFtYjT2bk)

Para el proyecto se utilizaron las siguientes herramientas y tecnologías.

* SO [ArcoLinuxB](https://arcolinuxb.com/)  | [Qtile WM](https://qtile.org/)
* IDE [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=linux)
* Gestor de base de datos [Dbeaver Community](https://dbeaver.io/)
* [Python 3.11.3](https://www.python.org/downloads/) 'siempre a la última moda de París'

## Plan de gestión de la configuración SIGT

* Clonar el [repositorio](https://github.com/IvanTomasevich/DevOps_Issues.git)
* En el directorio raíz del repositorio, abrir un terminal y ejecutar el command para instalar las dependencias:

Primero actualizamos a la última moda nuestro pip:
```commandline
python -m pip install --upgrade pip
```
Luego instalamos las dependencias leyendo el archivo txt:
```commandline
python -m pip isntall -r requirements.txt
```
* ¡Si todo salió bien es hora de darle marcha al sever!
Para esto ejecutar el sig. command pero esta vez dentro del project dir "JiraTk/".
```commandline
python manage.py runserver
```

### Cuadro de usuarios

| User      | Pass         | is_superuser |
|-----------|--------------|:-------------|
| DartVader | DevOps123    | yes          |
| Piky      | Chocolate23  |              |
| Amatista  | sabado.23    |              |

### Test unitario

Se realizó la ejecución de 7 test sobre el model principal Ticket dando como resultado la siguiente salida por consola.

```commandline
(venv) [ivan@arch JiraTk]$ python manage.py test
Found 7 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.011s

OK
Destroying test database for alias 'default'...
(venv) [ivan@arch JiraTk]$ 

```

Para ejecutar estos test dentro del project dir "JiraTk/" correr el command:

```commandline
python manage.py test
```

