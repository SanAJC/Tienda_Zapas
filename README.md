# Tienda Zapas

**Tienda Zapas** es una aplicación web para la gestión de una tienda de zapatos, desarrollada con Django. Permite a los usuarios ver, buscar y comprar productos, así como gestionar el inventario y los pedidos.

## Funcionalidades

- **Gestión de Productos**: Añadir, editar, eliminar y visualizar productos en la tienda.
- **Gestión de Inventario**: Control del stock disponible.
- **Sistema de Pedidos**: Realizar y gestionar pedidos.
- **Autenticación de Usuarios**: Registro, inicio de sesión y control de acceso.

## Tecnologías

- **Backend**: Django
- **Base de Datos**: SQLite (por defecto)
- **Frontend**: HTML, CSS, JavaScript
- **Despliegue**: Instrucciones para ejecutar el proyecto localmente.

## Requisitos

- **Python 3.x**
- **Django**
- **Virtualenv**

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/SanAJC/Tienda_Zapas.git
    cd Tienda_Zapas
    ```

2. Crea un entorno virtual:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones:

    ```bash
    python manage.py migrate
    ```

5. Ejecuta el servidor:

    ```bash
    python manage.py runserver
    ```

6. Accede a la aplicación en `http://127.0.0.1:8000/`.

## Uso

- **Administración**: Accede a la interfaz de administración en `/admin` para gestionar productos y pedidos.
- **Navegación**: Explora los productos disponibles y realiza pedidos a través de la interfaz de usuario.

## Estructura del Proyecto

- **`/app/`**: Contiene las aplicaciones Django que forman la funcionalidad principal.
- **`/templates/`**: Archivos HTML para la interfaz de usuario.
- **`/static/`**: Archivos estáticos como CSS y JavaScript.
- **`/manage.py`**: Script de administración de Django.

