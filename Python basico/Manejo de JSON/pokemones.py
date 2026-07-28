import json

def read_file(file_path):
    with open(file_path , 'r', encoding='utf-8', newline='') as file:
        pokemons=json.load(file)
    return pokemons

def new_data_entry():
    name = input("Ingrese el nombre de su nuevo pokemon: ")
    category = input("Ingrese de que tipo es dicho pokemon: ")
    level = int(input("Ingrese el nivel de su pokemon: "))
    weight_kg = float(input("Ingrese el peso de su pokemon:"))

    is_shiny = input("¿Es shiny? (si/no): ").lower()=='si'

    held_item = input("Objeto equipado (deje vacío si no tiene): ")
    if held_item == '':
        held_item = None

    
    print('Ingrese las 4 habilidades de su pokemon:')
    skills=[]

    for i in range(4):
        skill = input(f'Hablidad {i+1}:')
        skills.append(skill)
    
    stats = {
    "hp": int(input("HP: ")),
    "attack": int(input("Attack: ")),
    "defense": int(input("Defense: ")),
    "sp_attack": int(input("Sp. Attack: ")),
    "sp_defense": int(input("Sp. Defense: ")),
    "speed": int(input("Speed: "))
    }


    new_pokemon = {
        "Nombre": name,
        "Tipo": category,
        "Nivel": level,
        "Peso (kg)": weight_kg,
        "is_shiny": is_shiny,
        "Articulo": held_item,
        "Habilidades": skills,
        "Estadisticas": stats
    }

    return new_pokemon

def save_files(file_path , pokemons):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        json.dump(pokemons,file,indent=4)


def main():
    file_path = "pokemon.json"
    pokemons = read_file(file_path)
    new_pokemon = new_data_entry()
    pokemons.append(new_pokemon)
    save_files(file_path, pokemons)
    print("¡Pokémon agregado correctamente!")

main()


