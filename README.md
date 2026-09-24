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