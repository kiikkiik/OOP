class Cache:
    _instance = None
    _cache = {} #статический словарь для хранения данных
    # Эта переменная ОБЩАЯ для всех экземпляров класса
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def set(self, key, value):
        self._cache[key] = value  # Работаем с общей переменной _cache

    
    def get(self, key):
        return self._cache.get(key) #получение данных из кэша

    def clear(self):
        self._cache.clear()
    
    def show_all(self):
        """Метод для отладки - показывает все содержимое кэша"""
        return self._cache.copy()

# Сервис пользователей
class UserService:
    def __init__(self):
        self.cache = Cache()
    
    def get_user(self, user_id):
        # Сначала проверяем кэш
        cached_user = self.cache.get(f"user_{user_id}")
        if cached_user:
            print(f"User {user_id} found in cache")
            return cached_user
        
        # Если нет в кэше, имитируем загрузку из БД
        print(f"Loading user {user_id} from database...")
        user_data = {"id": user_id, "name": f"User{user_id}", "email": f"user{user_id}@example.com"}
        
        # Сохраняем в кэш для будущих запросов
        self.cache.set(f"user_{user_id}", user_data)
        return user_data

# Сервис заказов
class OrderService:
    def __init__(self):
        self.cache = Cache()
    
    def create_order(self, user_id, order_data):
        # Используем данные пользователя из кэша
        user_data = self.cache.get(f"user_{user_id}")
        if user_data:
            print(f"Creating order for user: {user_data['name']}")
        else:
            print(f"User {user_id} not found in cache, loading...")
            user_data = {"id": user_id, "name": f"User{user_id}"}
            self.cache.set(f"user_{user_id}", user_data)
        
        order_id = f"order_{len(self.cache._cache)}"
        order_info = {
            "order_id": order_id,
            "user": user_data,
            **order_data
        }
        
        # Сохраняем заказ в кэш
        self.cache.set(order_id, order_info)
        return order_info
    
    def get_order(self, order_id):
        return self.cache.get(order_id)

# Демонстрация работы
if __name__ == "__main__":
    print("=== Демонстрация общего кэша между сервисами ===\n")
    
    # Создаем сервисы
    user_service = UserService()
    order_service = OrderService()
    
    print("1. Получаем пользователя через UserService:")
    user1 = user_service.get_user("123")
    print(f"   Результат: {user1}\n")
    
    print("2. Создаем заказ через OrderService (использует кэшированного пользователя):")
    order1 = order_service.create_order("123", {"product": "Laptop", "price": 999})
    print(f"   Результат: {order1}\n")
    
    print("3. Проверяем, что оба сервиса работают с одним кэшем:")
    print(f"   UserService cache ID: {id(user_service.cache)}")
    print(f"   OrderService cache ID: {id(order_service.cache)}")
    print(f"   Это один и тот же объект: {user_service.cache is order_service.cache}\n")
    
    print("4. Показываем все содержимое кэша:")
    print(f"   {user_service.cache.show_all()}\n")
    
    print("5. Получаем пользователя через OrderService (должен быть в кэше):")
    cached_user = order_service.cache.get("user_123")
    print(f"   Результат: {cached_user}\n")
    
    print("6. Очищаем кэш через один сервис и проверяем в другом:")
    user_service.cache.clear()
    print(f"   Кэш после очистки: {order_service.cache.show_all()}")