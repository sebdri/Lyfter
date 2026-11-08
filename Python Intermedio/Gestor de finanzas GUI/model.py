from datetime import date, datetime

#---Constantes---
DATE_FORMAT = "%d/%m/%Y"
INCOME = 'Ingreso'
EXPENSE = 'Gasto'







#Clases 

class Category:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {'Name': self.name}


    @classmethod
    def from_dict(cls,data):
        return cls(data["Name"])

    def __str__(self):
        return self.name










class Movement:
    def __init__(self, title, amount, category, m_type, date ):
        self.title = title
        self.amount = amount
        self.category = category
        self.m_type = m_type
        self.date = date


    def to_dict(self):
            return {'Title': self.title,
                    'Amount': self.amount,
                    'Category': self.category,
                    'Type': self.m_type,
                    'Date': self.date.strftime(DATE_FORMAT)
                    }
                    
    

    @classmethod
    def from_dict(cls,data):
        fecha = datetime.strptime(data["Date"], DATE_FORMAT).date()
        return cls(data["Title"],data["Amount"],data["Category"],data["Type"],fecha)
        
    def __str__(self):
        return f'{self.title} | {self.amount} | {self.category} | {self.m_type} | {self.date}'








if __name__ == "__main__":
    categoria = Category("Comida")
    datos_categoria = categoria.to_dict()
    print(datos_categoria)
    print(Category.from_dict(datos_categoria))

    mov = Movement("Salario", 1000, "Trabajo", INCOME, date.today())
    datos_mov = mov.to_dict()
    print(datos_mov)
    print(Movement.from_dict(datos_mov))