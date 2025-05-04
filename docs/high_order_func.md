Dưới đây là nội dung đã được định dạng lại theo chuẩn **Markdown** để bạn dễ dàng copy và sử dụng:

---

# Python: Hàm lambda và các hàm xử lý iterable

## 1. `lambda` Function

`lambda` là một cách viết hàm ngắn gọn, không cần định nghĩa đầy đủ với `def`.

**Ví dụ:**

```python
# Ví dụ về hàm lambda
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

---

## 2. `filter()` Function

`filter()` được dùng để lọc các phần tử trong một iterable (như list, tuple) theo một điều kiện.

**Cú pháp:**

```python
filter(function, iterable)
```

* `function`: Hàm trả về `True` hoặc `False`.
* `iterable`: Danh sách, tuple, v.v.

**Ví dụ:**

```python
# Ví dụ sử dụng filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]
```

---

## 3. `map()` Function

`map()` áp dụng một hàm cho mỗi phần tử trong iterable.

**Cú pháp:**

```python
map(function, iterable)
```

* `function`: Hàm áp dụng cho mỗi phần tử.
* `iterable`: Danh sách, tuple, v.v.

**Ví dụ:**

```python
# Ví dụ sử dụng map
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
```

---

## 4. `reduce()` Function

`reduce()` thuộc module `functools`, dùng để rút gọn một iterable thành một giá trị duy nhất.

**Cú pháp:**

```python
from functools import reduce
reduce(function, iterable)
```

* `function`: Hàm áp dụng liên tục.
* `iterable`: Danh sách, tuple, v.v.

**Ví dụ:**

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
```

---

## 5. `zip()` Function

`zip()` kết hợp các iterable lại với nhau thành một iterable mới. Mỗi phần tử là một tuple chứa giá trị tương ứng từ các iterable đầu vào.

**Cú pháp:**

```python
zip(iterable1, iterable2, ...)
```

**Ví dụ:**

```python
# Ví dụ sử dụng zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = zip(names, ages)
print(list(combined))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

---

## 6. List Comprehension

List Comprehension là cách viết ngắn gọn để tạo danh sách mới từ danh sách đã có, có thể kèm điều kiện.

**Cú pháp:**

```python
[expression for item in iterable if condition]
```

**Ví dụ:**

```python
# Ví dụ về list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

---

## Tổng kết

* ✅ `lambda`: Tạo hàm ngắn gọn.
* ✅ `filter()`: Lọc phần tử theo điều kiện.
* ✅ `map()`: Áp dụng hàm lên từng phần tử.
* ✅ `reduce()`: Rút gọn iterable thành một giá trị.
* ✅ `zip()`: Kết hợp nhiều iterable thành tuple.
* ✅ List Comprehension: Tạo danh sách ngắn gọn và hiệu quả.

---

