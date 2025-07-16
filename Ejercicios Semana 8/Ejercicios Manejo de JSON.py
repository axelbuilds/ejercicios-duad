#Ejercicio de Archivos JSON

import json

def load_pokemon_file(file_path): #Reads the json file and returns the list
    with open(file_path,'r',encoding='utf-8') as x: #x = open file variable
        return json.load(x)


def get_int_input(prompt):
    while True: #Catches strings and request for a valid number
        try:
            return int(input(prompt))
        except ValueError:
            print(
                "Digite un numero valido"
            )


def get_new_pokemon(): #Requests pokemon information
    pokemon_name = input("Escriba el nombre del Pokemon: ")
    pokemon_type = input("Escriba el tipo del Pokemon: ")
    print("Escriba los Stats del Pokemon")
    pokemon_stats = {
        "HP": get_int_input("HP: "),
        "Attack": get_int_input("Attack: "),
        "Defense": get_int_input("Defense: "),
        "Sp. Attack": get_int_input("Sp. Attack: "),
        "Sp. Defense": get_int_input("Sp. Defense: "),
        "Speed": get_int_input("Speed: ")
    }
    #Returns the new pokemon to the json file
    return {
        "name": {"english": pokemon_name},
        "type": pokemon_name,
        "base": pokemon_stats
    }


def save_pokemon(file_path, pokemon_list): #Writes the updated pokemon list to the file
    with open(file_path, 'w', encoding='utf-8') as x:
        json.dump(pokemon_list, x, indent=2)

def main():
    file_path = '/Users/akuseru/Documents/Programming/Python/Ejercicios Semana 8/pokemon.json'
    pokemon_list = load_pokemon_file(file_path) #Loads pokemon list
    new_pokemon = get_new_pokemon() #Adds new pokemon information
    pokemon_list.append(new_pokemon) #Appends the pokemon data to the list
    save_pokemon(file_path, pokemon_list) #Saves updated list

    print("El pokemon ha sido agregado a la lista.")


main()