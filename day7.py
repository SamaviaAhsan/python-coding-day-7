def electricity_bill():
 while True:
    units=int(input("Enter your units"))
    # while True:
    if units==0:
       break
    if units<= 100:
       print("bill is : ",units*10)
       
    elif units>100 and units<=200:
       print("bill is : ",units*15)
       
    elif units>200 and units<=300:
         print("bill is : ",units*20)
         
electricity_bill()




def verify_pin():
    correct_pin = "1234"
    attempts = 3
    while attempts>0:
     pin = input("Enter your pin: ")
    # while attempts>0:
     attempts -= 1
     if pin == "1234":
            print("Pin verified successfully!")
            break
     else :
                   print(" invalid pin.remaining pins are: ", attempts)
    else:
        print("You have exceeded the maximum number of attempts. Please try again later.")
        
    
verify_pin()           



def find_second_larges():
    largest=None
    second_largest=None
    for i in range(5):
        num=int(input("Enter a number: "))
        if largest is None or num>largest:
            second_largest=largest
            largest=num
        elif second_largest is None or num>second_largest:
            second_largest=num
    print("The second largest number is: ", second_largest)
find_second_larges()    




def salary_calculator():
    while True:
        salary=int(input("Enter your salary: "))
        if salary==0:
            break
        if salary<=30000:
            print("your bonus is 5% of your salary: ",salary*0.05+salary)
        elif salary>30000 and salary<=60000:    
            print("your bonus is 10% of your salary: ",salary*0.10+salary)
        else:
            print("your bonus is 15% of your salary: ",salary*0.15+salary)    
salary_calculator()  




def count_letters():
    sentence = input("Enter a sentence: ")

    vowels = 0
    consonants = 0

    for char in sentence.lower():

        if char in "aeiou":
            vowels += 1

        elif char >= 'a' and char <= 'z':
            consonants += 1

        else:
            # Ignore spaces, digits, and special characters
            pass

    print("Total vowels:", vowels)
    print("Total consonants:", consonants)


count_letters()



def online_quiz():
    score = 0

    questions = [
        ("What is the capital of Pakistan? ", "Islamabad"),
        ("How many days are in a week? ", "7"),
        ("What is 5 + 5? ", "10"),
        ("Which language are we learning? ", "Python"),
        ("How many months are in a year? ", "12")
    ]

    for question, answer in questions:
        user_answer = input(question)

        if user_answer.lower() == answer.lower():
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer!")
            print("Correct answer is:", answer)

    print("\nYour total score is:", score, "/ 5")

    if score == 4 or score == 5:
        print("Excellent")
    elif score == 3:
        print("Good")
    else:
        print("Keep Practicing")


online_quiz()
