# High-Order Functions in Python

## 1. **`map()`**
   - `map()` áp dụng một hàm cho từng phần tử trong một iterable và trả về một iterator.
   - Ví dụ:
     ```python
     numbers = [1, 2, 3, 4]
     result = map(lambda x: x ** 2, numbers)
     print(list(result))  # Output: [1, 4, 9, 16]
     ```

## 2. **`filter()`**
   - `filter()` lọc các phần tử trong iterable dựa trên một hàm kiểm tra điều kiện và trả về một iterator.
   - Ví dụ:
     ```python
     numbers = [1, 2, 3, 4, 5, 6]
     even_numbers = filter(lambda x: x % 2 == 0, numbers)
     print(list(even_numbers))  # Output: [2, 4, 6]
     ```

## 3. **`reduce()`**
   - `reduce()` (từ `functools`) giảm dần các phần tử trong iterable về một giá trị duy nhất.
   - Ví dụ:
     ```python
     from functools import reduce
     numbers = [1, 2, 3, 4]
     result = reduce(lambda x, y: x + y, numbers)
     print(result)  # Output: 10
     ```

## 4. **`lambda()`**
   - `lambda` là một hàm vô danh (anonymous function) có thể sử dụng để thực thi một biểu thức.
   - Ví dụ:
     ```python
     double = lambda x: x * 2
     print(double(5))  # Output: 10
     ```

## 5. **`functools.partial()`**
   - `partial()` tạo ra một hàm mới với một hoặc nhiều đối số được "cố định" trước, giúp tái sử dụng mã nguồn.
   - Ví dụ:
     ```python
     from functools import partial

     def multiply(x, y):
         return x * y

     double = partial(multiply, 2)  # cố định x = 2
     print(double(5))  # Output: 10
     ```

## 6. **`functools.reduce()`**
   - `reduce()` nhận một hàm và một iterable, sau đó "rút gọn" nó thành một giá trị duy nhất.
   - Ví dụ:
     ```python
     from functools import reduce

     numbers = [1, 2, 3, 4]
     result = reduce(lambda x, y: x + y, numbers)  # Cộng dồn các phần tử trong list
     print(result)  # Output: 10
     ```

## 7. **`sorted()`**
   - `sorted()` có thể nhận một hàm `key`, đó là một high-order function, giúp bạn xác định cách sắp xếp các phần tử.
   - Ví dụ:
     ```python
     people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
     sorted_people = sorted(people, key=lambda person: person[1])  # Sắp xếp theo độ tuổi
     print(sorted_people)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
     ```

## 8. **`all()` và `any()`**
   - Hai hàm này kiểm tra điều kiện của các phần tử trong một iterable và trả về kết quả boolean.
   - `all()` trả về `True` nếu tất cả các điều kiện đều đúng.
   - `any()` trả về `True` nếu ít nhất một điều kiện đúng.
   - Ví dụ:
     ```python
     nums = [1, 2, 3, 4, 5]
     print(all(x > 0 for x in nums))  # Output: True
     print(any(x < 0 for x in nums))  # Output: False
     ```

## 9. **`zip()`**
   - `zip()` kết hợp các iterable lại với nhau, giúp bạn xử lý chúng như một tập hợp các tuple.
   - Ví dụ:
     ```python
     names = ["Alice", "Bob", "Charlie"]
     ages = [25, 30, 35]
     combined = zip(names, ages)
     print(list(combined))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
     ```

## 10. **`enumerate()`**
   - `enumerate()` giúp bạn duyệt qua một iterable và lấy cả chỉ mục và giá trị của mỗi phần tử.
   - Ví dụ:
     ```python
     fruits = ["apple", "banana", "cherry"]
     for index, fruit in enumerate(fruits):
         print(index, fruit)
     # Output: 
     # 0 apple
     # 1 banana
     # 2 cherry
     ```
