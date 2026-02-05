# libreria-cafe-edd-db

Librería para manejar una base de datos relacional SQLite entre todos los módulos del proyecto final de Estructuras de Datos de manera consistente.

## Instalación

```bash
pip install libreria-cafe-edd-db
```

## Descripción

Esta biblioteca ofrece una colección completa de modelos SQLAlchemy diseñados para facilitar la gestión de una librería-café. Incluye modelos para clientes, inventario de libros, consumo de café, membresías, facturación, proveedores y más.

## Inicio Rápido

```python
from datetime import date, timedelta
from libreria_cafe_edd_db import crear_sesion, establecer_logs, Membresia

# Habilitar o deshabilitar los logs de las queries de la base de datos
establecer_logs(True)

# Crear una sesión de base de datos
session = crear_sesion()

# Crear una nueva membresía
membresia = Membresia(
    fecha_inicio=date.today(),
    fecha_vencimiento=date.today() + timedelta(days=365),
    cantidad_libros=10,
    descuento_cafe=15,
    monto=50000,
    cantidad_cafe_gratis=5,
    tiempo_mesa=120
)

# Guardar en la base de datos
session.add(membresia)
session.commit()

# Cerrar la sesión una vez que hayas terminado
session.close()
```

## Modelos Disponibles

### Modelos Principales

- **Cliente**: Gestión de información de clientes
- **Libro**: Catálogo de libros disponibles
- **Membresia**: Planes de membresía para clientes
- **Venta**: Registro de transacciones de venta
- **Factura**: Generación y gestión de facturas

### Consumo

- **ConsumoCafe**: Registro de consumo de café
- **ConsumoLibro**: Registro de consumo/préstamo de libros

### Inventario y Proveedores

- **Proveedor**: Información de proveedores
- **OrdenReposicion**: Órdenes de reposición de inventario
- **DetallesReposicion**: Detalles de las órdenes de reposición

### Otros

- **RecomendacionLibro**: Sistema de recomendaciones de libros

### Enumeraciones

- **MetodoPago**: Métodos de pago disponibles
- **TipoVenta**: Tipos de venta (presencial, en línea, etc.)
