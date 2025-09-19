"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
from ejemploPerros import Perros #importo la clase 
from ejemploHerencia import Animal, Vaca, Grillo, Molusco

# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


#creando mi perro
pocholo = Perros('pocholo', 10, 'no')
lula = Perros('lula', 5, 'si')

print(pocholo.nombre)

print(lula.nombre)
print(pocholo._edad)

print(lula._edad)

pocholo.ladrar()
lula.ladrar()

print('antes de jugar', pocholo.contento)
pocholo.jugar()
print('despues de jugar', pocholo.contento)

lula.sanar()

pepito = Grillo('pepito')
pepito.hablar()

lola = Vaca('lola')
lola.hablar()
print(pepito.comer)
print(lola.comer)

whosThatAnimal = Animal('esperpento')
print(whosThatAnimal.comer)
print(whosThatAnimal.hablar())

print('whosThatAnimal.alive',whosThatAnimal.alive)
print('pepito.alive',pepito.alive)
print('lola.alive', lola.alive)

molu = Molusco('molu')
print(molu.alive)
print(molu.comer)
print(molu.nombre)
molu.hablar()

molu.responder('que comes???? ')
lola.responder('muu muu muuu muuuuuuuuuu')

lola.darLeche() #funciona porque tenemos darLechge como metodo para la clase Vaca
#molu.darleche() # el metodo darLeche es propio de la vaca, por lo que la clase molusco no puede ejecutarlo 

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"hello": "world",
                     "family": members}
    return jsonify(response_body), 200



# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
