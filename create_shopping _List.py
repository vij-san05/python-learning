products = [
    {"name":"pen","prise":10,"discription":"for Writing"},
    {"name":"car","prise":100000,"discription":"for travel"},
    {"name":"desk","prise":77,"discription":"for sitting"},
    {"name":"laptop","prise":140,"discription":"for make things easy"}
]
cart= []
while True:
    for index,product in enumerate(products):
        print(f"{index}){product['name']}: ${product['prise']}")
    ID= int(input("Enter Item ID to continue add items"))
    cart.append(products[ID])
    status= input("Wand to continue add: ")
    if status =="YES":
        continue
    else:
        print(cart)
        break




