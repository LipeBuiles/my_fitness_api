# 🏃‍♂️ My Fitness API

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.8+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**Una API REST completa para el seguimiento y análisis de datos de fitness y entrenamiento deportivo**

[Características](#-características) •
[Instalación](#-instalación) •
[Uso](#-uso) •
[API Endpoints](#-api-endpoints) •
[Estructura](#-estructura-del-proyecto)

</div>

---

## 📋 Descripción

My Fitness API es una solución backend robusta diseñada para aplicaciones de fitness y entrenamiento deportivo. Proporciona endpoints para gestionar usuarios, entrenamientos, métricas de salud, análisis de rendimiento y objetivos personalizados.

### ✨ Características

- 🔐 **Gestión de Usuarios** - Registro, autenticación y perfiles de usuario
- 🏃 **Seguimiento de Entrenamientos** - Registro completo de sesiones de entrenamiento
- ❤️ **Monitoreo de Salud** - Seguimiento de métricas vitales y ritmo cardíaco
- 📊 **Análisis de Rendimiento** - Métricas detalladas de cadencia, ritmo y zancada
- 😴 **Tracking de Sueño** - Registro y análisis de patrones de descanso
- 🎯 **Objetivos Diarios** - Gestión de metas y seguimiento de progreso
- 🏋️ **Tipos de Entrenamiento** - Clasificación personalizada de actividades
- 🔄 **API RESTful** - Arquitectura limpia siguiendo mejores prácticas

## 🚀 Tecnologías

- **Framework:** FastAPI
- **ORM:** SQLAlchemy 2.0
- **Base de Datos:** MySQL (PyMySQL)
- **Validación:** Pydantic v2
- **Servidor:** Uvicorn
- **Autenticación:** bcrypt
- **Configuración:** python-dotenv

## 📦 Instalación

### Prerequisitos

- Python 3.8+
- MySQL 5.7+ o MariaDB
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/my_fitness_api.git
cd my_fitness_api
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

Crear archivo `.env` en la raíz del proyecto:
```env
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/fitness_db
```

5. **Ejecutar migraciones de base de datos**
```bash
# Asegúrate de que tu base de datos existe
# Las tablas se crearán automáticamente al iniciar la aplicación
```

## 🎯 Uso

### Iniciar el servidor

```bash
cd src
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`

### Documentación interactiva

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 📡 API Endpoints

### Usuarios
- `GET /users/` - Listar todos los usuarios
- `GET /users/{user_id}` - Obtener usuario específico
- `POST /users/` - Crear nuevo usuario
- `PUT /users/{user_id}` - Actualizar usuario
- `DELETE /users/{user_id}` - Eliminar usuario

### Entrenamiento
- `GET /training/` - Listar entrenamientos
- `POST /training/` - Registrar entrenamiento
- `PUT /training/{training_id}` - Actualizar entrenamiento
- `DELETE /training/{training_id}` - Eliminar entrenamiento

### Salud
- `GET /health/` - Obtener métricas de salud
- `POST /health/` - Registrar datos de salud
- `PUT /health/{health_id}` - Actualizar registro
- `DELETE /health/{health_id}` - Eliminar registro

### Métricas de Rendimiento
- **Ritmo Cardíaco:** `/heart_rate/`
- **Cadencia:** `/cadence/`
- **Ritmo:** `/pace/`
- **Ritmo por KM:** `/pace_for_km/`
- **Longitud de Zancada:** `/stride_cm/`

### Otros
- **Seguimiento de Sueño:** `/dream/`
- **Objetivos Diarios:** `/objetives_day/`
- **Tipos de Entrenamiento:** `/type_training/`

## 🏗️ Estructura del Proyecto

```
my_fitness_api/
├── 📄 README.md              # Documentación del proyecto
├── 📄 requirements.txt       # Dependencias de Python
├── 📄 .env                   # Variables de entorno (no incluir en git)
│
├── 📁 core/                  # Módulos centrales
│   ├── config.py            # Configuración con Pydantic Settings
│   └── database.py          # Conexión y sesión de SQLAlchemy
│
├── 📁 models/                # Modelos de base de datos (SQLAlchemy)
│   ├── users.py
│   ├── training.py
│   ├── health.py
│   ├── heart_rate.py
│   ├── cadence.py
│   ├── pace.py
│   ├── pace_for_km.py
│   ├── stride_cm.py
│   ├── dream.py
│   ├── objetives_day.py
│   └── type_training.py
│
├── 📁 crud/                  # Lógica de acceso a datos
│   ├── users.py
│   ├── training.py
│   ├── health.py
│   ├── heart_rate.py
│   ├── cadence.py
│   ├── pace.py
│   ├── pace_for_km.py
│   ├── stride_cm.py
│   ├── dream.py
│   ├── objetives_day.py
│   └── type_training.py
│
└── 📁 src/                   # Aplicación principal
    ├── main.py              # Punto de entrada de FastAPI
    │
    ├── 📁 api/              # Routers de endpoints
    │   ├── users.py
    │   ├── training.py
    │   ├── health.py
    │   ├── heart_rate.py
    │   ├── cadence.py
    │   ├── pace.py
    │   ├── pace_for_km.py
    │   ├── stride_cm.py
    │   ├── dream.py
    │   ├── objetives_day.py
    │   └── type_training.py
    │
    └── 📁 shemas/           # Schemas de Pydantic
        ├── users.py
        └── health.py
```

## 🏛️ Arquitectura

El proyecto sigue una arquitectura en capas limpia y escalable:

```
┌─────────────────────────────────────┐
│      API Layer (FastAPI)            │
│   (Routers en src/api/)             │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Business Logic (CRUD)            │
│   (Operaciones en crud/)            │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Data Layer (SQLAlchemy)          │
│   (Modelos en models/)              │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│         Database (MySQL)            │
└─────────────────────────────────────┘
```

## 🔧 Configuración Avanzada

### Variables de Entorno

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `DATABASE_URL` | URL de conexión a la base de datos | `mysql+pymysql://user:pass@localhost:3306/db` |

### Personalización

Puedes personalizar el comportamiento de la API modificando [core/config.py](core/config.py)

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: nueva característica'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Convenciones de Código

- Seguir PEP 8 para estilo de código Python
- Usar type hints en todas las funciones
- Documentar funciones complejas con docstrings
- Mantener los modelos, CRUD y routers separados

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Juan Felipe Builes**

- GitHub: [@LipeBuiles](https://github.com/LipeBuiles)

## 🙏 Agradecimientos

- FastAPI por el excelente framework
- La comunidad de Python por las herramientas
- Todos los contribuidores del proyecto

---

<div align="center">

**⭐ Si este proyecto te ha sido útil, considera darle una estrella ⭐**

Hecho con ❤️ y ☕

</div>