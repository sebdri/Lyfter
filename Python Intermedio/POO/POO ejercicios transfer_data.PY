import csv
from Student import Student   


def export_data(file_path, students):

    if len(students) == 0:
        print("Error, There is no data")
        return


    headers = [
        "name",
        "section",
        "spanish",
        "english",
        "social_studies",
        "science",
        "average"
    ]


    with open(file_path, "w", encoding="utf-8", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()


        for student in students:

            writer.writerow({
                "name": student.name,
                "section": student.section,
                "spanish": student.spanish,
                "english": student.english,
                "social_studies": student.social_studies,
                "science": student.science,
                "average": student.average
            })


    print("Data successfully exported.")



def import_data(file_path, students):

    try:

        with open(file_path, "r", encoding="utf-8", newline="") as file:

            reader = csv.DictReader(file)

            students.clear()


            for row in reader:

                student = Student(
                    row["name"],
                    row["section"],
                    int(row["spanish"]),
                    int(row["english"]),
                    int(row["social_studies"]),
                    int(row["science"])
                )


                students.append(student)


        print("Data successfully imported.")

        return students


    except FileNotFoundError:

        print("No data has been previously exported.")

        return students