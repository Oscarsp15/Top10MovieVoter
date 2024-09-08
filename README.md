# Movie Voting System

## Descripción

El **Movie Voting System** es una aplicación web que permite a los usuarios buscar películas y votar por sus favoritas. Las películas se ordenan en un ranking de Top 10 basado en el número de votos recibidos. A medida que los usuarios emiten sus votos, la lista de las 10 películas más populares se actualiza dinámicamente.

## Funcionalidades

- **Búsqueda de Películas:** Busca películas por título utilizando una API externa (The Movie Database).
- **Sistema de Votación:** Los usuarios pueden votar por sus películas favoritas.
- **Ranking Dinámico:** Las películas se ordenan en función del número de votos, generando una lista de Top 10 que se actualiza en tiempo real.
- **Visualización del Top 10:** Muestra las 10 películas más votadas con detalles como el título, la portada, la fecha de lanzamiento y el promedio de votos.

## Instalación

### Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Clonación del Repositorio

```bash
git clone https://github.com/tu_usuario/Top10MovieVoter.git
cd Top10MovieVoter
pip install -r requirements.txt
```
## Configuración

1. **Crea un archivo `.env` en el directorio raíz del proyecto y añade tus credenciales de API:**

    ```ini
    API_KEY=tu_clave_de_api
    ```

2. **Asegúrate de que el archivo `votes.json` tenga los permisos adecuados.**

## Uso

1. **Ejecuta la aplicación:**

    ```bash
    python app.py
    ```

2. **Abre tu navegador y visita `http://127.0.0.1:5000` para acceder a la aplicación.**

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación.
- `templates/`: Carpeta que contiene las plantillas HTML.
- `static/`: Carpeta para archivos estáticos como CSS y JavaScript.
- `votes.json`: Archivo para almacenar los votos de las películas.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos para contribuir al proyecto:

1. Haz un fork del repositorio.
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commits (`git commit -am 'Añadir nueva característica'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-caracteristica`).
5. Crea una solicitud de extracción (pull request).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
