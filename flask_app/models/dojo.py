from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
   def __init__(self, data):
      self.id = data['id']
      self.city = data['city']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']
      self.ninjas = []

   @classmethod
   def get_all(cls):
      query = 'SELECT * FROM dojos;'
      results = connectToMySQL('dojos_and_ninjas').query_db(query)
      dojos = []
      for dojo in results:
         dojos.append(cls(dojo))
      return dojos

   @classmethod 
   def save_dojo(cls, data):
      query = 'INSERT INTO dojos(city, created_at, updated_at) VALUES (%(city)s, NOW(), NOW());'
      result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
      return result

   @classmethod
   def get_one(cls, data):
      query = 'SELECT * FROM dojos WHERE id = %(id)s;'
      result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
      return cls(result[0])
   
   @classmethod
   def delete_dojo(cls, data):
      query = "DELETE FROM dojos WHERE id = (%(id)s);"
      return connectToMySQL('dojos_and_ninjas').query_db(query, data)

   @classmethod
   def get_dojo_with_ninjas(cls, data):
      query = 'SELECT * from dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojo.id WHERE dojo.id = %(id)s;'
      results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
      print(results)
      dojo = cls( results[0])

      for row_from_db in results:
         ninja_data = {
            'id': row_from_db['ninjas.id'],
            'first_name': row_from_db['first_name'],
            'last_name': row_from_db['last_name'],
            'age': row_from_db['age'],
            'created_at': row_from_db['ninjas.created_at'],
            'updated_at': row_from_db['ninjas.updated_at']
         }
         dojo.ninjas.append(Ninja(ninja_data))
      return dojo