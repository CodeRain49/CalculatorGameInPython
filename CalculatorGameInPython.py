from random import randint

totalScore = 0

#player select the operator { +  -  * }
while True:
    selectOperator = input("Choose operator => + , - , * : ")
    if selectOperator in ["+","-","*"]:
        break
    else:
        print("[Invalid Input]")


def RndNumber():
    num1 = randint(1,99)
    num2 = randint(1,99)
    print(f"{num1} {selectOperator} {num2}")
    return num1,num2

def Calculate(num1,num2):
    match selectOperator:
        case "+":
            num1 + num2
            return num1 + num2
        case "-":
            num1 - num2
            return num1 - num2
        case "*":
            num1 * num2
            return num1 * num2

# Main Program
for x in range(5):
    num1,num2 = RndNumber()
    correct_answer = Calculate(num1,num2)

    while True:
        try:
            answer = int(input("Ans: "))
            break
        except:
            print("[Invalid Input]")

    if answer == correct_answer:
        print("Correct!")
        totalScore += 1
    else:
        print(f"Wrong!! -> The Correct Answer is : {correct_answer}")

print(" ")
print(f"Total: {totalScore}/5")



