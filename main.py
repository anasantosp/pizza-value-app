#programa para calcular el ratio diametro-precio optimo
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "pizza calculation app"
 
if __name__ == "__main__":
    app.run()

