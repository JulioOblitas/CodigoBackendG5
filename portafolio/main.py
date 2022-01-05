from flask import Flask, render_template


app = Flask (__name__)

@app.route('/')
def index():
#datos en un diccionario
    skill = [
        {
         "curso" : "PYTHON",
          "imagen" : "img/python.png",
          "descripcion" : "Intermedio, Avanzado",
        },
        {
         "curso" : "FLASK",
          "imagen" : "img/python.png",
          "descripcion" : "Avanzado",
        },
        {
         "curso" : "DJANGO",
          "imagen" : "img/python.png",
          "descripcion" : "Avanzado",
        },
        {
         "curso" : "HTML 5",
          "imagen" : "img/python.png",
          "descripcion" : " Avanzado",
        },

    ]   

    return render_template('home.html',skills = skills)

app.run(debug = True)