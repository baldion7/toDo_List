# Gestor de Tareas - Django

## 📋 Descripción del Proyecto

Un sistema completo de gestión de tareas desarrollado con Django que permite a los usuarios crear, editar, eliminar y
administrar sus tareas con diferentes estados.

![image](https://github.com/user-attachments/assets/6c54ef93-47e8-4435-937f-3e0aff57ca55)


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
git clone https://github.com/baldion7/toDo_List.git
cd toDo_List
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

- **Página Principal**: `http://localhost:8000/taskes/` `https://to-do-list-plzj.vercel.app/taskes/`
- **Panel de Administración**: `http://localhost:8000/admin/` `https://to-do-list-plzj.vercel.app/admin/`

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

- Python 3.12.8
- Django 2.3.3
- Bootstrap 5
- HTML 5
- asgiref 3.8.1
- certifi 2024.8.30
- charset-normalizer 3.4.0
- coreapi 2.3.3
- coreschema 0.0.4
- Django 5.1.4
- django-cors-headers 4.6.0
- djangorestframework 3.15.2
- idna 3.10
- itypes 1.2.0
- Jinja2 3.1.4
- MarkupSafe 3.0.2
- mysqlclient 2.2.6
- pip 24.3.1
- requests 2.32.3
- setuptools 75.6.0
- sqlparse 0.5.3
- tzdata 2024.2
- uritemplate 4.1.1
- urllib3 2.2.3

## 🔍 Próximas Mejoras

- [ ] Autenticación de usuarios
- [ ] Filtrado y búsqueda de tareas
- [ ] Notificaciones de tareas próximas a vencer
- [ ] Integración con calendarios

## 📞 Contacto

- [Kevin Jose Quiñones Baldion](https://github.com/baldion7) - [baldionkevin8@gmail.com](mailto:baldionkevin8@gmail.com)

Link del Proyecto: https://github.com/baldion7/toDo_List

## Capturas de Pantalla

### Vista Principal

![image](https://github.com/user-attachments/assets/db09b8e4-db47-4981-a393-f71e97fa8dd9)

### Edición de Tarea

![image](https://github.com/user-attachments/assets/d2bf7878-93cd-4616-8cc6-22e83b261a8a)

### Resultados de sonarqube

![image](https://github.com/user-attachments/assets/d87fab0c-d2aa-4d8d-ada1-129c638f744f)


---

