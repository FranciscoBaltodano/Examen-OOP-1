from classes import DbMongo, Dataprocess, DATA
from classes import Students, Careers, Courses, Enrollments
from dotenv import load_dotenv


from classes import DATA, Dataprocess

def main():
    client, db = DbMongo.getDB()

    # Students.save_all(db)
    # Students("1", "2", "3", "4", "5", "6", ).save(db)



    # collection = db["Students"]
    # collection.insert_many(DATA)
    Students.delete_all(db)
    Students.save_all(db)

    Careers.delete_all(db)
    Careers.save_all(db)
    # Careers("medicina", "121").save(db)


    Courses.delete_all(db)
    Courses.save_all(db)

    pipeline = Dataprocess(DATA)
    pipeline.create_careers()
    pipeline.create_students()
    pipeline.create_enrollments()

    print("Bienvenido a la DB")
    return True










if __name__ == "__main__":
    load_dotenv()
    main()