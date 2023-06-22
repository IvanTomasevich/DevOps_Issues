# DevOps Center
## Sistema Integral de Gestion de Ticket (SIGT)

Proyecto final curso Python CoderHouse comisión 40440

<!-- Reemplaza `VIDEO_ID` con el ID real de tu video de YouTube -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/mYnPZ49RCQE" frameborder="0" allowfullscreen></iframe>

<iframe width="2383" height="985" src="https://www.youtube.com/embed/udssHLrTzTU" title="&quot;Lo Que No Muere&quot; (EPK - Backstage)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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



