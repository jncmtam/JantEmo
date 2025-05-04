# Python Decorators in OOP

## 1. **`@property`**

Decorator `@property` biến một phương thức thành một thuộc tính của class. Nó cho phép bạn gọi phương thức như thể đó là một thuộc tính thông thường.

### Cách sử dụng:
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person("John", 25)
print(p.age)   # Output: 25
p.age = 30     # Set age
print(p.age)   # Output: 30
```
## 2. **@staticmethod**
- Decorator `@staticmethod` dùng để biến một phương thức thành phương thức tĩnh. Phương thức này có thể được gọi mà không cần tạo một instance của class.
### Cách sử dụng
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 3))  # Output: 8
```
## 3. **@classmethod**
Decorator `@classmethod` dùng để biến một phương thức thành phương thức của class, thay vì phương thức của instance. Phương thức này nhận `cls` (class) làm đối số đầu tiên thay vì `self` (instance).
### Cách sử dụng
```python
class Car:
    wheels = 4

    @classmethod
    def number_of_wheels(cls):
        return cls.wheels

print(Car.number_of_wheels())  # Output: 4
```
## 4. **@property & @setter**
- Kết hợp giữa `@property` và `@setter` cho phép bạn không chỉ truy cập và thay đổi thuộc tính như một thuộc tính thông thường, mà còn kiểm soát được hành vi của việc thay đổi giá trị đó.
### Cách sử dụng
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person("John", 25)
print(p.age)   # Output: 25
p.age = 30     # Set age
print(p.age)   # Output: 30
```
## 5. **@abstractmethod**
- Decorator `@abstractmethod`được sử dụng trong các lớp abstract để khai báo các phương thức bắt buộc phải được cài đặt trong các lớp kế thừa. Bạn cần sử dụng ABC class từ abc module.
### Cách sử dụng
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

dog = Dog()
print(dog.make_sound())  # Output: Woof!
```
## 6. **@functools.lru_cache**
Decorator `@lru_cache` từ module functools giúp tăng hiệu suất bằng cách lưu trữ kết quả của các hàm đệ quy để không phải tính toán lại khi gọi với cùng một đối số.
### Cách sử dụng
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Output: 55
```
## 7. **@wraps**
`functools.wraps` là một decorator đặc biệt trong Python giúp đảm bảo rằng các thuộc tính như `tên hàm` `(__name__)`, `docstring` `(__doc__)`, và các thuộc tính khác của hàm gốc được giữ nguyên khi hàm đó được trang trí.

Khi bạn sử dụng decorator, hàm trang trí (wrapper) sẽ thay thế hàm gốc trong bộ nhớ. Điều này có thể dẫn đến việc mất đi thông tin quan trọng của hàm gốc, ví dụ như tên hàm và docstring. Để tránh điều này, chúng ta sử dụng wraps để sao chép tất cả các thuộc tính của hàm gốc sang hàm wrapper.
### Ví dụ :
```python
from functools import wraps

def log_time(func):
    @wraps(func)  # Giữ nguyên thông tin của hàm gốc
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is running")  # In tên hàm
        return func(*args, **kwargs)
    return wrapper

@log_time
def my_function():
    print("Doing something")

print(my_function.__name__)  # Kết quả: 'my_function'
```