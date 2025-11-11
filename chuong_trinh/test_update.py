from common.update_category import update_category

def main():
    print("=== 🛠️ CẬP NHẬT TÊN DANH MỤC THEO ID ===")
    try:
        # Nhập ID danh mục
        category_id = int(input("Nhập ID danh mục cần cập nhật: "))

        # Nhập tên mới
        new_name = input("Nhập tên danh mục mới: ").strip()

        # Gọi hàm cập nhật
        update_category(category_id, new_name=new_name)

    except ValueError:
        print("⚠️ Vui lòng nhập ID hợp lệ (số nguyên).")

if __name__ == "__main__":
    main()
