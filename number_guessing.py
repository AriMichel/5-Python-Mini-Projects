
import random

'''r= random.randrange(-5, 11)
rr= random.randint(-5, 10)

print(r)
print(rr)'''



top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<= 0:
        print("Please type a number larger than 0 next time, please")
        quit()

else:
    print("Please type a number next time")
    quit()


random_number = random.randint(0, top_of_range)
print(random_number)

while True:
    