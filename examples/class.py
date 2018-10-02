class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (1, 2, 3)
    
    def total(self):
        return sum(self.numbers)


# player = LotteryPlayer('Rolf')
# player.numbers = (32, 56, 77)
# player_2 = LotteryPlayer('Marcelo')

# print(player.name)
# print(player.total())

###################################

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def friend(cls, object, friend_name, *args, **kwargs):
        return cls(friend_name, object.school, *args, **kwargs)

    @classmethod
    def go_to_school(cls):
        print("I'm going to school!")

    @staticmethod
    def come_back_to_school():
        print("I'm coming back to school!")


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


mari = WorkingStudent('Maria', 'Oxford', 20.00, 'Mathematic') 
print(mari.salary)

dani = WorkingStudent.friend(mari, 'Daniel', 20, 'Developer')
print(dani.job_title)

anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(100)
print(anna.marks)
print(anna.average())

def que_son_args_kwargs(*args, **kwargs):
    print(sum(args))
    print(args)
    print(kwargs)
		
que_son_args_kwargs(1, 2, 3, 4, 5, 6, name='Pablo', location='Un lugar', edad=20)
