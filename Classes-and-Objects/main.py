class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name: str = name
        self.age: int = age
        self.track: list = track
        self.score: float = score
        #print(f"my name is {name}, my age is {age}, and my score is {score}")

    def change_name(self, new_name):
        self.new_name = new_name
        print(f"the student's name is {new_name}")

    def change_age(self, new_age):
        self.new_age = int(new_age)
        print(f"the student's age is {new_age}")

    def add_track(self, new_track):
        self.new_track = new_track
        print(f"the student's track is {new_track}")

    def get_score(self):
        print(f"the student's score is {self.score}")


Bob = Student(name="Bob", age=26, track=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
