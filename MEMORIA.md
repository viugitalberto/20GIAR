# Memoria del Proyecto: Pipeline DataOps

**Autor:** viugitalberto  
**Asignatura:** Metodologías de Desarrollo y Despliegue de Aplicaciones para Ciencia de Datos  
**Fecha:** 29 de mayo de 2026

---

## 1. Resumen ejecutivo (Página 1)

Este proyecto consiste en la implementación de un pipeline DataOps que automatiza un proceso ETL (Extract, Transform, Load). El pipeline extrae datos de la API pública JSONPlaceholder, los transforma calculando la longitud de los títulos y filtrando aquellos con más de 50 caracteres, y finalmente los guarda en un archivo CSV.

**Tecnologías utilizadas:**
- Python 3.11
- GitHub Actions (CI/CD)
- Docker
- GitHub Projects (Kanban)

**Resultados clave:**
- Pipeline funcional que se ejecuta automáticamente
- CI/CD configurado con 4 ejecuciones exitosas
- Contenedor Docker para reproducibilidad

---

## 2. Arquitectura del sistema (Páginas 2-3)

### Diagrama de arquitectura


### Componentes

| Componente | Tecnología | Función |
|------------|------------|---------|
| Extract | Python + requests | Obtiene datos de API REST |
| Transform | Python + pandas | Limpia y filtra datos |
| Load | Python | Guarda CSV en disco |
| CI/CD | GitHub Actions | Ejecuta pipeline automáticamente |
| Contenedor | Docker | Asegura reproducibilidad |

### Flujo de datos

1. El script `src/etl.py` se ejecuta
2. `extract()` hace GET a `jsonplaceholder.typicode.com/posts`
3. `transform()` convierte a DataFrame y filtra títulos largos
4. `load()` guarda en `output/data.csv`

---

## 3. Decisiones técnicas (Páginas 4-5)

### ¿Por qué Python?
- Ecosistema maduro para ETL (pandas, requests)
- Fácil integración con GitHub Actions
- Amplia documentación

### ¿Por qué GitHub Actions?
- Integración nativa con GitHub
- Gratuito para repositorios públicos
- Sintaxis YAML simple

### ¿Por qué Docker?
- Asegura que el pipeline funcione en cualquier entorno
- Facilita el despliegue
- Buenas prácticas DevOps/DataOps

### ¿Por qué JSONPlaceholder?
- No requiere API key
- Datos estructurados listos para usar
- 100% disponible y gratuito

---

## 4. Metodología ágil (Páginas 6-7)

### Tablero Kanban

El proyecto se organizó usando GitHub Projects con un tablero Kanban con las siguientes columnas:

- **Sprint 1 (29 mayo)**: Tareas iniciales
- **Sprint 2 (29 mayo)**: CI/CD y pruebas
- **Sprint 3 (30 mayo)**: Docker y documentación
- **Done**: Tareas completadas

### Sprints documentados

| Sprint | Fecha | Tareas | Estado |
|--------|-------|--------|--------|
| Sprint 1 | 29/05 | Script ETL, tests | ✅ Completado |
| Sprint 2 | 29/05 | GitHub Actions, subir código | ✅ Completado |
| Sprint 3 | 30/05 | Dockerfile, memoria, vídeo | 🔄 En curso |

### User Stories

1. *"Como científico de datos, quiero un pipeline automático que extraiga datos para no hacerlo manualmente"*
2. *"Como desarrollador, quiero tests automáticos para detectar errores antes de desplegar"*
3. *"Como DevOps, quiero un contenedor Docker para ejecutar el pipeline en cualquier entorno"*

### Sprint Retrospective

**Lo que salió bien:**
- Configuración rápida del pipeline base
- GitHub Actions funcionó a la primera
- El script ETL es simple pero funcional

**Lo que se puede mejorar:**
- Implementar subida a AWS S3
- Añadir más tests para mayor cobertura
- Usar logging en lugar de prints

---

## 5. Implementación técnica (Páginas 8-9)

### Estructura del repositorio




### CI/CD Pipeline (GitHub Actions)

El workflow `ci.yml` se ejecuta automáticamente en cada push a la rama `main`.

**Pasos del pipeline:**
1. Checkout del código
2. Configuración de Python 3.11
3. Instalación de dependencias
4. Ejecución del script ETL

**Resultado:** 4 ejecuciones exitosas (verde ✅)

### Tests

Los tests verifican que:
- `extract()` devuelve datos (lista no vacía)
- `transform()` filtra correctamente títulos largos

**Cobertura estimada:** ~80% (funciones principales cubiertas)

### Docker

El Dockerfile permite ejecutar el pipeline en cualquier entorno:

```bash
docker build -t dataops-pipeline .
docker run --rm dataops-pipeline

Capturas de pantalla

<img width="1307" height="482" alt="image" src="https://github.com/user-attachments/assets/e00342f0-74be-493f-b2c0-b389b0d68062" />
<img width="1284" height="576" alt="image" src="https://github.com/user-attachments/assets/43d99348-9f04-4617-bbc1-8eec9596aa73" />


$ python src/etl.py
Iniciando pipeline...
Datos guardados en output/data.csv
Pipeline finalizado!

$ cat output/data.csv
userId,id,title,body,title_length
...
