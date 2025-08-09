from flask import Flask, render_template

app = Flask(__name__)

# Construir las rutas
@app.route('/')
def inicio():
    # return '<h1>Bienvenido</h1>'
    return render_template('index.html')

# levantar el servidor
if __name__ == '__main__':
    app.run(debug=True)

    
