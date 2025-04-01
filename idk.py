deathFile = open("death.py", "w")
deathFile.write('num = int(input("Give me an  integer in between 0 and 5000 "))\n')

for i in range(5001):
    deathFile.write(f'if (num == {i}):\n')
    deathFile.write(f'    print("your number is {i}")\n')

deathFile.close()