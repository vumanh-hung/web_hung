import mysql.connector
from mysql.connector import Error

def create_connection():
    """Tạo kết nối đến MySQL Database"""
    try:
        connection = mysql.connector.connect(
            host='localhost',       # Địa chỉ server MySQL (VD: '127.0.0.1')
            user='root',            # Tên user MySQL
            password='',            # Mật khẩu MySQL
            database='qlithuoc_ankhang'  # Tên database cần kết nối
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print(f"❌ Lỗi khi kết nối MySQL: {e}")
        return None
