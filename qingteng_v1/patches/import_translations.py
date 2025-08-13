import frappe
import csv
def execute():
    path = frappe.get_app_path("qingteng_v1","public","translations.csv")
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["语言"] and row["源文本"] and row["已翻译文本"]:
                frappe.get_doc({
                    "doctype": "Translation",
                    "language": row["语言"],
                    "source_text": row["源文本"],
                    "translated_text": row["已翻译文本"]
                }).insert(ignore_permissions=True,ignore_if_duplicate=True)
