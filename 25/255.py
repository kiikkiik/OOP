# Пример БЕЗ паттерна Singleton - всё дублируется
# Каждый сервис имеет свой кэш и свой код

# Кэш для пользователей (глобальная переменная)
user_cache = {}

def get_user(user_id):
    """Получить пользователя (только свой кэш)"""
    key = f"user_{user_id}"
    if key in user_cache:
        print(f"UserService: нашел пользователя {user_id} в СВОЕМ кэше")
        return user_cache[key]
    
    print(f"UserService: загружаю пользователя {user_id} из БД")
    user = {"id": user_id, "name": f"Юзер {user_id}", "email": f"user{user_id}@mail.com"}
    user_cache[key] = user
    return user

# Кэш для заказов (ДРУГАЯ глобальная переменная)
order_cache = {}

def create_order(user_id, product, price):
    """Создать заказ (только свой кэш)"""
    key = f"user_{user_id}"
    if key in order_cache:
        user = order_cache[key]
        print(f"OrderService: создаю заказ для {user['name']}")
    else:
        print(f"OrderService: пользователя {user_id} нет в МОЕМ кэше, создаю...")
        user = {"id": user_id, "name": f"Клиент {user_id}", "phone": "123-456-789"}
        order_cache[key] = user
    
    order_id = f"order_{len(order_cache)}"
    order = {"id": order_id, "user": user, "product": product, "price": price}
    order_cache[order_id] = order
    return order

# Демонстрация работы
if __name__ == "__main__":
    print("=" * 50)
    print("ПРИМЕР БЕЗ PATTERN SINGLETON")
    print("=" * 50)
    
    print("\n1. UserService получает пользователя 100:")
    user1 = get_user("100")
    print(f"   Результат: {user1}")
    
    print("\n2. OrderService создает заказ для пользователя 100:")
    order1 = create_order("100", "Ноутбук", 999)
    print(f"   Результат: {order1}")
    
    print("\n3. Смотрим что в кэшах:")
    print(f"   user_cache: {list(user_cache.keys())}")
    print(f"   order_cache: {list(order_cache.keys())}")
    
    print("\n4. Проблема №1: Дублирование данных")
    print(f"   В user_cache: user_100 = {user_cache.get('user_100')}")
    print(f"   В order_cache: user_100 = {order_cache.get('user_100')}")
    print("   Это две разные копии одного пользователя!")
    
    print("\n5. Проблема №2: Несогласованность данных")
    # Меняем пользователя только в user_cache
    if 'user_100' in user_cache:
        user_cache['user_100']['name'] = 'ИЗМЕНЕННОЕ ИМЯ'
    
    print(f"   user_cache имя: {user_cache.get('user_100', {}).get('name')}")
    print(f"   order_cache имя: {order_cache.get('user_100', {}).get('name')}")
    print("   Разные имена у одного пользователя!")
    
    print("\n6. Проблема №3: Дублирование кода")
    print("   У каждого сервиса:")
    print("   - Свой кэш (глобальная переменная)")
    print("   - Своя логика проверки кэша")
    print("   - Своя логика создания пользователя")
    
    print("\n7. Еще один заказ:")
    order2 = create_order("100", "Телефон", 500)
    print(f"   Результат: {order2}")
    print(f"   Теперь order_cache имеет: {list(order_cache.keys())}")
    
    print("\n" + "=" * 50)
    print("ИТОГ: 2 разных кэша, 2 копии одного пользователя,")
    print("данные не синхронизируются, код дублируется!")
    print("=" * 50)