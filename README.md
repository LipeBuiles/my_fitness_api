# my_fitness_app

my_fitness_api/
├── .env                # Variables sensibles (DB_URL, etc.)
├── core/               # El "motor" del proyecto
│   ├── config.py       # Configuración con Pydantic Settings
│   └── database.py     # Conexión y sesión de SQLAlchemy
├── models/             # Mapeo de tablas existentes
│   └── item.py         # Modelo de la tabla 'items'
├── crud/               # Lógica de acceso a datos
│   └── item.py         # Consultas SQL encapsuladas
├── src/                # Aplicación principal
│   └── main.py         # Endpoints y arranque de FastAPI
└── requirements.txt    # Dependencias del sistema