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
* Operaciones CRUD: este proyecto permite realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar) sobre objetos utilizando una interfaz web.

* Búsqueda de objetos: también se incluye una funcionalidad de búsqueda para encontrar objetos específicos por su nombre o descripción.

# Rutas
* index/: muestra la página principal del proyecto.
* listar/: muestra una lista de todos los objetos creados.
* agregar/: permite crear un nuevo objeto.
* eliminar/<int:pk>/: permite editar un objeto existente.
* editar/<int:pk>/: permite eliminar un objeto existente.
* buscar/: permite buscar objetos por su nombre.

# Tecnologías utilizadas
* Django
* Bootstrap
