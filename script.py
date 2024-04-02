from flask import Flask, request, url_for, render_template, redirect
import sqlite3 as lite
import os

# ------------------
# application Flask
# ------------------

app = Flask(__name__)

def retour_index():
	return "<a href='" + url_for("index") + "'>retour à l'index</a><br/><br/>"
	
# renvoie un formulaire vers la page cible demandant un prénom (avec une valeur par défaut)
def formulaire_prenom(cible, prenom = "entrez votre prénom"):
	formulaire = ""
	formulaire += "<form method='post' action='" + url_for(cible) + "'>"
	formulaire += "<input type='text' name='prenom' value='" + prenom + "'>"
	formulaire += "<input type='submit' value='Envoyer'>"
	formulaire += "</form><br/>"
	
	return formulaire
	
# connecte à la BDD, affecte le mode dictionnaire aux résultats de requêtes et renvoie un curseur
def connection_bdd():
	
	con = lite.connect('exemples.db')
	con.row_factory = lite.Row
	
	return con
	
# connecte à la BDD et renvoie toutes les lignes de la table personne
def selection_personnes():
	
	conn = connection_bdd()
	cur = conn.cursor()
	
	cur.execute("SELECT nom, prenom, role FROM personnes")
	
	lignes = cur.fetchall()
	
	conn.close()
	
	return lignes
	
# connecte à la BDD et renvoie les lignes de la table personne dont le prénom commence par la lettre donnée
def selection_personnes_lettre(lettre):
	
	conn = connection_bdd()
	cur = conn.cursor()
	
	cur.execute("SELECT nom, prenom, role FROM personnes WHERE prenom LIKE ?", (lettre + "%",))
	
	lignes = cur.fetchall()
	
	conn.close()
	
	return lignes
	
# connecte à la BDD et insère une nouvelle ligne avec les valeurs données
def insertion_personne(nom, prenom, role):
	
	try:
		conn = connection_bdd()
		cur = conn.cursor()
		
		cur.execute("INSERT INTO personnes('nom', 'prenom', 'role') VALUES (?,?,?)", (nom,prenom,role))
		
		conn.commit()
		
		conn.close()
		
		return True
		
	except lite.Error:
		
		return False


############ Accueil ########################
@app.route('/')
def Accueil():
	return render_template('1index.html')


############ Client ########################
@app.route('/Client')
def Client():
	return render_template('1client.html')

############ Client/Nouvelle Commande ########################
@app.route('/Client/NouvelleCommande')
def NouvelleCommande():
	return render_template('1cmde.html')

############ Client/Nouvelle Commande/Chassis court fermé ########################
@app.route('/Client/NouvelleCommande/ccf', methods=['GET','POST'])
def NouvelleCommandeccf():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1foccf.html')

############ Client/Nouvelle Commande/Chassis court ouvert ########################
@app.route('/Client/NouvelleCommande/cco', methods=['GET','POST'])
def NouvelleCommandecco():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1focco.html')

############ Client/Nouvelle Commande/Chassis long fermé ########################
@app.route('/Client/NouvelleCommande/clf', methods=['GET','POST'])
def NouvelleCommandeclf():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1foclf.html')

############ Client/Nouvelle Commande/Chassis long ouvert ########################
@app.route('/Client/NouvelleCommande/clo', methods=['GET','POST'])
def NouvelleCommandeclo():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1foclo.html')

############ Client/Nouvelle Commande/repcl ########################
@app.route('/Client/NouvelleCommande/repcl', methods=['GET','POST'])
def NouvelleCommanderepcl():
	Nom = request.form['Nom']
	option = request.form['option']
	Chassis = 'ccf'
	# if request.method =='POST':  # appuyer sur le bouton pour commander
	message = f"Bonjour {Nom}, votre châssis {Chassis} avec l'option {option} a bien été commandé."
	#Insertion BDD
	#conn = connection_bdd()
	#cur = conn.cursor()
	#cur.execute("INSERT INTO personnes('nom', 'prenom', 'role') VALUES (?,?,?)", (nom,prenom,role))
	#conn.commit()
	#conn.close()
	return render_template('1repcl.html', message = message)

############ Client/Suivi Commande ########################
@app.route('/Client/SuiviCommande', methods=['GET','POST'])
def SuiviCommande():
	
# permet d'utiliser les noms de colonnes comme indices : ligne['Prenom']
	con = lite.connect(r"D:\AgiWeb\PRJ\Base_de_donnees_Serious_Game.db")
	con.row_factory = lite.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM Commandes")
	lignes=cur.fetchall()
	print(lignes)
	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1csuiv.html')

############ AgiLean ########################
@app.route('/AgiLean', methods=['GET','POST'])
def AgiLean():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1agilea.html')

############ AgiLean/Commande kits ########################
@app.route('/AgiLean/CommandeKit', methods=['GET','POST'])
def AgiLeanCommandeKit():
	
	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1cmdk.html')

############ AgiLean/Commande kits/reple ########################
@app.route('/AgiLean/CommandeKit/reple', methods=['POST'])
def AgiLeanreple():
	qk1 = request.form['qte1']
	qk2 = request.form['qte2']
	qk3 = request.form['qte3']
	message = f"Bonjour vous avez commandé {qk1} kit 1, {qk2} kit 2 et {qk3} kit 3 ."
	# if request.method =='POST':  # appuyer sur le bouton pour commander
	#conn = connection_bdd()
	#cur = conn.cursor()
	#cur.execute("INSERT INTO personnes('nom', 'prenom', 'role') VALUES (?,?,?)", (nom,prenom,role))
	#conn.commit()
	#conn.close()
	#Insertion BDD
	return render_template('1reple.html', message=message)

############ AgiLean/ Commande client ########################
@app.route('/AgiLean/CommandeClient', methods=['GET','POST'])
def AgiLeanCommandeClient():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1sclnt.html')

############ AgiLog ########################
@app.route('/AgiLog', methods=['GET','POST'])
def AgiLog():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1agilog.html')

############ AgiLog/Commande de pièces ########################
@app.route('/AgiLog/CommandePièce', methods=['POST'])
def AgiLogCommandePiece():
	qtea = request.form['qtea']
	qteb = request.form['qteb']
	qtec = request.form['qtec']
	qted = request.form['qted']
	qtee = request.form['qtee']
	qtef = request.form['qtef']
	qteg = request.form['qteg']
	qteh = request.form['qteh']
	qtei = request.form['qtei']
	qtej = request.form['qtej']
	qtek = request.form['qtek']
	qtel = request.form['qtel']
	qtem = request.form['qtem']
	qten = request.form['qten']
	qteo = request.form['qteo']
	qtep = request.form['qtep']
	qteq = request.form['qteq']
	qter = request.form['qter']
	qtes = request.form['qtes']
	qtet = request.form['qtet']
	qteu = request.form['qteu']
	qtev = request.form['qtev']
	qtew = request.form['qtew']
	qtex = request.form['qtex']
	qtey = request.form['qtey']
	qtez = request.form['qtez']
	qteaa = request.form['qteaa']
	qteab = request.form['qteab']
	message = f"{ qtea }, { qteb }, { qtec }, { qted }, { qtee }, { qtef }, { qteg }, { qteh }, { qtei }, { qtej }, { qtek }, { qtel }, { qtem }, { qten }, { qteo }, { qtep }, { qteq }, { qter }, { qtes }, { qtet }, { qteu }, { qtev }, { qtew }, { qtex }, {qtey }, { qtez }, { qteaa }, { qteab }"
	# if request.method =='POST':  # appuyer sur le bouton pour commander
	#conn = connection_bdd()
	#cur = conn.cursor()
	#cur.execute("INSERT INTO personnes('nom', 'prenom', 'role') VALUES (?,?,?)", (nom,prenom,role))
	#conn.commit()
	#conn.close()
	#insertion dans la base de données
	return render_template('1cmdp.html', message = message)

############ AgiLog/Commande de pièces/replo ########################
@app.route('/AgiLog/CommandePièce/replo', methods=['GET','POST'])
def AgiLogCommandePiecereplo():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1replo.html')

############ AgiLog/Affichage des stocks ########################
@app.route('/AgiLog/AffichageStock', methods=['GET','POST'])
def AgiLogAffStock():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1gests.html')
############ en savoir plus ########################
@app.route('/enspl', methods=['GET','POST'])
def enspl():

	# if request.method =='POST':  # appuyer sur le bouton pour commander
	return render_template('1enspl.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)