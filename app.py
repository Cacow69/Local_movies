from flask import Flask, render_template, url_for
import os
from datetime import datetime

# Caminho absoluto da pasta "src"
src_path = os.path.join(os.path.dirname(__file__), "src")

# Criação da aplicação Flask com os caminhos personalizados
app = Flask(__name__, template_folder=os.path.join(src_path, "templates"), static_folder=os.path.join(src_path, "static"))


# Rotas
@app.route("/")
def index():
    now = datetime.now()
    day = now.strftime("%a")        
    time = now.strftime("%H:%M")    
    datetime_display = f"{day} {time}"
    return render_template("index.html", datetime_display=datetime_display)

@app.route("/videos")
def videos():
    now = datetime.now()
    day = now.strftime("%a")        
    time = now.strftime("%H:%M")    
    datetime_display = f"{day} {time}"
    return render_template("videos.html", datetime_display=datetime_display)








if __name__ == '__main__':
    app.run(debug=True)
