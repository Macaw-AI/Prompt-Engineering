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
    name = "hobbies and the importance of hobbies"
    questions = "Having a hobbies, how to find them, why it is worth to have hobbies"


prompt = (
    f"The following is a conversation between {Teacher.name} and {Student.name}. {Teacher.character} "
    f"{Student.name} is a {Student.age} year-old student. "
    f"They are talking about {Subject.name}. Firstly teacher welcomes {Student.name}. "
    f"Secondly in a clever way introduces the topic of a conversation."
    f"During the long conversation teacher asks about {Subject.questions}. Teacher asks maximum one question at time. "
    f"Never more.\n"
    # f"Then during the conversation checks what questions are not asked yet. Then asks one.\n"
    # f"{Teacher.few_shots}"
    f"Teacher: Hi")






