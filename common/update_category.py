from ketnoidb.ketnoi_mysql import create_connection

def update_category(category_id, new_name=None, new_description=None):
    """
    Cập nhật thông tin danh mục theo ID.
    Có thể cập nhật tên (name) và/hoặc mô tả (description).
    """

    conn = create_connection()
    if conn is None:
        print("❌ Không thể kết nối đến MySQL.")
        return

    try:
        cursor = conn.cursor()

        # Tạo danh sách cột cần cập nhật động
        fields = []
        values = []

        if new_name is not None:
            fields.append("name = %s")
            values.append(new_name)
        if new_description is not None:
            fields.append("description = %s")
            values.append(new_description)

        if not fields:
            print("⚠️ Không có thông tin nào để cập nhật.")
            return

        sql = f"UPDATE categories SET {', '.join(fields)} WHERE category_id = %s"
        values.append(category_id)

        cursor.execute(sql, tuple(values))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có ID = {category_id}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {category_id}")

    except Exception as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)

    finally:
        cursor.close()
        conn.close()
