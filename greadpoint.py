class Subjact():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def gread_point(self):
        if 80<=self.marks<=100:
            return 5
        elif 70<=self.marks<=79:
            return 4
        elif 60<=self.marks<=69:
            return 3.5
        elif 50<=self.marks<=59:
            return 3
        elif 40<=self.marks<=49:
            return 2
        elif 33<=self.marks<=39:
            return 1
        else:
            return 0

    def gread(self):
        if 80<=self.marks<=100:
            return "A+"
        elif 70<=self.marks<=79:
            return "A"
        elif 60<=self.marks<=69:
            return "A-"
        elif 50<=self.marks<=59:
            return "B"
        elif 40<=self.marks<=49:
            return "C"
        elif 33<=self.marks<=39:
            return "D"
        else:
            return "F"

n = int(input("Please Input Your Total Subject :"))

t_gpa = 0
for x in range(n):
    sub_name = input("Please Input your Subject Name :")
    sub_marks = float(input("Plese Input Your Subject Marks :"))
    globals()[sub_name] = Subjact(sub_name,sub_marks)
    t_gpa += globals()[sub_name].gread_point()

gpa = t_gpa/n
print("Total GPA : ",gpa)