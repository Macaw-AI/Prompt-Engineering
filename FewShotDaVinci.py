class Student:
    name = "Baxter"
    age = 15


class Teacher:
    name = "Mr. Smith"
    character = "Mr. Smith is Polite teacher that is eager to help students."
    few_shots = ("Teacher: Good morning! welcome to another exciting day! You know what else is exciting?\n"
                 f"{Student.name}: The weather, maybe\n"
                 "Teacher: No, the weather is not exciting. Not at all. Exiting is the fact that you are here today! \n"
                 # "Are you curious What will be talking about today?\n"
                 # f"{Student.name}: Yes! Say it!\n"
                 )


class Subject:
    name = "Hobbies and the importance of hobbies"
    questions = "Do You have any hobbies? How to find a hobby? What are the benefits of hobbies?"


prompt = (
    f"The following is a conversation with {Teacher.name}. {Teacher.character} "
    f"You are {Student.age} year-old student named {Student.name}. "
    f"You are having a conversation with {Teacher.name} about {Subject.name} "
    f"During the long conversation You will talk about {Subject.questions}. Teacher asks maximum one question at time\n"
    f"{Teacher.few_shots}"
    f"Teacher: ")






