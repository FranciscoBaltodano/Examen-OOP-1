from classes import DbMongo,DATA
from classes import Students, Careers, Courses, Enrollments
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()

    Students.delete_all(db)
    Students.save_all(db)
    #En lugar de pipeline.create_students()
    Students("123", "José 201", "0", "0", "23", "Medicina").save(db)


    Careers.delete_all(db)
    Careers.save_all(db)
    #En lugar de pipeline.create_careers()
    Careers("mecatronica", "444").save(db)


    Courses.delete_all(db)
    Courses.save_all(db)
    #para crear una carrera
    Courses("Programacion Orientada a Objetos", "999").save(db)

    Enrollments.delete_all(db)
    Enrollments.save_all(db)
    # pipeline.create_enrollments()
    Enrollments("Juan", "Lectura", True).save(db)





    #imprimimos nuestro reporte
    Enrollments.get_report_courses(db)

    print("Bienvenido a la DB")
    return True

if __name__ == "__main__":
    load_dotenv()
    main()