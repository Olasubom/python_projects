# create a function that returns another funtion,the return funtion should icrement a counter any time it's called
import string

# def counter():
#     counter = 0 
#     def function():
#          nonlocal counter
#          counter += 1
#          return counter
#     return function 
# time = counter()
# print(time())
# print(time())
# print(time())
# print(time())
# print(time())
# print(time())

# A teacher needs to calculate the average grade of her student and determine their performance,write a python function (grade_student)that accepts a list of scors and returns the average score.the function should also print whether the avarage gradeis an "A"(90-100), "B"(80-89),"C"(70-79),"D"(60-69),or "F"(below 60)
#

def student_grade(score):
    score_of_f = sum(score) / len(score)
    
    if score_of_f >= 80:
        result = "A"
    elif score_of_f >= 70:
        result = "B"
    elif score_of_f >= 50:
        result = "C"
    elif score_of_f >= 40:
        result = "D"
    else:
        result = "F"
    return score_of_f, result
score_input = input("input your score  ")
score = [int (item) for item in score_input.split()]
score_of_f, result = student_grade(score)
print(f"your average score is: {score_of_f:.2f} ")
print(f"your RESULT is {result}")

print("")

#TIME TRAVEL PROBLEM
def time_travel(distance ,speed):
    time = distance/speed 
    return time
m_p_h = time_travel(distance = int(input("distance needed: ")),speed= (int(input(f"speed km/hour: "))))
print(m_p_h)


   



        
        