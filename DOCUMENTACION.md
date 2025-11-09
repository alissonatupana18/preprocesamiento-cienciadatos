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
[Aquí debes insertar capturas de pantalla de los comandos git ejecutados en terminal]

### Pull Requests y Fusión
[Insertar capturas de los pull requests creados y sus fusiones en GitHub]

### GitHub Actions
[Incluir capturas de las ejecuciones exitosas de los workflows]

---
**Nota**: Las capturas de pantalla deben ser añadidas en la carpeta `/docs/images` y referenciadas aquí usando sintaxis markdown:
```markdown
![Descripción de la imagen](/docs/images/nombre-imagen.png)
```