atm_vault_balance = 50000000      
user_account_balance = 10000000   

def display_balances():
    """
    Chức năng 1: Xem số dư tài khoản và số dư ATM phục vụ debug.

    Hàm này sẽ in ra màn hình số dư hiện tại trong tài khoản của người dùng 
    và số lượng tiền mặt còn lại bên trong khay chứa của cây ATM.

    Đối số:
        None

    Trả về:
        None: Hàm này chỉ in thông tin ra màn hình, không trả về giá trị.
    """
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")

def deposit_money(amount):
    """
    Chức năng 2: Nạp tiền vào tài khoản.

    Hàm kiểm tra tính hợp lệ của số tiền nạp (phải lớn hơn 0). Nếu hợp lệ, 
    hàm sử dụng từ khóa `global` để cập nhật cộng thêm tiền vào cả tài khoản 
    người dùng và khay chứa tiền của cây ATM.

    Đối số:
        amount (int): Số tiền khách hàng muốn nạp vào hệ thống.

    Trả về:
        bool: Trả về True nếu nạp tiền thành công, ngược lại trả về False.
    """
    global user_account_balance, atm_vault_balance
    if amount <= 0:
        print("Số tiền không hợp lệ")
        return False
    user_account_balance += amount
    atm_vault_balance += amount
    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
    return True

def check_withdrawal_rules(amount):
    """
    Kiểm tra các điều kiện và luật rút tiền từ tài khoản và cây ATM.

    Hàm này thực hiện tính toán chi phí rút tiền cố định (1,100 VND) và 
    tổng số tiền thực tế sẽ bị trừ khỏi tài khoản của khách hàng. Sau đó,
    hàm đối chiếu với số dư tài khoản và số tiền mặt hiện có trong ATM 
    để quyết định giao dịch có hợp lệ hay không.

    Đối số:
        amount (int): Số tiền khách hàng yêu cầu rút từ bàn phím.

    Trả về:
        str: Trạng thái của giao dịch, bao gồm một trong ba giá trị:
             - "INSUFFICIENT_FUNDS": Tổng tiền trừ vượt quá số dư tài khoản khách.
             - "ATM_OUT_OF_CASH": Số tiền rút vượt quá số tiền mặt có sẵn trong ATM.
             - "OK": Thỏa mãn tất cả các điều kiện, sẵn sàng rút tiền.
    """
    fee = 1100
    total_deduction = amount + fee
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    return "OK"

def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Thực hiện trừ tiền vào hệ thống và in biên lai giao dịch thành công.

    Hàm này sử dụng từ khóa `global` để trực tiếp cập nhật và thay đổi giá trị
    of hai biến toàn cục lưu trữ số dư. Sau khi trừ tiền thành công, hàm sẽ
    in ra màn hình các thông tin chi tiết của giao dịch dưới dạng biên lai hóa đơn.

    Đối số:
        total_deduction (int): Tổng số tiền bị trừ ở tài khoản khách (Tiền rút + Phí).
        amount_to_dispense (int): Số tiền mặt thực tế máy ATM sẽ chi trả cho khách.

    Trả về:
        None: Hàm này chỉ cập nhật dữ liệu hệ thống và in thông tin, không trả về giá trị.
    """
    global user_account_balance, atm_vault_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")

def main():
    """
    Hàm điều khiển chính (Luồng xử lý trung tâm) của chương trình SMART ATM.

    Hàm khởi chạy một vòng lặp vô hạn để hiển thị Menu chức năng cho người dùng. 
    Nó tiếp nhận lựa chọn (1-4), bắt các ngoại lệ dữ liệu đầu vào (ValueError) và 
    gọi các hàm xử lý logic tương ứng (Xem số dư, Nạp tiền, Rút tiền). Vòng lặp 
    chỉ kết thúc khi người dùng chọn chức năng số 4.

    Đối số:
        None

    Trả về:
        None
    """
    while True:
        print("\n================ SMART ATM ================")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("===========================================")
        
        choice = input("Vui lòng chọn giao dịch (1-4): ")
        
        match choice:
            case "1":
                display_balances()
                
            case "2":
                print("\n--- NẠP TIỀN ---")
                try:
                    amount = int(input("Nhập số tiền muốn nạp: "))
                    deposit_money(amount)
                except ValueError:
                    print("Vui lòng nhập một số nguyên hợp lệ!")
                    
            case "3":
                print("\n--- RÚT TIỀN ---")
                try:
                    amount = int(input("Nhập số tiền cần rút: "))
                    if amount <= 0:
                        print("Số tiền không hợp lệ")
                        continue
                    if amount % 50000 != 0:
                        print("Số tiền rút phải là bội số của 50,000")
                        continue
                    
                    status = check_withdrawal_rules(amount)
                    
                    match status:
                        case "INSUFFICIENT_FUNDS":
                            print("Giao dịch thất bại: Số dư tài khoản không đủ.")
                        case "ATM_OUT_OF_CASH":
                            print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                        case "OK":
                            fee = 1100
                            total_deduction = amount + fee
                            execute_withdrawal(total_deduction, amount)
                            
                except ValueError:
                    print("Vui lòng nhập một số nguyên hợp lệ!")
                    
            case "4":
                print("\nCảm ơn quý khách đã sử dụng dịch vụ!")
                break
                
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()
