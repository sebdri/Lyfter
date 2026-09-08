import sys

my_pets={}


def show_menu():
    print("==============================")
    print("   🐾 MIS MASCOTAS 🐾")
    print("==============================")
    print("1. Add a pet")
    print("2. See all pets")
    print("3. Find your pet")
    print("4. Deelete a pet ")
    print("5. Count pets ")
    print("6. View pets per type")
    print("7. Exit")
    print("==============================")



def add_pet():  #Requierments: name . age 
    name = input("Please enter the name of your pet: ")
    while True:
        try:    
            pet_age = int(input("Please enter the age of your pet:"))
            if pet_age < 0 or pet_age > 100 :
                print("Invalid age")
                continue
            break

        except ValueError:
            print("Debe ingresar un número entre 1 y 100.")

    pet_type = input("Please enter your pets type:")

    my_pets[name] = [pet_age , pet_type]


def see_all_pets():
    print("---Your pets 🐕 ")
    if len(my_pets) == 0:
        print("No data yet")
    else:
        for name , data in my_pets.items():
            age = data[0]
            Ptype = data[1]

            print(f'Your pet is: {name}, has {age} years and it is a: {Ptype}')


def find_your_pet():
    pets_name = input("Enter the name of the pet you want to find: ")

    if pets_name in my_pets:
        age = my_pets[ pets_name][0]
        Ptype = my_pets[ pets_name][1]

        print("\n🔍 Pet found: ")
        print(f"{pets_name}, {Ptype}, {age}")

    else: 
        print ("Pet not found 😞")



def delete_pet():

    Dname = input("Enter the name of the pet you want to delete: ")

    if Dname in my_pets:
        del my_pets[Dname]
        print(f"🗑️Your pet {Dname} has been deleted")

    else:
        print(f"Pet {Dname} not found")




def count_pets():
    if len(my_pets) == 0:
        print("No data yet")
    else:
        total = len(my_pets)
        print(f"📊 You have {total} pets")



def show_type():
    type_to_find = input("Enter the type you want to find: ")

    found = False
    print(f"\n🔎 Pets of type '{type_to_find}':")

    for name, data in my_pets.items():
        age = data[0]
        Ptype = data[1]

        if Ptype.lower() == type_to_find.lower():
            print(f"- {name}, {age} years old")
            found = True

    if not found:
        print("No pets found of that type 😞")


def exit():
    print("Bye Bye, take care ")
    sys.exit()

def main():
    while True:
        show_menu()
        option = input("Enter an option: ")

        match option:
            case "1":
                add_pet()
            case "2":
                see_all_pets()
            case "3":
                find_your_pet()
            case "4":
                delete_pet()
            case "5":
                count_pets()
            case "6":
                show_type() 
                
            case "7":
                exit()





if __name__ == "__main__":
    main()
