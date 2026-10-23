# Blog Django

Proyecto base de un blog web desarrollado con Django. Incluye la configuración del proyecto `blog_project` y la aplicación principal `posts`, preparada para gestionar las publicaciones del blog.

## Instalación

### Clonar el repositorio

Reemplaza `URL_DEL_REPOSITORIO` por la URL real del repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd NOMBRE_DEL_REPOSITORIO
```

### Crear el entorno virtual

```bash
python -m venv venv
```

### Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

### Instalar las dependencias

Con el entorno virtual activo, ejecuta:

```bash
pip install -r requirements.txt
```

### Preparar la base de datos

```bash
python manage.py migrate
```

### Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador. El panel de administración está disponible en [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Aplicación principal

- `posts`: aplicación inicial del proyecto, destinada a gestionar las publicaciones del blog.

## Configuración y carga de imágenes

El proyecto guarda los archivos subidos fuera de las aplicaciones, en la carpeta `media/` ubicada en la raíz del repositorio. Esta ubicación y la URL pública se configuran en `blog_project/settings.py`:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

El modelo `Post` tiene un campo de imagen opcional (`imagen`). Django guarda cada archivo dentro de `media/posts/`, según `upload_to="posts/"`. Para procesar imágenes se instala Pillow junto con las demás dependencias (`requirements.txt`).

### Crear o actualizar una publicación con imagen

1. Inicia el servidor con `python manage.py runserver`.
2. Abre [http://127.0.0.1:8000/crear_post/](http://127.0.0.1:8000/crear_post/) para crear una publicación. Para cambiar una imagen, abre la edición de una publicación existente.
3. Completa el formulario y selecciona un archivo en el campo **Imagen del post**. El campo es opcional.
4. Envía el formulario. Si se guarda correctamente, el archivo queda en `media/posts/` y la publicación conserva su ruta en la base de datos.

El formulario usa `enctype="multipart/form-data"` para enviar archivos, y las vistas de creación y edición pasan `request.FILES` al `PostForm` para que Django procese la imagen. Las plantillas muestran la imagen cuando la publicación tiene una.

En desarrollo, `blog_project/urls.py` agrega una ruta para servir archivos bajo `MEDIA_URL` desde `MEDIA_ROOT`, pero solo cuando `DEBUG` está activado. Esta forma de servir archivos es para desarrollo; en producción hay que configurar el servidor web o un servicio de almacenamiento para publicar los archivos de `MEDIA_ROOT`.
