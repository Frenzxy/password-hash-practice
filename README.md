# Password Hash Practice

## English

Password Hash Practice is a small Flask application for practicing user registration and authentication with PostgreSQL and bcrypt password hashing.

### Features

- User registration with username, email, and password validation.
- Password hashing with bcrypt before storage.
- Login authentication against PostgreSQL.
- Environment-based database configuration.
- Simple HTML templates for registration and login.

### Requirements

- Python 3.10 or newer
- PostgreSQL
- Python packages: `Flask`, `bcrypt`, and `psycopg`

Install the dependencies with:

```bash
python -m pip install Flask bcrypt psycopg[binary]
```

### Configuration

Create a local `.env` file with your PostgreSQL settings. Never commit this file or share its values:

```env
POSTGRES_DB=backend_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-local-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
```

The application reads these variables from the process environment. Load them with your preferred environment manager before starting the application.

### Run

```bash
python base_register.py
```

The application initializes the `user_data` table when it starts. Open the local address shown by Flask in your browser to register a user and test the login flow.

### Security note

This is an educational project. Passwords are hashed with bcrypt, but the application still needs production hardening before deployment, including CSRF protection, session management, rate limiting, secure cookie settings, and stricter database error handling.

## Español

Password Hash Practice es una aplicación pequeña de Flask para practicar el registro y la autenticación de usuarios usando PostgreSQL y el hash de contraseñas con bcrypt.

### Funcionalidades

- Registro de usuarios con validación de nombre de usuario, correo y contraseña.
- Hash de contraseñas con bcrypt antes de guardarlas.
- Autenticación mediante PostgreSQL.
- Configuración de la base de datos mediante variables de entorno.
- Plantillas HTML simples para registro e inicio de sesión.

### Requisitos

- Python 3.10 o superior
- PostgreSQL
- Paquetes de Python: `Flask`, `bcrypt` y `psycopg`

Instalá las dependencias con:

```bash
python -m pip install Flask bcrypt psycopg[binary]
```

### Configuración

Creá un archivo `.env` local con la configuración de PostgreSQL. Nunca subas este archivo ni compartas sus valores:

```env
POSTGRES_DB=backend_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=tu-contraseña-local
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
```

La aplicación lee estas variables desde el entorno del proceso. Cargalas con el gestor de variables de entorno que prefieras antes de iniciar la aplicación.

### Ejecución

```bash
python base_register.py
```

La aplicación crea la tabla `user_data` al iniciarse. Abrí en el navegador la dirección local que muestre Flask para registrar un usuario y probar el inicio de sesión.

### Nota de seguridad

Este es un proyecto educativo. Las contraseñas se protegen con bcrypt, pero antes de usar la aplicación en producción habría que agregar protección CSRF, gestión de sesiones, limitación de intentos, cookies seguras y un manejo más estricto de los errores de la base de datos.
