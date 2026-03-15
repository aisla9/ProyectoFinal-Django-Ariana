# Entrega Final Proyecto Django - Ariana Isla 👩🏻‍💻

## 🌐 Enlaces del Proyecto
* **Página de Inicio:** http://127.0.0.1:8000/

## 💡 Datos de prueba
Para probar todas las funcionalidades (crear posts, editar perfil, enviar mensajes), puede crear un usuario nuevo en la sección de "Registrarse" o utilizar las credenciales del administrador.

## 🔑 Acceso al panel de administración
He creado un superusuario para validar los registros, posts y perfiles:
* **URL:** http://127.0.0.1:8000/admin
* **Usuario:** admin
* **Contraseña:** admin123

## 📂 Estructura y Funcionalidades
* **Modelos:** Clase `Post` (con texto enriquecido usando CKEditor e imágenes) y modelo `Perfil` vinculado al usuario. También incluye una app de `messenger` para comunicación entre usuarios. Aunque es básica, funciona como MVP :)
* **Autenticación:** Sistema de Login, Logout y Registro optimizado para facilitar la entrada del usuario.
* **Perfiles de Usuario:** Cada usuario tiene una vista estética de su perfil con avatar, nombre real y biografía, con opción de edición y cambio de contraseña.
* **CRUD de Publicaciones:** Los usuarios pueden gestionar sus propios artículos (Crear, Leer, Actualizar, Borrar) desde la sección "Mis Posts".
* **Interfaz (UI):** Diseño moderno y responsivo usando Bootstrap 5, con colores básicos para facilitar la visualización.
* **Templates:** Uso de herencia de plantillas con un archivo `base.html` para unificar la navegación y el estilo.

## 🛠️ Requisitos de Instalación
1. Clonar el repositorio.
2. Crear un entorno virtual e instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar migraciones: `python manage.py migrate`
4. Correr el servidor: `python manage.py runserver`

**Espero le guste!! 😊**