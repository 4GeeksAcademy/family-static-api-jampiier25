
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        self._members.append(member)
        return member

    def delete_member(self, id):
     for member in self.members:
        if member["id"] == id:
            self.members.remove(member)  # Asegúrate de usar self.members y no self._members
            print(f"El usuario {member['first_name']} ha sido eliminado")  # Cambié name a first_name
            return {"done": True}  # Devolvemos un diccionario de éxito
        return {
        "error": f"No se encontró ningún miembro con ID {id} para eliminar."
        }

    def get_member(self, id):
      for member in self.members:
        if member ["id"]  == id:
           return {"error":"no se encontro"}

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
