
print('''
 ____________________
!                    !
!      Welcome       !
!    to  QUICK-QUIZ  !
\____________________/
         !  !
         L_ !
        / _)!
       / /__L
 _____/ (____)
        (____)
 _____  (____)
      \_(____)
         !  !
         \__/   ''')
playing= input("Do you want to play? (y/n) ")

if playing.lower() != "y":
    print("See you around!")
    quit()

print("Let's PLAY! :)")
score = 0 

answer = input("What does CPU stand for? ")
if answer.lower() =="central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong! CPU stands for central processing unit")

answer = input("What does GPU stand for? ")
if answer.lower() =="graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong! GPU stands for graphics processing unit")

answer = input("What does RAM stand for? ").lower()
if answer =="random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong! GPU stands for random access memory")

answer = input("What does PSU stand for? ").lower()
if answer =="power supply":
    print("Correct!")
    score += 1
else:
    print("Wrong! GPU stands for power supply")

print("You got " + str(score) + " questions correct!")
print(f"Your score is {((score/4) * 100)}%")

if score == 0:
    print("""
                                  ___________
                             .---'::'        `---.
                            (::::::'              )
                            |`-----._______.-----'|
                            |              :::::::|
                           .|               ::::::!-.
                           \|               :::::/|/
                            |               ::::::|
                            | Special Flonk Award:|
                            |    for Silliness::::|
                            |               ::::::|
                            |              .::::::|
                            J              :::::::F
                             \            :::::::/
                              `.        .:::::::'
                                `-._  .::::::-'
                                    |   ""|"
                                    |  :::|
                                    F   ::J
                                   /     ::\                                        
                              __.-'      :::`-.__
                             (_           ::::::_)
                               `""-----------""'

""")