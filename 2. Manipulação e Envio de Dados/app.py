from flask import Flask, render_template, request

app = Flask(__name__)

# 127.0.0.1:5000/
@app.route('/')
def principal():
    return render_template("index.html")

frutas_favoritas = []

@app.route('/frutas', methods=["GET", "POST"])
def frutas():
    fruta1 = 'Mamão'
    fruta2 = 'Morango'
    fruta3 = 'Uva'
    fruta4 = 'Laranja'
    fruta5 = 'Maçã'
    frutas_exoticas = ["Durian", "Mangostim", "Rambutã", "Carambola", "Pitaya"]

    if request.method == "POST":
        if request.form.get("fruta"):
            frutas_favoritas.append(request.form.get("fruta"))

    return render_template("frutas.html", fruta1=fruta1, fruta2=fruta2, fruta3=fruta3, fruta4=fruta4, fruta5=fruta5, frutas_exoticas=frutas_exoticas, frutas_favoritas=frutas_favoritas)

diario_professor = []

@app.route('/notas', methods=["GET", "POST"])
def notas():
    notas = {"Italo": 10.0, "Giovanna":9.5, "Fernandes":5.7, "Martins": 0.3}

    if request.method == 'POST':
        if request.form.get("aluno") and request.form.get("nota"):
            diario_professor.append({"aluno": request.form.get('aluno'), "nota": request.form.get('nota')})

    return render_template("notas.html", notas=notas, diario_professor=diario_professor)

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")
