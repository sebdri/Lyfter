'''Main'''

import FreeSimpleGUI as sg
from model import INCOME, EXPENSE, DATE_FORMAT
from persistance import load_data, save_data


HEADINGS = ["Fecha", "Título", "Monto", "Categoría", "Tipo"]

def movements_to_rows(manager):

    for m in manager.movements:
        rows.append([
            m.date.strftime(DATE_FORMAT),  
            m.title,
            f"{float(m.amount):.2f}",   
            m.category,
            m.m_type,
        ])
    return rows


def refresh(window, manager):

    totals = manager.calculate_totals()  
    window["-TABLE-"].update(values=movements_to_rows(manager))
    window["-INCOME-"].update(f"{totals['income']:.2f}")
    window["-EXPENSES-"].update(f"{totals['expenses']:.2f}")
    window["-BALANCE-"].update(f"{totals['balance']:.2f}")




def category_window(manager):

    layout = [
        [sg.Text("Nombre de la categoría:")],
        [sg.Input(key="-NAME-", size=(30, 1))],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]
    
    window = sg.Window("Agregar categoría", layout, modal=True)


    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Cancelar"):
            break

        if event == "Guardar":
            try:

                manager.add_category(values["-NAME-"])
                save_data(manager)  
                sg.popup("Categoría agregada")
                break
            except ValueError as error:

                sg.popup_error(str(error))

    window.close()



def movement_window(manager, m_type):

    if not manager.categories:
        sg.popup_error("No hay categorías. Agregue una primero.")
        return

    category_names = [c.name for c in manager.categories]

    layout = [
        [sg.Text("Título:", size=(10, 1)), sg.Input(key="-TITLE-", size=(25, 1))],
        [sg.Text("Monto:", size=(10, 1)), sg.Input(key="-AMOUNT-", size=(25, 1))],
        [sg.Text("Categoría:", size=(10, 1)),
        sg.Combo(category_names, default_value=category_names[0],
                key="-CATEGORY-", readonly=True, size=(23, 1))],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]
    window = sg.Window(f"Agregar {m_type.lower()}", layout, modal=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Cancelar"):
            break

        if event == "Guardar":
            try:
                
                manager.add_movement(values["-TITLE-"], values["-AMOUNT-"],
                                    values["-CATEGORY-"], m_type)
                save_data(manager)
                sg.popup(f"{m_type} agregado")
                break
            except ValueError as error:
                sg.popup_error(str(error))

    window.close()



def main_window(manager):

    layout = [
        [sg.Text("Gestor de Finanzas", font=("Helvetica", 16))],


        [sg.Table(values=movements_to_rows(manager), headings=HEADINGS,
                key="-TABLE-", auto_size_columns=False,
                col_widths=[12, 18, 10, 14, 10], justification="left",
                num_rows=12, expand_x=True, expand_y=True)],

        [sg.Text("Ingresos:"), sg.Text("0.00", key="-INCOME-", size=(12, 1)),
        sg.Text("Gastos:"), sg.Text("0.00", key="-EXPENSES-", size=(12, 1)),
        sg.Text("Balance:"), sg.Text("0.00", key="-BALANCE-", size=(12, 1))],

        [sg.Button("Agregar categoría"), sg.Button("Agregar gasto"),
        sg.Button("Agregar ingreso"), sg.Button("Salir")],
    ]


    window = sg.Window("Gestor de Finanzas", layout, resizable=True, finalize=True)
    refresh(window, manager)  

    while True:
        event, _ = window.read()

        if event in (sg.WIN_CLOSED, "Salir"):
            break
        if event == "Agregar categoría":
            category_window(manager)
        elif event == "Agregar gasto":
            movement_window(manager, EXPENSE)
            refresh(window, manager)
        elif event == "Agregar ingreso":
            movement_window(manager, INCOME)
            refresh(window, manager)

    window.close()



def run():
    manager = load_data()
    main_window(manager)


if __name__ == "__main__":
    run()
