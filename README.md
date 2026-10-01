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
