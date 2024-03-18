### Caracteristicas

- Python 3/HTML5/CSS3/JS/Bootstrap
- Probado (hasta el momento) en Google Chrome
- Dependencias:  Git/Django

# Aplicación Web: Sistema de Inventario para Grupo PYD
#### Gerencia de Sistemas

![](https://media.licdn.com/dms/image/C4D0BAQEyYj8xK_XCJg/company-logo_200_200/0/1631355042913/pyd_logo?e=2147483647&v=beta&t=Dv6lxw6vfVSyF1ntPf6bGCeONf5AdQZT-iljc93OJ9A)

##Modelos creados
---
###Vista de carpeta
| Sistema_Inventario     |
| ----------- | ----------- |
| Sistema_Inventario      | Carpeta Principal (settings.py, manage.py, etc.) |
| Aplicacion_Inventario   | Carpeta de Aplicación (models.py, templates, static) |

En la carpeta  'Aplicacion_Inventario' tendremos los modelos
<ol>
  <li>Campañas</li>
  <li>Notebooks</li>
  <li>Computadoras de Escritorio</li>
  <li>Mouses</li>
  <li>Headsets</li>
  <li>Personas (Usuarios)</li>
</ol>

---
##Modo de uso
Una vez cargado el manage.py desde consola utilizando:
- python manage.py runserver

Seleccionar link con puerto y dirigirse a la página

![Inicio de página](/static/assets/img/imagen-inicio_index-readme.jpg)

Del lado izquierdo tienen el aside_bar para poder ir entre diferentes opciones.
El circuito 'deseado' es:

<ol>
  <li>Crear una Campaña en:  PYD - Campañas > Campañas </li>
  <li>Crear una Computadora en: PYD - Computadoras > Computadoras </li>
  <li>Crear una Notebook y Perifericos en: PYD-NOTEBOOKS Y PERIFERICOS > Notebooks o Perifericos</li>
  <li>Por último, crear un Usuario en:  PYD - USUARIOS REGISTRADOS> Usuarios</li>
</ol>

## Estructura de páginas
Todas las páginas contienen tablas que muestran los registros de cada modelo, provenientes desde la DB.

Cada página de menú tiene sus opciones para manipular los registros.
Tienen una barra de búsqueda para buscar los registros que coincidan con lo ingresado.
Tienen un botón de "Creación" para crear los registros según lo que se ingrese en el formulario.

Cada registro tiene asociado un botón de eliminación y/o actualización de dato.

Aún no están en funcionamiento los botones, de las distintas páginas, para exportar datos. En el futuro, la idea, es agregar esta implementación para exportar datos de las tablas.
