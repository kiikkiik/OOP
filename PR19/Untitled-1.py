class Driver:

    def __init__(self, full_name: str, experience_years: int):
        self.full_name = full_name
        self.experience_years = experience_years #стаж

    def get_full_name(self) -> str:
        # Возвращает ФИО водителя
        return f'{self.full_name}'
    
    def __str__(self) -> str:
        # Представление объекта Водитель
        return f'Водитель: ФИО "{self.full_name}", стаж {self.experience_years} лет.'
    
class Vehicle:
    
    def __init__(self, model: str, license_plate: str):
        self.model = model
        self.license_plate = license_plate

    def get_model(self) -> str:
        # Возвращает модель транспорта
        return f'{self.model}'
    
    def __str__(self) -> str:
        # Представление объекта Транспорт
        return f'Транспорт: Модель "{self.model}", гос. номер: "{self.license_plate}"'
    
class Company:
   
    def __init__(self, name: str, vehicle: Vehicle, drivers: list[Driver]):
        self.name = name
        self.vehicle = vehicle
        self.drivers = drivers

    def get_name(self) -> str:
        # Возвращает название фирмы
        return self.name

    def __str__(self) -> str:
        # Содержимое объекта Фирма: Транспорт и список Водителей
        driver_names = [d.get_full_name() for d in self.drivers]
        vehicle_info = self.vehicle.get_model()
        
        return f'Фирма "{self.name}". Транспорт: {vehicle_info} ({self.vehicle.license_plate}). Водители: ({", ".join(driver_names)})'

def main():
    # Реестр объектов Фирмы
    all_companies = []
    
    menu = '''
--- Меню Реестра Фирм ---
1. Создание нового объекта "Фирма".
2. Вывод содержимого всех объектов "Фирма" (используя __str__ Фирмы).
3. Вывод представления конкретного объекта (Фирмы, Транспорта, Водителя).
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

            # 1. Создание нового объекта
            case 1:
                print("--- Создание новой Фирмы ---")
                company_name = input("Введите название Фирмы: ").strip()
                    
                # Создание объекта Транспорт
                vehicle_model = input("Введите модель Транспорта: ").strip()
                vehicle_plate = input("Введите гос. номер Транспорта: ").strip()
                vehicle = Vehicle(vehicle_model, vehicle_plate)
                
                # Создание объектов Водителей
                drivers_input = input("Введите ФИО Водителей и их стаж (через запятую, например: Иванов И.И. 5, Петров П.П. 10): ").strip()
                drivers_data = [item.strip() for item in drivers_input.split(',')]
                
                if not drivers_data or drivers_data == ['']:
                    print("Должен быть указан хотя бы один водитель. Попробуйте ещё раз.")
                    continue
                
                drivers = [Driver(d.rsplit(' ', 1)[0], int(d.rsplit(' ', 1)[1])) for d in drivers_data]
                company = Company(company_name, vehicle, drivers)
                all_companies.append(company)
                
                print("Объект успешно создан!")
                continue

            # 2. Вывод содержимого всех объектов
            case 2:
                if not all_companies:
                    print('Нет ни одного созданного объекта "Фирма". Попробуйте для начала ввести команду 1.')
                    continue
                
                print("--- Вывод содержимого всех объектов 'Фирма' ---")
                for obj in all_companies:
                    print(obj)
                
                continue

            # 3. Вывод представления конкретного объекта
            case 3:
                idx = int(input("Введите индекс интересующей Фирмы: ").strip())
                if not (0 <= idx < len(all_companies)):
                    print("Индекс выходит за допустимый диапазон. Попробуйте ещё раз.")
                    continue
                print(f'Название фирмы: {all_companies[idx].get_name()}')
                print(f'Транспорт фирмы: {all_companies[idx].vehicle.__str__()}')
                print('Водители, работающие в фирме:')
                for driver in all_companies[idx].drivers:
                    print(driver.__str__())
                    continue
if __name__ == "__main__":
    main()