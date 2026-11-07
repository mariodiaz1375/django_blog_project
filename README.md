# Blog Django

Aplicación web de blog desarrollada con Django. Permite consultar publicaciones, crear y administrar posts, registrar usuarios y mantener un perfil con biografía, sitio web y avatar.

## Funcionalidades actuales

- Listado de publicaciones y búsqueda por título.
- Detalle de cada publicación mediante una URL con slug.
- Creación de publicaciones para usuarios autenticados, con título, contenido, estado e imagen opcional.
- Edición y eliminación de publicaciones por su autor, usuarios con permiso de cambio o superusuarios.
- Sección para que cada usuario consulte sus propias publicaciones.
- Registro, inicio y cierre de sesión.
- Perfil de usuario editable con biografía, enlace web y avatar.
- Formulario de contacto. Actualmente valida los datos y los muestra en la salida del servidor; no envía correos.
- Panel de administración de Django para gestionar publicaciones y perfiles.

Los estados disponibles para una publicación son **Borrador**, **Publicado** y **Archivado**. La lista y el detalle no filtran las publicaciones por estado.

La recuperación de contraseña tiene plantillas preparadas, pero sus rutas están desactivadas actualmente.

## Requisitos

- Python en una versión compatible con Django 6.1.
- Las dependencias indicadas en `requirements.txt`.

## Instalación y ejecución

1. Clona el repositorio y entra en su carpeta:

   ```bash
   git clone URL_DEL_REPOSITORIO
   cd django_blog_project
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   ```

   En Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   En Linux o macOS:

   ```bash
   source venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Define `SECRET_KEY`, que es obligatoria para iniciar Django. Por ejemplo, en Windows PowerShell:

   ```powershell
   $env:SECRET_KEY = "reemplaza-esto-por-una-clave-secreta"
   ```

   En Linux o macOS:

   ```bash
   export SECRET_KEY="reemplaza-esto-por-una-clave-secreta"
   ```

   La variable debe estar definida en cada terminal nueva donde ejecutes comandos del proyecto. No uses una clave de desarrollo en producción ni la guardes en el repositorio.

5. Aplica las migraciones y, si necesitas administrar el sitio, crea un usuario administrador:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

   Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Rutas principales

| Ruta | Descripción |
| --- | --- |
| `/` | Inicio |
| `/posts/` | Listado y búsqueda de publicaciones |
| `/posts/<slug>/` | Detalle de una publicación |
| `/crear_post/` | Crear publicación (requiere iniciar sesión) |
| `/mis_posts/` | Publicaciones del usuario (requiere iniciar sesión) |
| `/contacto/` | Formulario de contacto |
| `/cuentas/registro/` | Registro |
| `/cuentas/login/` | Inicio de sesión |
| `/cuentas/logout/` | Cierre de sesión |
| `/cuentas/mi_perfil/` | Perfil del usuario (requiere iniciar sesión) |
| `/cuentas/mi_perfil/editar/` | Editar perfil (requiere iniciar sesión) |
| `/admin/` | Administración de Django |

Las rutas para editar o eliminar publicaciones incluyen el slug y están disponibles desde el detalle de cada post.

## Base de datos y archivos multimedia

La configuración actual usa SQLite y guarda la base de datos en `db.sqlite3`. Aunque `mysqlclient` figura entre las dependencias, el proyecto no está configurado actualmente para conectarse a MySQL.

Las imágenes de publicaciones se guardan en `media/posts/` y los avatares en `media/avatares/`. `MEDIA_ROOT` y `MEDIA_URL` están configurados en `blog_project/settings.py`; durante el desarrollo, Django sirve esos archivos cuando `DEBUG` está activado. Para producción, configura un servidor web o un servicio de almacenamiento para los archivos multimedia y sigue la lista de verificación de despliegue de Django.
