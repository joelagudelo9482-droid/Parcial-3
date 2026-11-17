# 1. Información del proyecto

| Información | Descripción |
|------------|-------------|
| Estudiante | Joel Agudelo |
| Asignatura | Desarrollo de Aplicaciones con Acceso a Datos |
| Docente | Eduardo Pimienta |
| Fecha | 17/11/2026 |
| Lenguaje de programación | Python |
| ORM utilizado | SQLAlchemy |
| Base de datos | SQLite |

---

# 2. Descripción del proyecto

Este proyecto consiste en implementar la persistencia de datos para una aplicación de consola que administra el inventario de una tienda de zapatos.

La persistencia fue desarrollada utilizando SQLAlchemy ORM y SQLite. El sistema permite registrar, consultar, actualizar y eliminar zapatos almacenados en la base de datos.

## Funcionalidades implementadas

- Registrar zapatos.
- Listar todos los zapatos.
- Buscar zapatos por ID.
- Actualizar precios.
- Eliminar zapatos.
- Persistencia de datos entre ejecuciones.

---

# 3. Estructura del proyecto

Presenta la estructura de archivos de la aplicación.

```text
tienda_zapatos/
├── main.py
├── datos.py
├── requirements.txt
├── README.md
├── zapateria.db
└── evidencias/
```

## Explicación de los archivos

| Archivo | ¿Cuál es su responsabilidad? |
|----------|----------------------------|
| main.py | Contiene el menú principal y la interacción con el usuario. |
| datos.py | Implementa el modelo ORM y las operaciones CRUD utilizando SQLAlchemy. |
| requirements.txt | Contiene las dependencias necesarias para ejecutar el proyecto. |
| README.md | Contiene la documentación técnica y las respuestas del parcial. |
| zapateria.db | Base de datos SQLite que almacena permanentemente los registros de zapatos. |
| evidencias/ | Carpeta donde se almacenan las capturas de pantalla de las pruebas realizadas. |

---

# 4. Instalación y ejecución

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
python main.py
```

---

# 5. Respuestas técnicas

## Pregunta 1

### ¿Qué clase de Python representa la tabla de la base de datos?

| Elemento | Explicación |
|-----------|-------------|
| Clase ORM | Zapato |
| Nombre de tabla | zapatos |
| Clave primaria | id |
| Otras columnas | modelo, talla y precio |

La clase que representa la tabla de la base de datos es:

```python
class Zapato(Base):
```

SQLAlchemy identifica el nombre de la tabla mediante:

```python
__tablename__ = "zapatos"
```

Las columnas son definidas con `Mapped` y `mapped_column()`. La columna `id` fue configurada como clave primaria autoincremental.

---

## Pregunta 2

### ¿Qué ocurre cuando ejecutas el programa por primera vez?

| Proceso | Resultado |
|----------|-----------|
| Se ejecuta `inicializar_bd()` | SQLAlchemy verifica las tablas |
| No existe `zapateria.db` | SQLite crea el archivo automáticamente |
| No existe la tabla `zapatos` | SQLAlchemy crea la tabla |

La creación se realiza mediante:

```python
Base.metadata.create_all(engine)
```

Cuando se ejecuta por primera vez, SQLite crea el archivo `zapateria.db` y SQLAlchemy genera automáticamente la tabla `zapatos`.

---

## Pregunta 3

### ¿Qué recorrido siguen los datos desde el menú hasta SQLite?

| Paso | Acción |
|--------|--------|
| 1 | El usuario selecciona Registrar zapato |
| 2 | El programa solicita modelo, talla y precio |
| 3 | Se ejecuta `crear_zapato()` |
| 4 | Se crea un objeto `Zapato` |
| 5 | Se agrega con `session.add()` |
| 6 | Se confirma con `session.commit()` |
| 7 | El registro queda almacenado en SQLite |

Fragmento utilizado:

```python
zapato = Zapato(
    modelo=modelo,
    talla=talla,
    precio=precio
)

session.add(zapato)
session.commit()
```

---

## Pregunta 4

### ¿Para qué se utiliza una sesión de SQLAlchemy?

| Concepto | Explicación |
|------------|------------|
| Session | Administra la comunicación con la base de datos |
| commit() | Guarda permanentemente los cambios |

La sesión se utiliza para realizar consultas, inserciones, modificaciones y eliminaciones.

Si se crea o modifica un objeto y no se ejecuta:

```python
session.commit()
```

los cambios no se guardan en la base de datos y se perderán al finalizar la sesión.

---

## Pregunta 5

### ¿Cómo funciona la búsqueda de zapatos por ID?

| Situación | Resultado |
|------------|-----------|
| El ID existe | Devuelve un objeto Zapato |
| El ID no existe | Devuelve None |

La búsqueda se realiza mediante:

```python
session.get(Zapato, id_zapato)
```

Cuando encuentra el registro devuelve el objeto correspondiente. Cuando el registro no existe devuelve `None`.

---

## Pregunta 6

### ¿Cómo se actualiza el precio de un zapato?

| Paso | Acción |
|--------|--------|
| 1 | Buscar el zapato por ID |
| 2 | Modificar el atributo precio |
| 3 | Ejecutar commit() |
| 4 | SQLAlchemy actualiza SQLite |

Código utilizado:

```python
zapato.precio = nuevo_precio
session.commit()
```

Si el ID no existe la función retorna `False`.

---

## Pregunta 7

### ¿Qué ocurre cuando eliminas un zapato?

| Paso | Acción |
|--------|--------|
| 1 | Buscar el objeto |
| 2 | Ejecutar delete() |
| 3 | Ejecutar commit() |
| 4 | Verificar que ya no existe |

Código utilizado:

```python
session.delete(zapato)
session.commit()
```

La verificación se realizó buscando nuevamente el mismo ID y consultando el listado completo de registros.

---

## Pregunta 8

### ¿Qué sucede cuando cierras y vuelves a ejecutar el programa?

| Situación | Resultado |
|------------|-----------|
| Cerrar programa | Los datos permanecen almacenados |
| Abrir nuevamente | Los registros siguen disponibles |

Los datos permanecen porque SQLite almacena la información en el archivo:

```text
zapateria.db
```

Durante las pruebas se comprobó que, al cerrar y volver a ejecutar el programa, los registros seguían disponibles.

---

# 6. Evidencias de funcionamiento

| Prueba | Evidencia |
|----------|-----------|
| Registrar dos zapatos | registro_zapatos.png |
| Consultar todos los zapatos | listado_zapatos.png |
| Buscar zapato por ID | busqueda_id.png |
| Actualizar precio | actualizar_precio.png |
| Eliminar zapato | eliminar_zapato.png |
| Persistencia de datos | persistencia.png |

---

# 7. Pruebas con registros inexistentes

| Operación | ¿Qué sucedió? |
|------------|---------------|
| Buscar ID inexistente | La función devolvió `None` y el programa mostró "Zapato no encontrado". |
| Actualizar ID inexistente | La función devolvió `False` y no se realizó ninguna modificación. |
| Eliminar ID inexistente | La función devolvió `False` y no se eliminó ningún registro. |

Estas pruebas demuestran que el programa maneja correctamente los casos en los que el identificador solicitado no existe en la base de datos.
