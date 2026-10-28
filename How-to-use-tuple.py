#Viết chương trình nhận vào hai số nguyên a, b từ bàn phím. In ra tổng, hiệu, tích, phần nguyên, phần dư và kết quả chia thực của phép chia a cho b (lấy đến 2 chữ số phần thập phân) theo định dạng đúng của output

import math
def tinhtoan (a,b):
    return tuple ([a+b,
                   a-b,
                   a*b,
                   a//b,
                   a%b,
                   a/b
                   ])
input_values = input().split()
a,b = map(int, input_values)
results = tinhtoan (a,b)
print(results[0])
print(results[1])
print(results[2])
print(results[3])
print(results[4])
print(f"{results[5]:.2f}")


