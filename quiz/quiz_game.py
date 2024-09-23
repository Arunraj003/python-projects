

print("Welcome to my computer quiz")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay Let's play :)" )


score = 0
answer = input("what does CPU stands for ?")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does GPU stands for ?")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does RAM stands for ?")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does ROM stands for ?")
if answer.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does PSU stands for ?")
if answer.lower() == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")


print("You had Scored" + str(score) )
print("You had Scored" + str((score / 4) * 100) + "%")


