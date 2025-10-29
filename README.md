# Validación del modelo en el lenguaje de programacion
Como ultimo punto del trabajo voy a crear el diseño arquitectonico junto con el patron de diseño singleton , donde la estructura del proyecto sera la siguiente:  
- View(Capa de presentacion) 
- Controller(Coordina operaciones)  
- Service(Reglas de negocio)  
- Model(Entidades)  
- Repository(acceso a datos)  
- Base de datos  

>[!IMPORTANT]
>Para ver los puntos pedidos en la consigna del tp ir al readme de documentos
>documentos/README.md  



### Autor : Ogas Augusto



## Ejecución rápida (CLI de ejemplo)

Para probar el flujo básico (alta de socios/libros, reservar y devolver) ejecutá:

```bash
python -m src.view.view
```

Estructura de capas implementada:

- View: `src/view/view.py` (CLI simple)
- Controller: `src/controller/*.py`
- Service: `src/service/*.py`
- Model: `src/model/*.py`
- Repository (Singleton in-memory): `src/repository/*.py`
