from ketnoidb.ketnoi_mysql import create_connection

def get_all_categories():
    """
    Lấy danh sách tất cả danh mục từ bảng categories
    """
    conn = create_connection()
    if conn is None:
        print("❌ Không thể kết nối đến MySQL.")
        return []

    try:
        cursor = conn.cursor(dictionary=True)  # Trả về dạng dict (có tên cột)
        sql = "SELECT category_id, name, description, created_at FROM categories"
        cursor.execute(sql)
        categories = cursor.fetchall()

        if not categories:
            print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("=== 📋 DANH SÁCH DANH MỤC ===")
            for cat in categories:
                print(f"🆔 {cat['category_id']} | 📦 {cat['name']} | 📝 {cat['description'] or '(Không có mô tả)'} | ⏰ {cat['created_at']}")

        return categories

    except Exception as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []

    finally:
        cursor.close()
        conn.close()
