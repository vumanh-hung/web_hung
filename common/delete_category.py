from ketnoidb.ketnoi_mysql import create_connection

def delete_category(category_id):
    """
    Xóa danh mục theo ID
    """
    conn = create_connection()
    if conn is None:
        print("❌ Không thể kết nối đến MySQL.")
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM categories WHERE category_id = %s"
        cursor.execute(sql, (category_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có ID = {category_id}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {category_id}")

    except Exception as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        cursor.close()
        conn.close()
