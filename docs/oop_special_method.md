# Python Special Methods (Magic / Dunder Methods)

---

## 📌 1. Khởi tạo & Biểu diễn đối tượng

| Method       | Mục đích                               | Có sẵn / Cần implement |
| ------------ | -------------------------------------- | ---------------------- |
| `__init__`   | Khởi tạo đối tượng                     | Cần implement          |
| `__new__`    | Tạo đối tượng trước khi `__init__` gọi | Cần implement          |
| `__del__`    | Hủy đối tượng                          | Có sẵn                 |
| `__str__`    | Chuỗi thân thiện (in ra)               | Cần implement          |
| `__repr__`   | Chuỗi chính xác, dùng cho debug        | Cần implement          |
| `__format__` | Format chuỗi (`format()`)              | Cần implement          |

---

## 📌 2. So sánh

| Method   | Mô tả | Có sẵn / Cần implement |
| -------- | ----- | ---------------------- |
| `__eq__` | `==`  | Cần implement          |
| `__ne__` | `!=`  | Cần implement          |
| `__lt__` | `<`   | Cần implement          |
| `__le__` | `<=`  | Cần implement          |
| `__gt__` | `>`   | Cần implement          |
| `__ge__` | `>=`  | Cần implement          |

---

## 📌 3. Toán tử số học

| Method         | Toán tử | Có sẵn / Cần implement |
| -------------- | ------- | ---------------------- |
| `__add__`      | `+`     | Cần implement          |
| `__sub__`      | `-`     | Cần implement          |
| `__mul__`      | `*`     | Cần implement          |
| `__truediv__`  | `/`     | Cần implement          |
| `__floordiv__` | `//`    | Cần implement          |
| `__mod__`      | `%`     | Cần implement          |
| `__pow__`      | `**`    | Cần implement          |
| `__neg__`      | `-obj`  | Cần implement          |

✅ Gồm cả: `__iadd__`, `__isub__`, v.v. cho các phép gán mở rộng.

---

## 📌 4. Indexing và Container Behavior

| Method         | Mô tả                         | Có sẵn / Cần implement |
| -------------- | ----------------------------- | ---------------------- |
| `__len__`      | `len(obj)`                    | Cần implement          |
| `__getitem__`  | `obj[key]`                    | Cần implement          |
| `__setitem__`  | `obj[key] = value`            | Cần implement          |
| `__delitem__`  | `del obj[key]`                | Cần implement          |
| `__contains__` | `x in obj`                    | Cần implement          |
| `__iter__`     | Lặp qua đối tượng             | Cần implement          |
| `__next__`     | Trả phần tử tiếp theo khi lặp | Cần implement          |

---

## 📌 5. Callable, Context, Attribute

| Method             | Mô tả                           | Có sẵn / Cần implement |
| ------------------ | ------------------------------- | ---------------------- |
| `__call__`         | Gọi object như một hàm          | Cần implement          |
| `__enter__`        | `with` block bắt đầu            | Cần implement          |
| `__exit__`         | `with` block kết thúc           | Cần implement          |
| `__getattr__`      | Khi truy cập attr không tồn tại | Cần implement          |
| `__getattribute__` | Bắt mọi truy cập attribute      | Cần implement          |
| `__setattr__`      | Khi gán attribute               | Cần implement          |
| `__delattr__`      | Khi xóa attribute               | Cần implement          |
| `__dir__`          | Kết quả của `dir(obj)`          | Có sẵn                 |

---

## 📌 6. Hashing và Boolean

| Method     | Mô tả                                    | Có sẵn / Cần implement |
| ---------- | ---------------------------------------- | ---------------------- |
| `__hash__` | Cho phép sử dụng trong `set`, `dict`     | Cần implement          |
| `__bool__` | Giá trị `True/False` khi gọi `bool(obj)` | Cần implement          |

---

## 📌 7. Class & Meta Information

| Method           | Mô tả                     | Có sẵn / Cần implement |
| ---------------- | ------------------------- | ---------------------- |
| `__class__`      | Truy cập class của object | Có sẵn                 |
| `__mro__`        | Method Resolution Order   | Có sẵn                 |
| `__bases__`      | Các class cha             | Có sẵn                 |
| `__subclasses__` | Lấy danh sách subclass    | Có sẵn                 |

---
