"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

jackson_family.add_member(
{
    "first_name": "jane",
    "age": "35",
    "lucky_numbers": [ 10, 14, 3]
}   
)

jackson_family.add_member(
{
    "first_name": "john",
    "age": "33",
    "lucky_numbers": [ 7, 13, 22]
}
)

jackson_family.add_member(
{
    "first_name": "jimmy",
    "age": "5",
    "lucky_numbers": [ 1]
}
)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "jampiier",
        "family": members
    }


    return jsonify(response_body), 200


@app.route('/members', methods=['POST'])
def add_member ():
    body = request.get_json()
    members = jackson_family.add_member(body)

    response_body = {
        "members": members
     }
    return jsonify(response_body), 200



@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    deleted_member = jackson_family.delete_member(member_id)  # Usamos el parámetro correcto

    if deleted_member:  # ✅ Ahora el 'if' está bien indentado dentro de la función
        response_body = {
            "message": f"Miembro con ID {member_id} eliminado con éxito.",
            "deleted_member": deleted_member
        }
        return jsonify(response_body), 200
    else:
        return jsonify({"error": "Miembro no encontrado"}), 404


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
