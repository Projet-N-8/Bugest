from flask import Flask
from routes.personneRoutes import personne_bp

app = Flask(__name__)
app.config['DATA_FILE'] = 'data/personnes.json'

app.register_blueprint(personne_bp)

if __name__ == '__main__':
    app.run(debug=True)