<img src="src/static/img/logo.jpg" alt="logo">
<hr>

<br>
<br>

## **🤔 Sobre o projeto**
O sistema tem o objetivo de **Ler e Transmitir** arquivos de vídeo de um dispositivo "raiz" para outros que estiverem conectados à mesma rede! 
O Local Movies **NÃO FORNECE ARQUIVOS E MUITO MENOS PROMOVE A PIRATARIA**, é apenas uma solução prática para o consumo de arquivos próprios.

 **🎯 Principais objetivos**
- Facilitar a visualização de arquivos de vídeo. 
- Centralizar as informações em um sistema local.
- Disponibilizar arquivos para outros dispositivos através da rede.  


<br> 
<br>


## **💻 Linguagens utilizadas**

<br>

<p align="center">
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

<br>
<br>


## **🚀 Recursos**

Para garantir um sistema mais funcional e eficiente, o projeto está sendo desenvolvido utilizando as seguintes tecnologias:

- **[Visual Studio Code](https://code.visualstudio.com/)**: Editor de código leve e versátil, com suporte a extensões e múltiplas linguagens.
- **[GitHub](https://github.com/)**: Plataforma online para hospedagem e colaboração em projetos de código, usando controle de versão com Git.

<br>
<br>

## 🛠️ Instalação

Para rodar o **Local Movies** localmente, siga os passos abaixo:

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Cacow69/Local_movies.git
   cd Local_movies
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o sistema**
   ```bash
   python app.py ou abra o 'Local Movies.bat'
   ```

5. Acesse no navegador:
   ```
   http://localhost:5000
   ```

## 📢 Solução de problemas

O **Local Movies** pode apresentar problemas na hora de ser acessado por outros dispositivos,
siga os passos para a resolução:

1. Firewall:
```
Abra o Painel de Controle → Sistema e Segurança → Firewall do Windows Defender → Permitir um aplicativo pelo Firewall do Windows.
```
Selecione o executável do Python **"python.exe"** e clique em **Alterar configurações**.

2. IP de acesso:
```
Quando o servidor é rodado, aparecem dois IP's. para acessar de outro dispositivo, acesse o que começa com 192.168.x.x
```

3. Arquivo loader:
```
Caso queira usar o .bat em outro diretório, basta edita-lo com o bloco de notas e colar o caminho completo para o diretório raiz.
```



> ⚠️ Certifique-se de ter o **Python 3.10+** instalado em sua máquina.

<br>
<br>
