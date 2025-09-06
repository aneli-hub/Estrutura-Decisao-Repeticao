i = 1
#enquanto 1 for menor que 6
while i < 6:
    print(1)
    i = i + 1 # somando i + 1


 #Pare o código quando o i valer 3 
i = 1
while i < 6:
    print(i)
    if i == 3:
       break
    i = i + 1

#Break -> para looping
# continue -> pula para o proximo looping

i = 1
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)