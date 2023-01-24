from backendComponents import Student, Teacher, Subject

student = Student("Baxter", 15)
teacher = Teacher("politeTeacher")
subject = Subject("hobbies")

prompt = (
    f"The following is a conversation between {teacher.name} and {student.name}. {teacher.character} "
    f"{student.name} is a {student.age} year-old student. "
    f"They are talking about {subject.name} "
    f"During the long conversation {teacher.name} firstly answers {student.name} questions. "
    f"Secondly {teacher.name} asks about {subject.questions}. {teacher.name} asks maximum one question at time."
    f"This is example of a conversation between {teacher.name} and {student.name}:\n{teacher.few_shots}\n"
    f"{teacher.name}: Welcome ")

# print(prompt)

location = "SplitIntoTasks"
