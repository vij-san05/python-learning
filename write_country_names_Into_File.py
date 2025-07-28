with open('country_name.txt','a') as file:
    countryName = input("Enter the country name")
    file.write(countryName+'\n')

print("Name has been written")

