import random
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','(',')']
passwordeasy=''
passwordhard=[]
noalpha = int(input("Enter number of alphabets you want in the password\n"))
nonumber = int(input("Enter number of Numbers you want in the password\n"))
nosymbol = int(input("Enter number of symbols you want in the password\n"))
for i in range(0,noalpha):
    passwordeasy+=random.choice(alpha)
    passwordhard.append(random.choice(alpha))
for i in range(0,nonumber):
    passwordeasy+=random.choice(number)
    passwordhard.append(random.choice(number))
for i in range(0,nosymbol):
    passwordeasy+=random.choice(symbol)
    passwordhard.append(random.choice(symbol))

print('Esay Password is -'+passwordeasy)
random.shuffle(passwordhard)
final=''
for i in passwordhard:
    final+=i
print('Hard Password -'+final)