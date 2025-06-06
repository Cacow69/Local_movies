from flask import Flask, render_template, url_for
import os

# Caminho absoluto da pasta "src"
src_path = os.path.join(os.path.dirname(__file__), "src")

# Criação da aplicação Flask com os caminhos personalizados
app = Flask(__name__, template_folder=os.path.join(src_path, "templates"), static_folder=os.path.join(src_path, "static"))


# Rotas
@app.route("/")
def index():
    return render_template("index.html")









if __name__ == '__main__':
    app.run(debug=True)
