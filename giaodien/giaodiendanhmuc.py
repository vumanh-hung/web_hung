import tkinter as tk
from tkinter import ttk, messagebox
from ketnoidb.ketnoi_mysql import create_connection

# ======================
# 🔧 Các hàm thao tác DB
# ======================
def get_all_categories():
    conn = create_connection()
    if conn is None:
        messagebox.showerror("Lỗi", "Không thể kết nối MySQL.")
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categories ORDER BY category_id ASC")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi lấy danh mục: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def add_category(name, description):
    conn = create_connection()
    if conn is None:
        messagebox.showerror("Lỗi", "Không thể kết nối MySQL.")
        return
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO categories (name, description) VALUES (%s, %s)"
        cursor.execute(sql, (name, description))
        conn.commit()
        messagebox.showinfo("Thành công", "✅ Đã thêm danh mục mới!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể thêm danh mục: {e}")
    finally:
        cursor.close()
        conn.close()


def update_category(category_id, name, description):
    conn = create_connection()
    if conn is None:
        messagebox.showerror("Lỗi", "Không thể kết nối MySQL.")
        return
    try:
        cursor = conn.cursor()
        sql = "UPDATE categories SET name = %s, description = %s WHERE category_id = %s"
        cursor.execute(sql, (name, description, category_id))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Thành công", "✅ Đã cập nhật danh mục!")
        else:
            messagebox.showwarning("Không tìm thấy", "⚠️ Không có danh mục nào trùng ID.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_category(category_id):
    conn = create_connection()
    if conn is None:
        messagebox.showerror("Lỗi", "Không thể kết nối MySQL.")
        return
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM categories WHERE category_id = %s"
        cursor.execute(sql, (category_id,))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Thành công", "🗑️ Đã xóa danh mục!")
        else:
            messagebox.showwarning("Không tìm thấy", "⚠️ Không có danh mục nào trùng ID.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi xóa: {e}")
    finally:
        cursor.close()
        conn.close()

# ======================
# 🖥️ Giao diện Tkinter
# ======================
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for cat in get_all_categories():
        tree.insert("", tk.END, values=(cat["category_id"], cat["name"], cat["description"], cat["created_at"]))


def on_add():
    name = entry_name.get().strip()
    desc = entry_desc.get().strip()
    if not name:
        messagebox.showwarning("Thiếu dữ liệu", "Tên danh mục không được để trống.")
        return
    add_category(name, desc)
    refresh_table()
    entry_name.delete(0, tk.END)
    entry_desc.delete(0, tk.END)


def on_update():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn 1 danh mục trong bảng để sửa.")
        return
    item = tree.item(selected[0])
    category_id = item["values"][0]
    name = entry_name.get().strip()
    desc = entry_desc.get().strip()
    update_category(category_id, name, desc)
    refresh_table()


def on_delete():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn 1 danh mục để xóa.")
        return
    item = tree.item(selected[0])
    category_id = item["values"][0]
    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa danh mục này?"):
        delete_category(category_id)
        refresh_table()


def on_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])
        entry_name.delete(0, tk.END)
        entry_name.insert(0, item["values"][1])
        entry_desc.delete(0, tk.END)
        entry_desc.insert(0, item["values"][2] if item["values"][2] else "")


# === Cửa sổ chính ===
root = tk.Tk()
root.title("💊 Quản lý Danh mục - Quầy thuốc An Khang")
root.geometry("800x500")
root.resizable(False, False)

# === Khung nhập ===
frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack(fill=tk.X)

tk.Label(frame_form, text="Tên danh mục:").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_form, width=40)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Mô tả:").grid(row=1, column=0, sticky="w")
entry_desc = tk.Entry(frame_form, width=40)
entry_desc.grid(row=1, column=1, padx=5, pady=5)

# === Nút chức năng ===
frame_buttons = tk.Frame(root)
frame_buttons.pack(fill=tk.X, pady=10)

tk.Button(frame_buttons, text="➕ Thêm", command=on_add, width=12, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="✏️ Sửa", command=on_update, width=12, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="🗑️ Xóa", command=on_delete, width=12, bg="#f44336", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="🔄 Làm mới", command=refresh_table, width=12).pack(side=tk.LEFT, padx=5)

# === Bảng hiển thị ===
cols = ("ID", "Tên danh mục", "Mô tả", "Ngày tạo")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", on_select)

# === Chạy khởi tạo ===
refresh_table()
root.mainloop()
