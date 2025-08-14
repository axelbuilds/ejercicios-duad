#Ejercicio Semana 10 - Main

from menu import show_menu  #Import main menu function

def main():
    students = []  #List to store students data
    show_menu(students)  #Starts the menu with the students list

#Ensures the code runs only if executed directly, not when imported
if __name__ == "__main__":
    main()