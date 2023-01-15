from backendComponents import Student, Teacher, Subject

student = Student("Baxter", 15)
teacher = Teacher("politeTeacher")
subject = Subject("hobbies")

prompt = (
    f"The following is a conversation between {teacher.name} and {student.name}. {teacher.character} "
    f"{student.name} is a {student.age} year-old student. "
    f"They are talking about {subject.name}. Firstly teacher welcomes {student.name}. "
    f"Secondly in a clever way introduces the topic of a conversation."
    f"During the long conversation teacher asks about {subject.questions}. Teacher asks maximum one question at time. "
    f"Never more.\n"
    # f"Then during the conversation checks what questions are not asked yet. Then asks one.\n"
    # f"{Teacher.few_shots}"
    f"Teacher: Hi ")

# print(prompt)

location = "SplitIntoTasks"

