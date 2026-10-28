#Hàm input() trong Python là một hàm dùng để nhận dữ liệu từ người dùng thông qua bàn phím, hàm này luôn trả về dữ liệu kiểu chuỗi(str).Viết chương trình nhận đầu vào là tên người từ bàn phím và in ra màn hình lời chào tương ứng.

def loi_chao(ten):
    return (f"Hello {ten}!")
ten = input().strip()
print(loi_chao(ten))