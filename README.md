# Tercera-pre-entrega-Notari

Instalación
* Clonar este repositorio: git clone https://github.com/mnotari/Entrega1-Notari.git
* Crear entorno virtual: python -m venv nombre_entorno
* Activar el entorno virtual: source nombre_entorno/bin/activate o nombre_entorno\Scripts\activate si estás en windows
* Instalar las dependencias: pip install -r requirements.txt
* Realizar las migraciones: python manage.py makemigrations // python manage.py migrate

# Uso
Para iniciar el servidor, ejecuta python manage.py runserver y navega a http://localhost:8000/ en tu navegador web.

# Funcionalidades
* Registro y posterior inicicio de Sesion de usuarios registrados
* Ver y Editar perfil de usuario logueado
* Operaciones CRUD: este proyecto permite realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar) sobre Automoviles utilizando una interfaz web.

* Búsqueda de Automoviles: también se incluye una funcionalidad de búsqueda para encontrar Automoviles específicos por su nombre o descripción.

# Rutas

#Usuarios
* index/: muestra la página principal del proyecto.
* registro/: permite el registro de nuevos usuarios
* iniciar_sesion/: permite el iniciio de sesión de los usuarios
* perfil/editar: permite editar el perfil del usuario logeado
* perfil/editar/cambiar_contrasenia: permite el cambio de contraseña logueado

#Automotora
* automoviles/: muestra una lista de todos los Automoviles creados.
* automoviles/agregar/: permite crear un nuevo Automovil solo a usuario logueado
* automoviles/buscar: permite buscar automoviles
* automoviles//detalles/<int:pk> : Permite ver los detalles de un automovil en particular
* automóviles/eliminar/<int:pk>/: permite editar un Automovil existente solo a usuario logueado
* automoviles/editar/<int:pk>/: permite eliminar un Automovil existente solo a usuario logueado
* acerca_de/ : Pagina con información acerca del desarrollador

# Tecnologías utilizadas
* Django
* Bootstrap
