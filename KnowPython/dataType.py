# Kiểu dữ liệu trong Python
a = 1 # int
b = 1.5 # float

# Kiểu chuỗi
c = "Hello world" # str

# Kiểu danh sách (CRUD
d = [1, 2, 3] # C list
d.append("4") # U Thêm phần tử vào list
d[0] = 5 # U Thay đổi giá trị của phần tử trong list
d.remove("4") # D Xóa phần tử khỏi list

# Kiểu tuple: Giống list nhưng không thể thực hiện CRUD index
e = (1, 2, 3) # tuple
del e # Xóa tuple

# Kiểu từ điển (dictionary): Là kiểu dữ liệu lưu trữ cặp key-value
f = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
f["name"] = "Jane" # Thay đổi giá trị của key
f["country"] = "USA" # Thêm key-value mới vào từ điển
del f["age"] # Xóa key-value khỏi từ điển

# Kiểu tập hợp (set): Là kiểu dữ liệu không có thứ tự và không có phần tử trùng lặp
g = {1, 2, 3, 4, 5} # set
g.add(6) # Thêm phần tử vào tập hợp
g.remove(1) # Xóa phần tử khỏi tập hợp

# Kiểu boolean: Là kiểu dữ liệu chỉ có 2 giá trị True và False
h = True # bool
h1 = False # bool

# Kiểu None: Là kiểu dữ liệu không có giá trị
i = None # None

# Kiểu byte: Là kiểu dữ liệu nhị phân
j = b"Hello world" # byte








# TỔng kết
a1 = 1 # int
a2 = 1.5 # float
a3 = "Hello world" # str
a4 = [1, 2, 3] # list
a5 = (1, 2, 3) # tuple
a6 = {
    "name": "John",
    "age": 30,
    "city": "New York"
} # dict
a7 = {1, 2, 3, 4, 5} # set
a8 = True # bool
a9 = False # bool
a10 = None # None
a11 = b"Hello world" # byte