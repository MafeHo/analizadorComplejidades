# Analizador de Complejidad Algorítmica

Este proyecto ha sido reestructurado en dos componentes principales: Backend y Frontend.

## Estructura del Proyecto

- **backend/**: Contiene la lógica de análisis (Python), la API (FastAPI) y los tests.
- **frontend/**: Contiene la interfaz de usuario moderna (React + Vite).

## Instrucciones de Ejecución

### 1. Backend

El backend expone una API REST para analizar el código.

1. Navega a la carpeta `backend`:
   ```bash
   cd backend
   ```
2. Instala las dependencias (si no lo has hecho):
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el servidor:
   ```bash
   uvicorn app:app --reload --port 8000
   ```
   El servidor correrá en `http://localhost:8000`.

### 2. Frontend

El frontend es una aplicación web moderna.

1. Navega a la carpeta `frontend`:
   ```bash
   cd frontend
   ```
2. Instala las dependencias (si no lo has hecho):
   ```bash
   npm install
   ```
3. Ejecuta el servidor de desarrollo:
   ```bash
   npm run dev
   ```
   La aplicación estará disponible en la URL que muestre la terminal (usualmente `http://localhost:5173`).

## Funcionalidades

- **Editor de Código**: Editor con resaltado de sintaxis (Monaco Editor).
- **Análisis**: Ejecuta el análisis de complejidad del algoritmo.
- **Gráfica**: Visualización interactiva de la complejidad asintótica.
- **Resultados**: Resumen ejecutivo, logs detallados y prueba de escritorio.
- **Traducción**: Opción para traducir lenguaje natural a pseudocódigo (requiere configuración de LLM en backend).

## Notas

- Las visualizaciones de "Pila de Recursión" y "Árbol de Recursión" están pendientes de migración completa a la nueva interfaz web.
