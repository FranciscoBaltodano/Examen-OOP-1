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
    def get_list(db):
        collection = db["Courses"]
        carreras = collection.find()

        list_carreras = []
        for e in carreras:
            temp_carrera = Careers(
                e["_id"] 
            )

            list_carreras.append(temp_carrera)
        return list_carreras

    @staticmethod
    def delete_all(db):
        collection = db["Courses"]
        collection.delete_many({})

    @staticmethod
    def save_all(db):
        collection = db["Courses"]
        name_courses = []
        
        for obj in DATA:
            
            for course in obj["cursos_aprobados"]:
                if course not in name_courses:
                    name_courses.append(course)
            
            for course in obj["cursos_reprobados"]:
                if course not in name_courses:
                    name_courses.append(course)
        
        document = {"name_course": name_courses}
        collection.insert_one(document)
