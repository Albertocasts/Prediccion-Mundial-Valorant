from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

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

    return "<h1>Prediccion recibida</h1><ul><li>Ganador : " + ganador +  "</li><li>Desarrollo : " + desarrollo + "</li><li>MVP : " + mvp + "</li><li>Rondas : " + rondas + "</li></ul>"

if __name__ == "__main__":
    app.run(debug=True)