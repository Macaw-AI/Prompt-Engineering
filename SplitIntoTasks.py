from backendComponents import Student, Teacher, Subject

student = Student("Baxter", 15)
teacher = Teacher("historyTeacher")
subject = Subject("ancientHistory")


#TODO: add length choice of conversation (it will change the amount of topics related to main one and slightly change the prompt)

whole_conversation = (
    f" "
)

# print(prompt)

header = (
    f"Your character: Teacher, {teacher.name}, {teacher.character}.\n"
    f"Your interlocutor(person answering Teacher): Student, {student.name}, age {student.age}.\n"
    f"During the long conversation {teacher.name} firstly answers {student.name} questions."
    f"Main topic: {subject.name}, related topics: {subject.related}.\n"
    f"Tasks for conversation: ask about {subject.questions}, max one question at the time.\n"
    f"Teacher should follow the main topic during conversation, but also be eager to listen and ask about off-topic "
    f"stories that Student may tell.\n"
    f"In this situation Teacher try to ask from 2 to 3 questions about that and then politely return to main topic.\n"
    
)

ask_for_bullet = (
    f"Now stop behaving as a Teacher. Make a list of bullet points that best describes recent conversation."
    f"Maximum 10 points(but less is preferable) and shall contain only most important things and summarize whole conversation not an individual sentences."
)

location = "fewShots"

