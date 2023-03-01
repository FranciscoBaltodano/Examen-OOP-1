from classes.data import DATA

class Courses:

    def __init__(self, name, id = ""):
        self.name = name
        self.__id = id
        self.__collection = "Courses"

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
        collection = db["Courses"]
        collection.delete_many({})

    @staticmethod
    def save_all(db):
        #asignamos la coleccion
        collection = db["Courses"]
        #creamos un set para que los cursos almacenados no se repitan
        course_unic = set()
        #con un for in recorremos DATA
        for obj in DATA:
            for course in obj["cursos_aprobados"] + obj["cursos_reprobados"]:
                #verificamos que nuestro curso no este agregado para asi, agregarlo
                if course not in course_unic:
                    #si no existia, lo agregamos con el insrt_one
                    collection.insert_one({"name_course": course})
                    #agregamos el curso al course_unic para que sea otro de los cursos que no hay que duplicar
                    course_unic.add(course)
