class Transport:
    '''Абстрактный класс для транспортных средств'''

    def __init__(self, model: str, vehicle_type: str):
        self.model = model
        self.vehicle_type = vehicle_type

    def get_info(self) -> tuple[str, str]:
        return (self.model, self.vehicle_type)

    def __str__(self) -> str:
        '''Метод который должен быть переопределён каждым наследником'''
        pass

class Bus(Transport):

    def __init__(self, model: str, capacity: int):
        super().__init__(model=model, vehicle_type='автобус')
        self.capacity = capacity
        
    def __str__(self) -> str:
        '''Реализация абстрактного метода для автобуса'''
        return f'Тип: {self.vehicle_type}, Модель: {self.model}, Вместимость: {self.capacity} пасс.'
#вместимоть
   
class Train(Transport):

    def __init__(self, model: str, carriages: int):
        super().__init__(model=model, vehicle_type='поезд')
        self.carriages = carriages
    
    def __str__(self) -> str:
        '''Реализация абстрактного метода для поезда'''
        return f'Тип: {self.vehicle_type}, Модель: {self.model}, Вагонов: {self.carriages}.'
#вагоны

class Airplane(Transport):

    def __init__(self, model: str, flight_range: int):
        super().__init__(model=model, vehicle_type='самолёт')
        self.flight_range = flight_range
    
    def __str__(self) -> str:
        '''Реализация абстрактного метода для самолёта'''
        return f'Тип: {self.vehicle_type}, Модель: {self.model}, Дальность полёта: {self.flight_range} км.'
#дальность

class TransportCompany:

    def __init__(self, vehicle: Transport, drivers: list, name: str):
        self.vehicle = vehicle
        self.drivers = drivers
        self.name = name

    def __str__(self) -> str:
        drivers_names = [d.get_info()[0] for d in self.drivers]
        return f'Фирма: "{self.name}". Транспорт: {self.vehicle.get_info()[0]}. Водители: ({", ".join(drivers_names)})'
#способность работать с любым видом транспорта благодаря полиморфизму

def main():
    all_objects = []
    menu = '''
    1. Создание нового объекта "TransportCompany".
    2. Вывод объектов.
    3. Вывод конкретного объекта.
    0. Завершение работы программы.
    '''

    while True:
        print(menu)
        menu_item = int(input("Введите номер команды: ").strip())

        if not (0 <= menu_item <= 4):
            print("Вы ввели неверную команду, попробуйте ещё раз.")
            continue
        
        match menu_item:
            case 0:
                print("Программа завершила свою работу.")
                break

            case 1:
                company_name = input("Введите название Фирмы: ").strip()
                vehicle_model = input("Введите модель Транспорта: ").strip()
                vehicle_plate = input("Введите гос. номер Транспорта: ").strip()
                drivers_input = input("Введите ФИО Водителей и их стаж (через запятую, например: Иванов И.И. 5, Петров П.П. 10): ").strip().split(', ')
                
                if len(drivers_input) == 0:
                    print("Должен быть указан хотя бы один водитель. Попробуйте ещё раз.")
                    continue
                drivers = [Driver(d.rsplit(' ', 1)[0], int(d.rsplit(' ', 1)[1])) for d in drivers_input]
                vehicle = Vehicle(vehicle_model, vehicle_plate)
                company = Company(company_name, vehicle, drivers)
                all_companies.append(company)
                print("Объект успешно создан!")
                continue

            case 2:
                if len(all_objects) == 0:
                    print('Нет ни одного созданного объекта. Попробуйте для начала ввести команду 1.')
                    continue
                
                print("Вывод содержимого всех объектов.")
                for obj in all_objects:
                    print(obj)
                
                continue

            case 3:
                idx = int(input("Введите индекс интересующего объекта: ").strip())

                if not(0 <= idx < len(all_objects)):
                    print("Индекс выходит за допустимый диапазон. Попробуйте ещё раз.")
                    continue
                    
                print(f'Название фирмы: {all_objects[idx].name}')
                print(f'Транспорт:')
                print(f'{all_objects[idx].vehicle.__str__()}')
                print('Водители:')
                for driver in all_objects[idx].drivers:
                    print(driver.__str__())
                
                continue

# Дополнительный класс для водителей 
class Driver:
    def __init__(self, name: str, experience: int):
        self.name = name
        self.experience = experience

    def get_info(self) -> tuple[str, int]:
        return (self.name, self.experience)

    def __str__(self) -> str:
        return f'Водитель: {self.name}, Стаж: {self.experience} лет.'
                
if __name__ == "__main__":
    main()

#bus_company = TransportCompany(Bus("Mercedes", 50), drivers, "Автобусные перевозки")
#train_company = TransportCompany(Train("Сапсан", 10), drivers, "Железнодорожные перевозки")  
#airplane_company = TransportCompany(Airplane("Boeing 737", 5000), drivers, "Авиаперевозки")


#companies = [bus_company, train_company, airplane_company]
#for company in companies:
#print(company.vehicle)