from classes.data import DATA

class Enrollments:

    def __init__(self, nombre_alumno, curso, aprobo, id = ""):
        self.nombre_alumno = nombre_alumno
        self.curso = curso
        self.aprobo = aprobo
        self.__id = id
        self.__collection = "Enrollments"

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
        collection = db["Enrollments"]
        collection.delete_many({})

    @staticmethod
    def save_all(db):
        collection = db["Enrollments"]
        for obj in DATA:
            name = obj["nombre_completo"]
            course_aprobade = obj["cursos_aprobados"]
            course_reprobade = obj["cursos_reprobados"]

            for aprobada in course_aprobade:
                enrollment= {"name": name, "course": aprobada, "aprobo": True}
                collection.insert_one(enrollment)

            for reprobada in course_reprobade:
                enrollment= {"name": name, "course": reprobada, "aprobo": False}
                collection.insert_one(enrollment)

