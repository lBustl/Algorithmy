# #Job 1.0
for i in range(101):
    if i//3 == i/3 and i//5 != i/5:
        print("Fizz")
    else :
        if i//5 == i/5 and i//3 != i/3:
         print("Buzz")
        else :
            if i//5 == i/5 and i//3 == i/3:
                print("FizzBuzz")
            else: 
                print (i)



#Job 1.1
def draw_rectangle(w,h):
    print("|",end = "")
    for r in range(w):
            print("-",end = "")
    print("|")
    for i in range(1,h-1):
        print("|",end = "")
        for r in range(w):
            print(" ",end = "")
        print("|")
    print("|",end = "")
    for r in range(w):
            print("-",end = "")
    print("|")
draw_rectangle(10,3)

#Job 1.2
def draw_triangle(h):
    for i in range (h-1):
        print(" "*(h-i) + "/" + " "*i*2 + "\ ")
    print( " /" + "_"*(h-1)*2 + "\ ")
draw_triangle(5)


#Job 1.3
class MathTeacher:
    def __init__(self):
        pass


    def round_grade(grade):
        if grade < 40:
            return grade

        next_multiple_of_5 = (grade // 5 + 1) * 5
        if next_multiple_of_5 - grade < 3:
            return next_multiple_of_5
        else:
            return grade

 
    def grade_students(notes):
        rounded_notes = []
        for note in notes:
            rounded_note = MathTeacher.round_grade(note)
            rounded_notes.append(rounded_note)
        return rounded_notes


