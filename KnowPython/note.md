# Cơ chế import trong Python
- Khi import một module, Python sẽ tìm kiếm module đó trong các thư viện đã được cài đặt và trong thư mục hiện tại.
- Các kiểu import
```py
from module import function # Lấy 1 function trong module
from module import function as alias # Đổi tên function thành 1 alias
import module # Chỉ import module để cd đến các function
import module as alias # Đổi tên module thành 1 alias
from module import * # Import tất cả các function trong namespace
import module.function # Import 1 function trong module
```