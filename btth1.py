# Khởi tạo cấu trúc dữ liệu chính lưu trữ xe
parking_lot = []
current_id = 1

# Định nghĩa đơn giá theo giờ
PRICE_MOTORBIKE = 5000
PRICE_CAR = 10000

while True:
    # Hiển thị Menu
    print("\n" + "="*50)
    print(f"{'QUẢN LÝ BÃI XE - SMART PARKING':^50}")
    print("="*50)
    print("  1. Check-in (Đăng ký xe vào)")
    print("  2. Báo cáo tồn kho (Hiển thị danh sách)")
    print("  3. Tìm kiếm xe (Theo biển số)")
    print("  4. Check-out (Xử lý xe ra & Tính phí)")
    print("  5. Thoát chương trình")
    print("="*50)

    # Nhập lựa chọn menu
    choice_str = input("Nhập lựa chọn của bạn (1-5): ").strip()

    # Kiểm tra nhập liệu thay cho try-except
    if not choice_str.isdigit():
        print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
        continue

    choice = int(choice_str)

    # Xử lý các lựa chọn
    if choice == 1:
        # --- Check-in ---
        while True:
            plate = input("Nhập biển số xe: ").strip()
            if not plate:
                print("[Lỗi]: Biển số không được để trống!")
                continue

            # Kiểm tra trùng lặp biển số
            is_duplicate = False
            for v in parking_lot:
                if v['plate'] == plate:
                    is_duplicate = True
                    break

            if is_duplicate:
                print("[Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
                continue
            break

        while True:
            v_type_str = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
            if not v_type_str.isdigit() or int(v_type_str) not in [1, 2]:
                print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
                continue
            v_type = int(v_type_str)
            break

        while True:
            entry_time_str = input("Nhập giờ vào (0-24): ").strip()
            # isdigit() sẽ loại trừ chữ cái và cả số âm
            if not entry_time_str.isdigit() or int(entry_time_str) < 0 or int(entry_time_str) > 24:
                print("[Lỗi]: Giờ vào phải từ 0 đến 24!")
                continue
            entry_time = int(entry_time_str)
            break

        # Khởi tạo bản ghi
        vehicle = {
            'id': current_id,
            'plate': plate,
            'type': v_type,
            'entry_time': entry_time
        }
        parking_lot.append(vehicle)
        print(f"[Thành công]: Đã đăng ký xe {plate} vào bãi (ID: {current_id}).")
        current_id += 1

    elif choice == 2:
        # --- Báo cáo tồn kho ---
        if not parking_lot:
            print("[Thông báo: Bãi xe hiện đang trống!]")
        else:
            print(f"\n{'ID':<5} | {'Biển số xe':<15} | {'Loại xe':<10} | {'Giờ vào'}")
            print("-" * 55)
            for v in parking_lot:
                type_str = "Xe máy" if v['type'] == 1 else "Ô tô"
                print(f"{v['id']:<5} | {v['plate']:<15} | {type_str:<10} | {v['entry_time']}")

    elif choice == 3:
        # --- Tìm kiếm xe ---
        plate = input("Nhập biển số xe cần tìm: ").strip()
        found = False
        for v in parking_lot:
            if v['plate'] == plate:
                print(f"Thông tin chi tiết: {v}")
                found = True
                break
        if not found:
            print(f"[Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")

    elif choice == 4:
        # --- Check-out ---
        plate = input("Nhập biển số xe cần ra: ").strip()
        vehicle_idx = -1

        # Tìm xe
        for i, v in enumerate(parking_lot):
            if v['plate'] == plate:
                vehicle_idx = i
                break

        if vehicle_idx == -1:
            print(f"[Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")
        else:
            v = parking_lot[vehicle_idx]

            # Validate giờ ra
            while True:
                exit_time_str = input("Nhập giờ ra: ").strip()
                if not exit_time_str.isdigit():
                    print("[Lỗi]: Vui lòng nhập một số nguyên cho giờ ra!")
                    continue

                exit_time = int(exit_time_str)
                if exit_time < v['entry_time']:
                    print("[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
                    continue
                break

            # Tính phí
            price = PRICE_MOTORBIKE if v['type'] == 1 else PRICE_CAR
            fee = (exit_time - v['entry_time']) * price
            print(f"Tổng phí phải trả: {fee} VNĐ")

            # Xóa khỏi danh sách
            del parking_lot[vehicle_idx]
            print(f"[Thành công]: Đã xóa xe ID {v['id']} thành công!")

    elif choice == 5:
        # --- Thoát ---
        print("Đã thoát chương trình.")
        break

    else:
        print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
