from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Bienvenido a mi Api'

@app.route('/bienvenido')
def bienvenido():
    return 'Bienvenido a mi Api2'   


@app.route('/bienvenido_home')
def bienvenido_home():
    return 'Bienvenido a mi Home Adios'   


if __name__ == '__main__':
    app.run(debug=True, port = 3000 )

