from classes.data import DATA


class Students:
    def __init__(self, numero_cuenta, nombre_completo, cursos_aprobados, cursos_reprobados, edad, carrera, id =""):
        self.__id  = numero_cuenta
        self.nombre_completo = nombre_completo
        self.cursos_aprobados = cursos_aprobados
        self.cursos_reprobados = cursos_reprobados
        self.edad = edad
        self.carrera = carrera
        self.__collection = "Students"

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
    def get_list(db):
        collection = db["Students"]
        estudiantes = collection.find()

        list_estudiantes = []
        for e in estudiantes:
            temp_estudiante = Students(
                e["_id"]
                , e["nombre_completo"]
                , e["cursos_aprobados"]
                , e["cursos_reprobados"]
                , e["edad"]
                , e["carrera"]
            )

            list_estudiantes.append(temp_estudiante)
        return list_estudiantes

    @staticmethod
    def delete_all(db):
        collection = db["Students"]
        collection.delete_many({})

    @staticmethod
    def save_all(db):
        collection = db["Students"]
        collection.insert_many(DATA)