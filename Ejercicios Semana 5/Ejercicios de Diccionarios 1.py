#Ejercicio de Diccionarios #1

hotel_rooms = { #Hotel Dictionary
    "nombre": "Python Hotel",
    "numero_de_estrellas": 5,
    "habitaciones": [ #Rooms List
        { #Rooms Dictionary
        "numero": 1,
        "piso": 1,
        "precio_por_noche": '$200'
        },
        {
        "numero": 2,
        "piso": 2,
        "precio_por_noche": '$150'
        }
        ]
}

#Prints Hotel Dictionary Info
print(hotel_rooms["nombre"],hotel_rooms["numero_de_estrellas"],"Estrellas")

#Prints Rooms Dictionary Info
for rooms in hotel_rooms["habitaciones"]:
    print("Habitacion numero:",rooms["numero"],"Piso:",rooms["piso"],"Precio:",rooms["precio_por_noche"])
