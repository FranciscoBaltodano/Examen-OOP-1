from classes.data import DATA

class Careers:

    def __init__(self, nombre, id = ""):
        self.nombre = nombre
        self.__id = id
        self.__collection = "Careers"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def delete_all(db):
        collection = db["Careers"]
        collection.delete_many({})

    @staticmethod
    def save_all(db):
        #asignamos la coleccion
        collection = db["Careers"]
        #usamos list para poder iterar y con set evitamos que las carreras se repitan
        #luego recorremos con un for in todos los objetos del DATA
        carrera_unica = list(set([objeto["carrera"]for objeto in DATA]))
        for carrera in carrera_unica:
            #despues de haber recorrido el data y conseguir que las clases duplicadas desaparecieran
            #almacenamos con un insert__one en la coleccion
            collection.insert_one({"name_career":carrera})
