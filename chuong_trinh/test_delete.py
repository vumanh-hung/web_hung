from common.delete_category import delete_category

def main():
    print("=== TEST XÓA DANH MỤC ===")
    category_id = input("Nhập ID danh mục cần xóa: ")
    if category_id.isdigit():
        delete_category(int(category_id))
    else:
        print("⚠️ ID phải là số nguyên!")

if __name__ == "__main__":
    main()
