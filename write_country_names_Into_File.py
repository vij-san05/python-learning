while True:
    with open('country_name.txt','a') as file:
        countryName = input("Enter the country name")
        file.write(countryName+'\n')
        choice= input("Do you wnna continue add name? (y/n)")
        if choice=='n':
            break
print("Name has been written")

with open('country_name.txt','r') as file:
    All_names= file.readlines()

Capital_name =[]
for name in All_names:
    Capital_name.append(name.strip().capitalize())
print(Capital_name)

