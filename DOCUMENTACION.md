# Documentación del Proyecto de Preprocesamiento de Datos

## Introducción

Este proyecto tiene como objetivo implementar técnicas de preprocesamiento de datos para análisis de ciencia de datos. Las principales funcionalidades implementadas incluyen:

- Limpieza de datos faltantes
- Normalización de datos
- Codificación de variables categóricas
- Detección y tratamiento de valores atípicos

## Comandos Git Utilizados

| Comando | Descripción | Propósito |
|---------|-------------|-----------|
| `git clone <url>`  | Clonar repositorio remoto Inicializa repositorio | Obtener una copia local del repositorio |
| `git config --global user.name` | Configurar nombre de usuario | Identificar al autor de los commits |
| `git config --global user.email` | Configuraar email |Asociar email a los comits|
| `git checkout -b feature-preprocesamiento` | Crea rama y cambia a nueva rama | Desarrollar funcionalidad específica |
| `git add preprocesamiento.py` |Añade archivo especifico  | Preparar archivos para commit|
| `git commit -m "mensaje"` | Confirma cambios  | Guardar cambios con descripcion |
| `git push origin feature-preprocesamiento` | Sube rama a remoto |  Compartir cambios en GitHub| 

## Automatización con GitHub Actions

Se implementó un workflow de CI/CD que realiza:

1. **Verificación de código**:
    - Ejecuta tests automáticos
    - Valida formato del código
    - Comprueba dependencias

2. **Despliegue**:
    - Se activa en push a main
    - Construye el proyecto
    - Ejecuta pruebas de integración
    - Genera documentación

El archivo de workflow está en `.github/workflows/ci.yml`

## Evidencias

### Comandos Ejecutados

![alt text](<docs/Imagen de WhatsApp 2025-11-09 a las 11.40.49_e153ee52.jpg>)
![alt text](<docs/Imagen de WhatsApp 2025-11-09 a las 11.43.19_9048e1bd.jpg>)
![alt text](<docs/Imagen de WhatsApp 2025-11-09 a las 15.13.40_ebd8e985.jpg>)
![alt text](<docs/Imagen de WhatsApp 2025-11-09 a las 15.14.07_e392a499.jpg>)


### Pull Requests y Fusión

![alt text](<docs/Imagen de WhatsApp 2025-11-09 a las 15.14.46_68544420.jpg>)
![alt text](<docs/Imagen de WhatsApp 2025-11-09 a las 15.17.19_6c600062.jpg>)
![alt text](<docs/Imagen de WhatsApp 2025-11-09 a las 15.18.51_2022c5e0.jpg>)

### GitHub Actions

![alt text](<docs/Imagen de WhatsApp 2025-11-09 a las 16.34.52_5d3eb9a4.jpg>)


---
**Enlace de repositorio**: [https://github.com/alissonatupana18/preprocesamiento-cienciadatos.git](https://github.com/alissonatupana18/preprocesamiento-cienciadatos.git)