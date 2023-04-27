# Tercera-pre-entrega-Notari

Instalación
* Clonar este repositorio: git clone https://github.com/mnotari/Tercera-pre-entrega-Notari.git
* Crear entorno virtual: python -m venv nombre_entorno
* Activar el entorno virtual: source nombre_entorno/bin/activate o nombre_entorno\Scripts\activate si estás en windows
* Instalar las dependencias: pip install -r requirements.txt
* Realizar las migraciones: python manage.py makemigrations // python manage.py migrate

# Uso
Para iniciar el servidor, ejecuta python manage.py runserver y navega a http://localhost:8000/ en tu navegador web.

# Funcionalidades
* Operaciones CRUD: este proyecto permite realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar) sobre Automoviles utilizando una interfaz web.

* Búsqueda de Automoviles: también se incluye una funcionalidad de búsqueda para encontrar Automoviles específicos por su nombre o descripción.

# Rutas
* index/: muestra la página principal del proyecto.
* listar/: muestra una lista de todos los Automoviles creados.
* agregar/: permite crear un nuevo Automovil.
* eliminar/<int:pk>/: permite editar un Automovil existente.
* editar/<int:pk>/: permite eliminar un Automovil existente.
* buscar/: permite buscar Automoviles por su nombre.

# Tecnologías utilizadas
* Django
* Bootstrap
