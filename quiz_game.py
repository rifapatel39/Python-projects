print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")


answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")


answer = input("What is brain of computer system called? ")
if answer.lower() == "cpu":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")


answer = input("who is the father of computers? ")
if answer.lower() == "charles babbage":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4)*100) + "%")