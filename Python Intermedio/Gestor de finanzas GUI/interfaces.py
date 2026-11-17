'''Interfaz gráfica del gestor de finanzas.'''

import FreeSimpleGUI as sg
from model import INCOME, EXPENSE, DATE_FORMAT
from persistence import save_data


HEADINGS = ["Fecha", "Título", "Monto", "Categoría", "Tipo"]
COL_WIDTHS = [12, 18, 10, 14, 10]


def format_money(value):
    return f"{float(value):.2f}"


def movement_to_row(movement):
    return [
        movement.date.strftime(DATE_FORMAT),
        movement.title,
        format_money(movement.amount),
        movement.category,
        movement.m_type,
    ]


def movements_to_rows(manager):
    return [movement_to_row(m) for m in manager.movements]


def refresh(window, manager):
    totals = manager.calculate_totals()
    window["-TABLE-"].update(values=movements_to_rows(manager))
    window["-INCOME-"].update(format_money(totals["income"]))
    window["-EXPENSES-"].update(format_money(totals["expenses"]))
    window["-BALANCE-"].update(format_money(totals["balance"]))


def labeled_input(label, key):
    return [sg.Text(label, size=(10, 1)), sg.Input(key=key, size=(25, 1))]


def save_cancel_buttons():
    return [sg.Button("Guardar"), sg.Button("Cancelar")]


def run_form(title, layout, on_save):
    window = sg.Window(title, layout, modal=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        if event == "Guardar":
            try:
                on_save(values)
                break
            except ValueError as error:
                sg.popup_error(str(error))
    window.close()


def category_layout():
    return [
        [sg.Text("Nombre de la categoría:")],
        [sg.Input(key="-NAME-", size=(30, 1))],
        save_cancel_buttons(),
    ]


def category_window(manager):
    def on_save(values):
        manager.add_category(values["-NAME-"])
        save_data(manager)
        sg.popup("Categoría agregada")

    run_form("Agregar categoría", category_layout(), on_save)


def movement_layout(category_names):
    return [
        labeled_input("Título:", "-TITLE-"),
        labeled_input("Monto:", "-AMOUNT-"),
        [sg.Text("Categoría:", size=(10, 1)),
         sg.Combo(category_names, default_value=category_names[0],
                key="-CATEGORY-", readonly=True, size=(23, 1))],
        save_cancel_buttons(),
    ]


def movement_window(manager, m_type):
    if not manager.categories:
        sg.popup_error("No hay categorías. Agregue una primero.")
        return

    category_names = [c.name for c in manager.categories]

    def on_save(values):
        manager.add_movement(values["-TITLE-"], values["-AMOUNT-"],
                            values["-CATEGORY-"], m_type)
        save_data(manager)
        sg.popup(f"{m_type} agregado")

    run_form(f"Agregar {m_type.lower()}", movement_layout(category_names), on_save)


def movements_table(manager):
    return sg.Table(values=movements_to_rows(manager), headings=HEADINGS,
                    key="-TABLE-", auto_size_columns=False,
                    col_widths=COL_WIDTHS, justification="left",
                    num_rows=12, expand_x=True, expand_y=True)


def totals_row():
    return [
        sg.Text("Ingresos:"), sg.Text("0.00", key="-INCOME-", size=(12, 1)),
        sg.Text("Gastos:"), sg.Text("0.00", key="-EXPENSES-", size=(12, 1)),
        sg.Text("Balance:"), sg.Text("0.00", key="-BALANCE-", size=(12, 1)),
    ]


def main_buttons():
    return [sg.Button("Agregar categoría"), sg.Button("Agregar gasto"),
            sg.Button("Agregar ingreso"), sg.Button("Salir")]


def main_layout(manager):
    return [
        [sg.Text("Gestor de Finanzas", font=("Helvetica", 16))],
        [movements_table(manager)],
        totals_row(),
        main_buttons(),
    ]


def main_window(manager):
    window = sg.Window("Gestor de Finanzas", main_layout(manager),
                    resizable=True, finalize=True)
    refresh(window, manager)

    actions = {
        "Agregar categoría": lambda: category_window(manager),
        "Agregar gasto": lambda: movement_window(manager, EXPENSE),
        "Agregar ingreso": lambda: movement_window(manager, INCOME),
    }

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
        action = actions.get(event)
        if action:
            action()
            refresh(window, manager)

    window.close()
