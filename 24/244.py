# ========== ГЛОБАЛЬНЫЙ КЭШ (Singleton) ==========
_cache = {}  # Это наш "одиночка" - единственный экземпляр данных

def set_to_cache(key, value):
    """Сохранить в кэш"""
    _cache[key] = value

def get_from_cache(key):
    """Получить из кэша"""
    return _cache.get(key)  # Вернет None если ключа нет

def clear_cache():
    """Очистить кэш"""
    _cache.clear()

# ========== ПРОЦЕДУРНЫЕ СЕРВИСЫ ==========
def get_user(user_id):
    """Получить пользователя"""
    # Проверяем кэш
    cached_user = get_from_cache(f"user_{user_id}")
    if cached_user:
        print(f"Пользователь {user_id} найден в кэше")
        return cached_user
    
    # Если нет в кэше - загружаем
    print(f"Загружаем пользователя {user_id} из БД...")
    user_data = {
        "id": user_id,
        "name": f"Пользователь {user_id}",
        "email": f"user{user_id}@mail.com"
    }
    
    # Сохраняем в кэш
    set_to_cache(f"user_{user_id}", user_data)
    return user_data

def create_order(user_id, product, price):
    """Создать заказ"""
    # Используем кэшированного пользователя
    user_data = get_from_cache(f"user_{user_id}")
    if not user_data:
        print(f"Пользователь {user_id} не в кэше, загружаем...")
        user_data = get_user(user_id)
    
    print(f"Создаем заказ для: {user_data['name']}")
    
    order_id = f"order_{len(_cache)}"
    order = {
        "id": order_id,
        "user": user_data,
        "product": product,
        "price": price
    }
    
    # Сохраняем заказ в кэш
    set_to_cache(order_id, order)
    return order

# ========== ИСПОЛЬЗОВАНИЕ ==========
if __name__ == "__main__":
    print("=== Процедурный Singleton (общий кэш) ===\n")
    
    print("1. Получаем пользователя:")
    user = get_user("123")
    print(f"   Результат: {user}\n")
    
    print("2. Создаем заказ (использует кэшированного пользователя):")
    order = create_order("123", "Ноутбук", 999)
    print(f"   Результат: {order}\n")
    
    print("3. Показываем весь кэш:")
    print(f"   {_cache}\n")
    
    print("4. Получаем те же данные через разные вызовы:")
    user_from_cache = get_from_cache("user_123")
    print(f"   Пользователь из кэша: {user_from_cache}\n")
    
    print("5. Очищаем кэш:")
    clear_cache()
    print(f"   Кэш после очистки: {_cache}")