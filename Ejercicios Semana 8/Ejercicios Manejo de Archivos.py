#Ejercicio de Archivos

def open_songs_file(path_input, path_output):
    with open(path_input) as file: #Opens the file
        songs = file.readlines() #Reads each line of the file and saves as a list

    sorted_songs = sorted(songs) #Sorts the lines alphabetically

    for song in sorted_songs:
        print(song, end='') #Prints the songs. end='' avoid adding extra lines \n

    with open(path_output, 'w') as new_file: #Opens/Creates a new file on Write mode
        for song in sorted_songs: #Writes each line in the new file
            new_file.write(song)

#Calls function with input and output paths
open_songs_file(
    '/Users/akuseru/Documents/Programming/Python/Ejercicios Semana 8/songs.txt',
    '/Users/akuseru/Documents/Programming/Python/Ejercicios Semana 8/songs_alphabetically_sorted.txt'
)