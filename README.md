# Manual de instalación de la aplicación web



## Decisiones de proyecto

|Elemento|Decisión·|Versión|Justificación|
|--------|-------|--------|-------------|
|Servidor web|Apache|2|Facidilidad de uso, popular|
|Base de datos|MySQL|8|Experiencia previa, popular|
|Lenguaje servidor|Python|3|Muy interesante para ASIR, uso extendido|
|Framework|Flask|3|Facilidad de uso, pensado especificamente para web, formularios y sesiones|
|Control de versiones|Git|8|Muy extendido|
|Documentación|Markdown|-|Muy utilizado con guthub|

## Proceso de instalación / puesta en marcha

1. Actualización del sistema
`sudo apt update && sudo apt upgrade -y`
2. Instalar git
`sudo apt install git`
3. Instalar VSCode + plugins
    - Markdown all in one

4. Instalar apache
'sudo apt install apache2'

5. Cambiar permisos de la carpeta /var/www/html
```bash
sudo chown -R $USER:$USER /var/www/html
sudo chmod -R u=rwX,go=rx /var/www/html
```

6. Instalamos mysql
```bash
sudo apt install mysql-server
```

7. Configuracion mysql
``` mysql
create database registros;
create user 'narrador'@'localhost' identified by 'resultados';
grant all privileges on registros.* to 'narrador'@'localhost';
flush privileges;
```

8. Creamos tablas y añadimos datos
```mysql
create table registro( id int auto_increment primary key, resultado varchar(30), desarrollo text, mvp varchar(20), rondas varchar(30) );
insert into registro (ganador, desarrollo, mvp, rondas) values ('LIQUID', 'Empieza ganando LIQUID y remonta G2', 'Aspas', '13-10');
```

## Configuración de github

1. ,Instalar, crear repositorio local
 ```bash
sudo apt install git
git init
```

2. Añadir archivos y commit(siempre que iniciamos)
```
git add .
git commit -n "comentario"
```

3. Crear cuenta github, crear repositorio github 

4. Conectar repositorio local en remoto
```bash
git remote add origin https://github.com/Albertocasts/Prediccion-Mundial-Valorant.git
git branch -M main
git push -u origin main
```

## Python

1. Instalar python
``` bash
sudo apt install python3-pip python3-venv -y
```
2. Conectamos y activamos el entorno virtual
``` bash
python3 -m venv venv
source venv/bin/activate
```
3. Instalar flask, conector de base de datos, comporbar y guardar las dependencias
``` bash
pip install flask
pip install mysql-connector-python
pip list
pip freeze > requirement.txt
```

4. Creamos un fichero app.py en la carpeta principal del proyecto
```bash
python3 app.py
```

```
5. Comprobamos abriendo http://localhost:5000/
```

## Migración del formulario a Python/Flask

1. Creamos una carpeta templates y movemos ahi el index.html
2. Modificamos app.py
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

```

3. Comprobamos abriendo http://localhost:5000/ . El formulario lo devuelve flask

## Recibir los datos del formulario

1. Vamos a app.py y modificamos la primera línea añadiendo request:
```python
from flask import Flask, render_template, request
```
2. Añadimos una ruta en app.py para recibir los datos del formulario:
```python


@app.route("/resultados", methods=["POST"])
def crear_incidencia():
    ganador = request.form["Ganador"]
    desarrollo = request.form["desarrollo"]
    mvp = request.form["mvp"]
    rondas = request.form["rondas"]

    conexion = mysql.connector.connect(
        host="localhost",
        user="narrador",
        password="resultados",
        database="resultados"
    )

    cursor = conexion.cursor()
    sql = """
        INSERT INTO registro 
        (ganador, desarrollo, mvp, rondas) 
        VALUES (%s, %s, %s, %s)
    """
    valores = (ganador, desarrollo, mvp, rondas)
    
    cursor.execute(sql, valores)
    conexion.commit()
    
    cursor.close()
    conexion.close()

'''

## Comprobamos todo
```
1. Comprobamos que todo se envia bien mirando nuestra base de datos y github