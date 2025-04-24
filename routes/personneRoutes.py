from flask import Blueprint, render_template, request, redirect, url_for
from views.personneView import ajouter_nouvelle_personne

personne_bp = Blueprint('personne', __name__)

@personne_bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter_personne():
    if request.method == 'POST':
        mail = request.form['mail']
        nom = request.form['nom']
        prenom = request.form['prenom']
        date_naissance_str = request.form['date_naissance']
        sexe = request.form['sexe']

        success, message, nom_personne = ajouter_nouvelle_personne(mail, nom, prenom, date_naissance_str, sexe)

        if success:
            return redirect(url_for('personne.succes', nom=nom_personne, prenom=prenom))
        else:
            return render_template('ajouter_personne.html', error=message)

    return render_template('ajouter_personne.html')

@personne_bp.route('/succes/<nom>/<prenom>')
def succes(nom, prenom):
    return render_template('succes.html', nom=nom, prenom=prenom)