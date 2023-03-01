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
        #asignamos la coleccion
        collection = db["Enrollments"]
        #iteramos con for in para recorrer el DATA
        for obj in DATA:
            #asignamos keys de los objetos que hay en DATA a variables
            name = obj["nombre_completo"]
            course_aprobade = obj["cursos_aprobados"]
            course_reprobade = obj["cursos_reprobados"]
            #iteramos primero los que son cursos aprobados
            for aprobada in course_aprobade:
                #agregamos un parametro booleanos que nos indica si aprobo o no
                enrollment= {"name": name, "course": aprobada, "aprobo": True}
                #por cada curso aprobado, insertamos un objeto llamado enrollment a la coleccion
                collection.insert_one(enrollment)
            #lo mismo pero con los cursos reprobados
            for reprobada in course_reprobade:
                enrollment= {"name": name, "course": reprobada, "aprobo": False}
                collection.insert_one(enrollment)

    @staticmethod
    def get_report_courses(db):
        #indicamos la coleccion
        collection = db["Enrollments"]
        #creamos un set para que los cursos no se dupliquen
        courses = set()
        #iteramos para recorrer el DATA
        for obj in DATA:
            #asignamos a courses los cursos aprobadoy reprobados
            courses.update(obj["cursos_aprobados"])
            courses.update(obj["cursos_reprobados"])
        #iteramos para cada curso encontrado
        for course in courses:
            #inicializamos nuestras variables con 0
            aprobados = 0
            reprobados = 0
            for obj in DATA:
                #vamos sumando 1 estudiante por cada estudiante que apruebe
                if course in obj["cursos_aprobados"]:
                    aprobados += 1  
                #vamos sumando 1 estudiante por cada estudiante que apruebe
                if course in obj["cursos_reprobados"]:
                    reprobados += 1
            #mandamos a imprimir a la terminal nuestro reporte
            print("curso:",course, ", aprobados:", aprobados,", reprobados:", reprobados)


    @staticmethod
    def get_report_careers(db):
        collection = db["Enrollments"]
        reportCareers = {}
        for student in DATA:
            #asignamos en career todas las carreras de DATA
            career = student["carrera"]
            #usamos el metodo get para que no se repitan las carreras
            if career in reportCareers:
                students = reportCareers[career]
            else:
                students = 0
        #imprimimos el reporte
        for career, students in reportCareers.items():
            print("{carrera:", career, ", Estudiantes:", students,"}")
