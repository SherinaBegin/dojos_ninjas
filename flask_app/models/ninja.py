from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
   def __init__(self, data):
      self.id = data['id']
      self.first_name = data['first_name']
      self.last_name = data['last_name']
      self.age = data['age']
      self.created_at = data['created_at']
      self.updated_at = data['upadted_at']

   
   @classmethod
   def create_ninja(cls, data):
      query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s;)"
      result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
      return result
   
   @classmethod
   def get_all_ninjas(cls):
      query = "SELECT * FROM ninjas WHERE id = %(dojo_id)s;"
      results = connectToMySQL('dojos_and_ninjas').query_db(query)
      ninjas = []
      for ninja in results:
         ninjas.append(cls(ninja))
      return ninjas
   
   