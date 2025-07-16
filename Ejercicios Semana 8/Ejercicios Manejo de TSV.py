#Ejercicio de Archivos TSV

import csv

#CSV File Headers - TSV Tab Separated
file_headers = (
    'NOMBRE DE VIDEOJUEGO',
    'GENERO',
    'DESARROLLADOR',
    'CLASIFICACION ESRB'
)


def get_videogames(headers):
    videogames_list = [] #Empty game list
    
    while True: #Request the number of videogames to register
        try: 
            game_amount = int(input("Digite la cantidad de videojuegos que desea registrar: "))
            if game_amount <= 0: #Requests to enter a number higher than 0
                print("Por favor ingrese un numero mayor a 0.")
                continue
            break
        except ValueError: #Catches strings and requests to enter a valid number
            print(
            'Digite la cantidad que desea ingresar en numeros. Ejemplo: 1, 2, 3...'
            )

    for index in range(game_amount): #Loop to collect video games information
        game_data = {} #Empty Dictionary
        for header in headers:
            data = input(f'Ingrese {header}: ') #Request for the value in each header field
            game_data[header] = data #Saves the information under the file column
        videogames_list.append(game_data) #Adds the dictionary to the list
        print('La informacion se agrego correctamente.') #Confirms the information has been saved
    return videogames_list #Returns the list of videogames


def write_csv_games(file_path,data,headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers, delimiter='\t') #Create CSV writer with headers - data will be delimited with tab instead of commas
        writer.writeheader() #Write the header row
        writer.writerows(data) #Write all the data rows


def main():
    videogames_list = get_videogames(file_headers) #Gets input from get_videogames
    write_csv_games('/Users/akuseru/Documents/Programming/Python/Ejercicios Semana 8/games.csv', videogames_list, file_headers) #Calls write_csv_games function and saves data to the CSV file


main()