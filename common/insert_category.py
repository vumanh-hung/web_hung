from ketnoidb.ketnoi_mysql import create_connection

def insert_category(name):
    conn = create_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO categories (name) VALUES (%s)"
        cursor.execute(sql, (name,))
        conn.commit()
        print(f"✅ Đã thêm danh mục: {name}")
    except Exception as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        cursor.close()
        conn.close()

# ---- Test thử ----
if __name__ == "__main__":
    insert_category("Laptop Gaming")
