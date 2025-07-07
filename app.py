from flask import Flask, render_template, url_for, send_from_directory, request
import os
from datetime import datetime
from tkinter import Tk, filedialog
import pyfiglet
from rich import print
import socket

#Palavra legal no terminal
titulo = pyfiglet.figlet_format("LOCAL MOVIES")

# Caminho absoluto da pasta "src"
src_path = os.path.join(os.path.dirname(__file__), "src")

# Caminho absoluto para a pasta dos vídeos
PASTA_VIDEOS = r'C:\FILMES'


# Criação da aplicação Flask com os caminhos personalizados
app = Flask(__name__, template_folder=os.path.join(src_path, "templates"), static_folder=os.path.join(src_path, "static"))

# Função para converter .srt para .vtt com tratamento de codificação
def converter_srt_para_vtt(srt_path, vtt_path):
    encodings_possiveis = ['utf-8', 'latin-1', 'windows-1252']

    for encoding in encodings_possiveis:
        try:
            with open(srt_path, 'r', encoding=encoding) as srt_file, open(vtt_path, 'w', encoding='utf-8') as vtt_file:
                vtt_file.write("WEBVTT\n\n")
                for line in srt_file:
                    vtt_file.write(line.replace(',', '.'))
            return True
        except UnicodeDecodeError:
            continue
    print(f"[ERRO] Não foi possível decodificar {srt_path}")
    return False


# Rotas
@app.route("/")
def index():
    now = datetime.now()
    day = now.strftime("%a")        
    time = now.strftime("%H:%M")    
    datetime_display = f"{day} {time}"
    return render_template("vw_index.html", datetime_display=datetime_display)


@app.route("/videos")
def videos():
    now = datetime.now()
    day = now.strftime("%a")        
    time = now.strftime("%H:%M")    
    datetime_display = f"{day} {time}"

    lista_videos = []
    arquivos = os.listdir(PASTA_VIDEOS)

    for filme in arquivos:
        if filme.endswith(('.mp4', '.webm', '.ogg', '.mkv')):
            nome_base = os.path.splitext(filme)[0]

            #Legendas 
            srt_filename = nome_base + '.srt'
            vtt_filename = nome_base + '.vtt'

            srt_path = os.path.join(PASTA_VIDEOS, srt_filename)
            vtt_path = os.path.join(PASTA_VIDEOS, vtt_filename)

            # Se .srt existe e .vtt ainda não, converter
            if os.path.exists(srt_path) and not os.path.exists(vtt_path):
                converter_srt_para_vtt(srt_path, vtt_path)

            tem_legenda = os.path.exists(vtt_path)

            lista_videos.append({
                'video': filme,
                'legenda': vtt_filename if tem_legenda else None
            })

    print("FILMES RECEBIDOS: ", lista_videos)

    return render_template("vw_videos.html", datetime_display=datetime_display, videos=lista_videos)


@app.route('/filmes/<path:filename>')
def serve_video(filename):
    return send_from_directory(PASTA_VIDEOS, filename)



if __name__ == '__main__':
     if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        print(f"[yellow]{titulo}[/yellow]")
        print("[purple]>>> Ambiente virtual ativado com sucesso.[/purple]")
     app.run(host='0.0.0.0', port=5000, debug=True)


