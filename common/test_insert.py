from insert_category import insert_category

def main():
    print("=== TEST THÊM DANH MỤC ===")
    # 🧩 Nhập tên danh mục từ người dùng
    name = input("Nhập tên danh mục cần thêm: ")

    # Gọi hàm thêm danh mục
    insert_category(name)

if __name__ == "__main__":
    main()
