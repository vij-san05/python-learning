while True:
    with open('country_name.txt','a') as file:
        countryName = input("Enter the country name")
        file.write(countryName+'\n')
        choice= input("Do you wnna continue add name? (y/n)")
        if choice=='n':
            break

print("Name has been written")

