from classes import DbMongo, Dataprocess, DATA
from classes import Students, Careers, Courses, Enrollments
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()

    Students.delete_all(db)
    Students.save_all(db)
    Students("123", "José 201", "0", "0", "23", "Medicina").save(db)

    Careers.delete_all(db)
    Careers.save_all(db)
    Careers("mecatronica", "444").save(db)


    Courses.delete_all(db)
    Courses.save_all(db)
    Courses("Programacion Orientada a Objetos", "999").save(db)


    # pipeline = Dataprocess(DATA)
    # pipeline.create_careers()
    # pipeline.create_students()
    # pipeline.create_enrollments()

    print("Bienvenido a la DB")
    return True










if __name__ == "__main__":
    load_dotenv()
    main()