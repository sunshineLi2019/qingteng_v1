import frappe
import os
from frappe.utils.file_manager import save_file

def execute():
    # 获取 app 路径
    app_path = os.path.dirname(__file__)
    public_path = os.path.abspath(os.path.join(app_path, "..", "public"))
    logo_path = os.path.join(public_path, "logo.png")

    if not os.path.exists(logo_path):
        print(f"⚠️ No logo.png found at {logo_path}")
        return

    # 打开文件
    with open(logo_path, "rb") as f:
        content = f.read()

    # 检查是否已存在 logo 文件
    existing_file = frappe.get_all(
        "File",
        filters={
            "attached_to_doctype": "Website Settings",
            "attached_to_name": "Website Settings",
            "file_name": "logo.png"
        },
        limit_page_length=1
    )

    if existing_file:
        # 覆盖已有文件
        file_doc = frappe.get_doc("File", existing_file[0].name)
        file_doc.data = content
        file_doc.save(ignore_permissions=True)
        print("✅ Logo updated")
    else:
        # 创建新文件
        file_doc = frappe.get_doc({
            "doctype": "File",
            "file_name": "logo.png",
            "attached_to_doctype": "Website Settings",
            "attached_to_name": "Website Settings",
            "content": content,
            "is_private": 0
        })
        file_doc.save(ignore_permissions=True)
        print("✅ Logo created")

    frappe.db.commit()

