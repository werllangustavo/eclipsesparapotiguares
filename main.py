from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/conceitos')
def conceitos():
  return render_template('conceitos.html')

@app.route('/eclipsesregistrados')
def eclipsesregistrados():
  return render_template('eclipsesregistrados.html')

@app.route('/esp26fev2017')
def esp26fev2017():
  return render_template('esp26022017.html')

@app.route('/esp21ago2017')
def esp21ago2017():
  return render_template('esp21082017.html')

@app.route('/elt21jan2019')
def elt21jan2019():
  return render_template('elt21012019.html')

@app.route('/elp19nov2021')
def elp19nov2021():
  return render_template('elp19112021.html')

@app.route('/elt16mai2022')
def elt16mai2022():
  return render_template('elt16052022.html')

@app.route('/avisoimportante')
def avisoimportante():
  return render_template('avisos.html')

@app.route('/avaliacoes', defaults={"estrelas": "0"})
@app.route('/avaliacoes/<estrelas>')
def avaliacoes(estrelas):
  return render_template('avaliacoes.html', estrelas=estrelas)
  
app.run(host='0.0.0.0', port=81)
