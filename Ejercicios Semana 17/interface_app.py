import FreeSimpleGUI as sg

# ====================================
# Main Window
# ====================================

def transaction_window(type, manager_instance):
    #Get categories from the manager instance
    category_list = manager_instance.get_categories()
    #Categories cannot be created without a category
    if not category_list:
        sg.popup_error("Debe agregar al menos una categoría primero.", title = "Error de Categoría")
        return False

    window_title = f"Registrar {type.capitalize()}"
    
    layout = [
        [sg.Text(f"Detalles del {type.upper()}", font=('Arial', 14, 'bold'), justification='center', expand_x=True)],
        [sg.Text("Título:", size=(10, 1)), sg.Input(key='-TITLE-', expand_x=True)],
        [sg.Text("Monto:", size=(10, 1)), sg.Input(key='-AMOUNT-', expand_x=True)],
        [sg.Text("Categoría:", size=(10, 1)), sg.Combo(category_list, default_value=category_list[0], key='-CATEGORY-', readonly=True, expand_x=True)],
        #Validation message
        [sg.Text("", size=(40, 1), key='-MSG-', text_color='yellow')],
        [
            sg.Push(), 
            sg.Button("Guardar", key='-SAVE-', size=(12, 1), bind_return_key=True), 
            sg.Button("Cancelar", key='-CANCEL-', size=(12, 1)),
            sg.Push()
        ],
    ]
    
    window = sg.Window(window_title, layout, modal=True, finalize=True)
    
    while True:
        event, values = window.read()
        #Closes the window without saving any changes
        if event in (sg.WIN_CLOSED, '-CANCEL-'): 
            break
        
        if event == '-SAVE-':
            #Validation and creation of transaction
            success, message = manager_instance.add_transaction(type, values['-TITLE-'], values['-AMOUNT-'], values['-CATEGORY-'])
            if success:
                sg.popup_ok(message)
                window.close()
                return True
            #Display validation error message
            window['-MSG-'].update(message)
    
    window.close()
    return False

def category_window(manager_instance):
    #Displays window to add a new category
    layout = [
        [sg.Text("Nueva Categoría", font=('Arial', 12, 'bold'))],
        [sg.Input(key='-CAT_NAME-', expand_x=True)],
        #Validation message
        [sg.Text("", key='-MSG_CAT-', text_color='yellow')],
        [
            sg.Push(),
            sg.Button("Guardar", key='-SAVE_CAT-', size=(10, 1)),
            sg.Button("Cerrar", key='-CLOSE-', size=(10, 1)),
            sg.Push()
        ],
    ]
    window = sg.Window("Categorías", layout, modal=True, finalize=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-CLOSE-'): break
        if event == '-SAVE_CAT-':
            #Validation and creation of category
            success, message = manager_instance.add_category(values['-CAT_NAME-'])
            if success:
                sg.popup_ok(message)
                window.close()
                return True
            #Display validation error message
            window['-MSG_CAT-'].update(message)
    window.close()
    return False

# ====================================
# Main UI Layout
# ====================================

def main_layout(manager_instance):
    #Main window
    sg.theme('DarkGrey9')

    table_headers = ['Monto', 'Título', 'Categoría', 'Fecha']
    
    button_size = (18, 1)
    
    layout = [
        [sg.Text("Gestor de Finanzas Personales", font=('Arial', 18, 'bold'), justification='center', expand_x=True)],
        [sg.Text(f"Balance Total: ₡ {manager_instance.get_balance()}", key='-BAL-', font=('Arial', 16), text_color='lightgreen', justification='center', expand_x=True)],
        
        # Transactions Table
        [sg.Text("Historial de Movimientos:", font=('Arial', 11))],
        [sg.Table(
            values=manager_instance.get_formatted_data(),
            headings=table_headers,
            auto_size_columns=True,
            num_rows=12,
            key='-TABLE-',
            expand_x=True,
            justification='left'
        )],

        [sg.VPush()], # Pushes buttons to the bottom
        #Transaction Buttons
        [sg.Column([
            [
                sg.Button("Agregar Ingreso", key='-INCOME-', size=button_size, button_color=('white','#28a745')),
                sg.Button("Agregar Gasto", key='-EXPENSE-', size=button_size, button_color=('white', '#dc3545')),
                sg.Button("Nueva Categoría", key='-CAT_ADD-', size=button_size, button_color=('white', "#dc7d35")),
            ],
            #Utility Buttons
            [
                sg.Button("Exportar a CSV", key='-CSV-', size=button_size, button_color=('black', '#ffc107')),
                sg.Button("Eliminar Historial", key='-DELETE-', size=button_size, button_color=('black', "#07b5ff")),
                sg.Button("Salir", key='-EXIT-', size=button_size),
            ]
        ], element_justification='center', expand_x=True)]
    ]

    #Window Title and Size
    window = sg.Window("Aplicación de Finanzas", layout, size=(700,350),finalize=True, resizable=True)

    # Main Loop
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-EXIT-'):
            break

        data_changed = False
        
        if event == '-INCOME-':
            data_changed = transaction_window("ingreso", manager_instance)
        elif event == '-EXPENSE-':
            data_changed = transaction_window("gasto", manager_instance)
        elif event == '-CAT_ADD-':
            data_changed = category_window(manager_instance)
        elif event == '-CSV-':
            # File picker for export
            save_path = sg.popup_get_file('Guardar reporte', save_as=True, no_window=True, default_extension='.csv', file_types=(("CSV Files", "*.csv"),))
            if save_path:
                success, msg = manager_instance.export_to_csv(save_path)
                sg.popup_ok(msg) if success else sg.popup_error(msg)
        elif event == '-DELETE-':
            if sg.popup_yes_no("¿Está seguro de borrar todo el historial?", title="Confirmar") == 'Yes':
                success, msg = manager_instance.clear_history()
                if success:
                    data_changed = True
                    sg.popup_ok(msg)

        # Global UI Refresh
        if data_changed:
            window['-TABLE-'].update(values=manager_instance.get_formatted_data())
            window['-BAL-'].update(f"Balance Total: ₡ {manager_instance.get_balance()}")

    window.close()