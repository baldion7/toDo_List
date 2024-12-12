# Gestor de Tareas - Django 

## 📋 Descripción del Proyecto

Un sistema completo de gestión de tareas desarrollado con Django que permite a los usuarios crear, editar, eliminar y administrar sus tareas con diferentes estados.

![Captura de Pantalla](screenshot.png)

## ✨ Características

- **Crear Tareas**: Agrega nuevas tareas con título, descripción y estado
- **Gestión de Estados**: Cambia el estado de las tareas (Pendiente, En Proceso, Completado, Cancelado)
- **Exportación/Importación**: Exporta e importa tareas en formato JSON
- **Interfaz Amigable**: Diseño responsivo con Bootstrap
- **Persistencia de Datos**: Almacenamiento en base de datos SQLite

## 🚀 Requisitos Previos

- Python 3.8+
- Django 4.2+
- pip
- (Opcional) entorno virtual de Python

## 🔧 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/TuUsuario/gestor-tareas-django.git
cd gestor-tareas-django
```

### 2. Crear Entorno Virtual (Opcional pero Recomendado)

```bash
# En Windows
python -m venv .venv
.venv\Scripts\activate

# En macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos

```bash
python manage.py migrate
```

### 5. Crear Usuario Administrador (Opcional)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

## 🌐 URLs del Proyecto

- **Página Principal**: `http://localhost:8000/taskes/`
- **Panel de Administración**: `http://localhost:8000/admin/`

## 📦 Estructura del Proyecto

```
toDo_List/
│
├── manage.py
│
├── toDo_List/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── templates/
    ├── base.html
    ├── index.html
    └── edit_task.html
```

## 🧩 Modelos

### Modelo de Tarea (ToDo)

- **Título**: Máximo 100 caracteres
- **Descripción**: Texto opcional
- **Estado**: Seleccionable (Pendiente, En Proceso, Completado, Cancelado)
- **Fechas**: Creación y última actualización automáticas

## 🔒 Funcionalidades de Seguridad

- Protección contra CSRF
- Validación de formularios
- Control de estados de tareas

## 🤝 Contribuciones

1. Haz un fork del proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Distribuido bajo la Licencia MIT. Consulta `LICENSE` para más información.

## 🛠️ Tecnologías Utilizadas

- Python 3
- Django
- Bootstrap 5
- HTML5
- SQLite

## 🔍 Próximas Mejoras

- [ ] Autenticación de usuarios
- [ ] Filtrado y búsqueda de tareas
- [ ] Notificaciones de tareas próximas a vencer
- [ ] Integración con calendarios

## 📞 Contacto

Tu Nombre - [Tu Email]

Link del Proyecto: https://github.com/TuUsuario/gestor-tareas-django

## Capturas de Pantalla

### Vista Principal
![Vista Principal](screenshot_main.png)

### Edición de Tarea
![Edición de Tarea](screenshot_edit.png)

---

**Nota**: Reemplaza los marcadores de posición (Tu Usuario, Tu Email, etc.) con tu información real.