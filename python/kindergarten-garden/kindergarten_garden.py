class Garden:
    def __init__(self, diagram: str, students=None):
        self.diagram = diagram

        if students is None:
            students = [
                "Alice",
                "Bob",
                "Charlie",
                "David",
                "Eve",
                "Fred",
                "Ginny",
                "Harriet",
                "Ileana",
                "Joseph",
                "Kincaid",
                "Larry",
            ]

        self.students = sorted(students)

        self.plants_names = {
            "C": "Clover",
            "G": "Grass",
            "R": "Radishes",
            "V": "Violets",
        }

    def plants(self, student: str) -> list:
        rows = self.diagram.split("\n")
        cups = [
            [
                (self.plants_names[row[index]], self.plants_names[row[index + 1]])
                for index in range(len(row))
                if index % 2 == 0 and index + 1 < len(row)
            ]
            for row in rows
        ]
        students_plants = [[] for index in range(len(self.students))]

        for row_cups in cups:
            for index in range(len(row_cups)):
                students_plants[index].append(row_cups[index])

        students_plants = [
            [plant for plants in student_plants for plant in plants]
            for student_plants in students_plants
        ]

        return students_plants[self.students.index(student)]
