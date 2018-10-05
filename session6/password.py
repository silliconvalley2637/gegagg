while True:
    str = input("Nhập mật khẩu bằng số và cả chữ nhé thằng đần")
    if str.isdigit() is False and str.isalpha() is False :
        print("ok")
        break
    else:
        print("Não mày làm bằng gì vậy?")