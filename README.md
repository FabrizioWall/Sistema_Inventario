# Aplicación Web SGI (Sistema de Gestión de Inventario)
## By Fabrizio Molinelli Wallaces
![Version](https://img.shields.io/badge/Version-1-purple.svg)

![](https://media.licdn.com/dms/image/C4D0BAQEyYj8xK_XCJg/company-logo_200_200/0/1631355042913/pyd_logo?e=2147483647&v=beta&t=Dv6lxw6vfVSyF1ntPf6bGCeONf5AdQZT-iljc93OJ9A)

<p style="text-align:justify;">
  Este proyecto está creado con el fin de haber desarrollado una aplicación totalmente funcional
  para el uso de la misma en el área de Sistemas en la empresa Grupo PyD, desde la Gerencia de Sistemas.
</p>

<p style="text-align:justify;">
  Mi nombre es Fabrizio Molinelli Wallaces y, actualmente, soy parte de la empresa en la área comentada
  anteriormente y trabajo como Analista de Soporte Técnico.
  Entonces...
</p>

## ¿Por qué?
---
<p style="text-align:justify;">
  Desde que ejerzo mi labor en el área dentro de la gerencia hemos tenido problemas de organización.
  No solo trabajamos para ayuda, mantención y soporte de los sistemas empleados en la empresa, sino que también
  estamos en constante crecimiento dentro de la empresa: en staff y en campañas, puesto que Grupo PyD se dedica a 
  servicios de Contact-Center para empresas de gran calibre como: Santander Rio, La Nacion, Qualia, etc.
</p>
<p style="text-align:justify;">
  Por esto es que necesitamos llevar un conteo e información de, por ejemplo:
    - Cantidad de Notebooks

    - ¿Hay suficientes perifericos para un futuro?

    - ¿Alcanzan las notebooks que tenemos?

    - ¿Qué operadores/personas de staff poseen notebook/computadoras/perifericos?
</p>
<p style="text-align:justify;">
  Entonces, el porque viene de la mano del control, gestión de lo que se tiene, información relevante y, lo que para mí
  es lo más importante, un plan a futuro. Viendo el presente y analizandolo, pensamos en un futuro al que queremos llegar
  con el control de nuestro inventario interno como empresa y área.
</p>

## Modelos trabajados
---
<p style="text-align:justify;">
  En esta aplicación opté por crear los modelos adecuados para apaliar nuestra necesidad como área, con sus 
  caracteristicas más distintivas y, según yo, necesarias:

  * Modelo Campaña (campania en código): representan las campañas/empresas que trabajan en el call center (Santander, BBVA,    etc.)
  * Modelo Headset y Modelo Mouse: elegí crear ambos modelos por separado, en lugar de crear un modelo 'periferico', por una cuestión de organización. Cada modelo almacena la marca de su respectivo headset y mouse, cada identificador representa una marca por ende pensé que sería más fácil así para posteriormente asignarselo a una persona que posea alguno de estos perifericos
  * Modelo Notebook: este es el modelo que más se trabajaría dentro de la empresa, constantemente estamos en reposición de notebooks a personal, solicitudes de notebooks, compras, actualizaciones de estado o nombre, entre otras peticiones.
  Cada notebook contiene su información sobre modelo, numero de serie, nombre y estado.
  * Modelo Computadora: dentro del call center hay cientos de computadoras de escritorio por la necesidad de campañas, me pareció apropiado tener un listado de las mismas ya que es importante saber cuantas máquinas hay para x cantidad de personas.
  * Modelo Persona: finalmente el modelo central, cada persona cuenta con atributos personales y otros que dependen del resto de modelos.
  <b>
    Una persona al ser creada dentro de la aplicación requiere si o si tener una notebook o PC asignada al momento de crearse, sin ello nada de este proyecto tendría sentido para satisfacer la necesidad requerida
  </b>
</p>

## Dependencias utilizadas y forma de desarrollo
---
<p style="text-align:justify;">
  A continuación paso a detallar la lista de dependencias utilizadas y que son necesarias de instalar:
  <ul>
    <li>Git</li>
    <li>Django</li>
    <li>DataTables</li>
    <li>JQuery</li>
  </ul>

  Este proyecto está hecho en base a:
    <ul>
      <li>Python3</li>
      <li>Django (Última versión)</li>
      <li>DTL (Django Template Language)</li>
      <li>Se han utilizado CBV (Class Based View)</li>
  </ul>
</p>

## Modo de uso y puntos a tener en cuenta
---
<p style="text-align:justify;">
  Voy a detallar la forma en la que trabaja el inventario y caracteristicas de la aplicación:
  <ol>
    <li>En el menú úbicado del lado izquierdo se debe crear una campaña</li>
    <li>Una vez creada la campaña, se procede a crear una notebook, con todos sus datos completos</li>
    <li>Este paso es óptativo, pero se puede crear marca de headset y/o marca de mouse para que la persona posea</li>
    <li>
      Finalmente se procede a crear a la persona (usuario) con todos los atributos requeridos, excepto headset, mouse o computadora de escritorio.
    </li>
  </ol>

  Las consideraciones a tener en cuenta son que no se pueden crear personas sin que no posean una notebook o PC de escritorio.
  Tampoco es posible que una notebook pertenezca a dos personas al mismo tiempo, en general dentro de la empresa no otorgamos PC de escritorio para que se lleven. Todo se enfoca en las notebooks.
</p>

### Otras Caracteristicas
---
<p style="text-align:justify;">

  - El proyecto cuenta con un proceso de logueo donde es obligatorio autenticarse con nombre de usuario y contraseña, sin ello no se podrá ingresar al sistema, ni visualizar ningun modelo.

  - Además, existe un panel de registración para acceder con usuario a las funcionalidades. No se aceptan caracteres númericos en nombre/s y apellido/s al momento de registrarse

  - Dentro de la aplicación el usuario va a tener un avatar por default que, si quiere, va a poder modificar con la foto que elija.

  - En la parte superior derecha de la aplicación se va a encontrar con un menú desplegable para salir de la aplicación o acceder a un panel de edición de su perfil.

  - En el panel de edición va a poder modificar mail, nombre, apellido y nombre de usuario. Desde el mismo va a poder acceder al panel de modificación de contrseña, este último cuenta con proceso de recepción y tratamiento de errores (si los hay), una vez hecho el cambio se procede a desloguear al usuario y para que ingrese con sus nuevas credenciales.
</p>

### Estructura de páginas
---
<p style="text-align:justify;">
  Todas las páginas contienen tablas que muestran los registros de cada modelo, provenientes desde la DB.

  Cada página de menú tiene sus opciones para manipular los registros.
  Tienen una barra de búsqueda para buscar los registros que coincidan con lo ingresado.
  Tienen un botón de "Creación" para crear los registros según lo que se ingrese en el formulario.

  Cada registro tiene asociado un botón de eliminación y/o actualización de dato.

  En cada página se puede exportar los datos de las tablas, completos. Esto facilita la posterior generación de informes y tratamiento de los datos extraidos de la aplicación.

  Mismo, para facilitar el proceso de entrega de notebooks, cada persona tiene en sus acciones la posibilidad de descargar un archivo .txt con el formato de entrega de notebook. Esto con el objetivo de agilización.
</p>

### Usuarios
---
<p style="text-align:justify;">
  Detallo usuario con privilegios de administrador:

  - Usuario: admin
  - Contraseña: admin.123

</p>

### Links útiles e importantes
--- 
<p style="text-align:justify;">

  - Casos Unitarios de prueba (Unit Test): [Casos de Prueba](https://docs.google.com/spreadsheets/d/1PUAJ6mnpDpb2WOapeePhtsYSDb4oKfd7MS99KBuj6Eg/edit?usp=sharing)
  
  - Video de Youtube explicativo:
  
</p>
