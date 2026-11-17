'''Main: carga los datos y arranca la ventana principal.'''

from persistence import load_data
from interfaces import main_window


def run():
    manager = load_data()
    main_window(manager)


if __name__ == "__main__":
    run()
