from classes.data import DATA
from classes.Careers import Careers
from classes.Courses import Courses
from classes.Students import Students
from classes.Enrollments import Enrrolments
from classes.DbMongo import DbMongo
import pymongo




class Dataprocess:

    def __init__(self, data):
        self.__data = data
        self__collection = "Dataprocess"

    def create_careers(self):
        ## Do something to create careers on your mongodb collection using __data
        return True
    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        return True
    def create_students(self , numero_cuenta, nombre_completo, cursos_aprobados, cursos_reprobados, edad, carrera, id =""):
        ## Do something to create students on your mongodb collection using __data
        # collection = db["Students"]
        # estudiante = {"numero_cuenta":numero_cuenta,
        #                 "nombre_completo":nombre_completo,
        #                 "cursos_aprobados":cursos_aprobados,
        #                 "cursos_reprobados":cursos_reprobados,
        #                 "edad":edad,
        #                 "carrera":carrera,
        #                 "__id" :id
        #                 "collection" = "Students"}
        # collection.insert_one(estudiante)

        return True
    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        return True











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
        lista_e = Students.get_list(db)
        for e in lista_e:
            e.delete(db)

    @staticmethod
    def print_full_report_long_path(db):
        collection = db["Students"]

        for e in collection.find():
            r = { 
                "nombre" : e["nombre"]
                , "telefono": e["telefono"] 
                , "tipo": Tipoestudiante.get_one(db, e["tipo_estudiante"] ).tipo
            }
            print(r)

    @staticmethod
    def print_full_report_short_path(db):
        collection = db["Students"]

        result = collection.aggregate([
            {
                '$lookup': {
                    'from': "tipo_estudiante"
                    , 'localField': "tipo_estudiante"
                    , "foreignField": "_id"
                    , "as": "te"
                }
            },{
                '$project': {
                    'nombre': 1
                    , 'telefono': 1
                    , 'te.tipo': 1
                }  
            }
        ])

        for d in result:
            print(d)
