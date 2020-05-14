# read_gtfs
Módulo de lectura de un archivo GTFS.zip. 

## Requisitos

- Python3
- Dependencias (mirar archivo `requirements.txt`)

## Instalación 

Clonar repositorio de Github:

```
git clone https://github.com/Epilef-coder/read_GTFS.git
```
Cambiar el directorio de trabajo:

```
cd read_GTFS
```

### Dependencias y entorno virtual (puede omitir este paso si cumple los requisitos)

Se recomienda la utilización de un entorno virtual, si no tiene instalado ```virtualenv``` puede instalarlo con los siguientes comandos:

```pip install virtualenv```, ```pip3 install virtualenv``` o ```pip3 install virtualenv --user```


Luego el entorno virtual puede ser creado dentro de la misma carpeta.

```
virtualenv venv
```

En caso de tener python 2.7 por defecto es necesario definir que sea python3 para el entorno virtual

```
virtualenv -p python3 venv
```

Luego se debe activar el entorno virtual e instalar las dependencias.
 
```
# activar
source venv/bin/activate
 
# instalar dependencias
pip install -r requirements.txt
```

## Ejecución

Para su uso debe importar la clase e inicializarla con la ruta de la ubicación del archivo GTFS en su ordenador

```
#importamos clase
from read_GTFS import read_GTFS
#creamos clase lectura gtfs
read = read_GTFS(r"path\to\GTFS.zip")
```

El método ```read_gtfs_with_df``` le permitirá obtener un diccionario donde la ```Key``` corresponde al nombre del 
archivo que desea consultar (e.g: ```"stops.txt"```) y el ```Key Value``` a un dataframe del contenido del archivo. 
A continuación un ejemplo:

```
#importamos clase
from read_GTFS import read_GTFS
#creamos clase lectura gtfs
read = read_GTFS(r"path\to\GTFS.zip")
#generamos dataframes de todos los archivos del GTFS.zip
df_gtfs = read.read_gtfs_with_df()
#consultamos por un dataframe en particular "stops.txt"
df_stops = df_gtfs["stops.txt"]
print(df_stops)
#consultamos por una columna en particular "stop_id" del dataframe del archivo "stops.txt"
stops_id = df_stops["stop_id"]
print(stops_id)
```
