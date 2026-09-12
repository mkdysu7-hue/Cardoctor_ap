import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

class CarDoctorMobileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CarDoctor Mobile - فاحص سيارتك الذكي")
        
        # ضبط أبعاد النافذة لتشبه مقاسات شاشة الجوال (عمودية)
        self.root.geometry("400x700")
        self.root.config(bg="#f4f6f9")
        
        # قاعدة البيانات
        self.faults_db = []
        self.load_faults()
        
        # تصميم الواجهة
        self.create_widgets()

    def load_faults(self):
        """تحميل الأعطال من ملف faults.txt"""
        if not os.path.exists("faults.txt"):
            messagebox.showwarning("تنبيه", "ملف faults.txt غير موجود! تأكد من وجوده في نفس المجلد.")
            return
        
        try:
            with open("faults.txt", "r", encoding="utf-8") as f:
                content = f.read()
                # تقسيم الأعطال بناءً على الفواصل أو الأسطر
                fault_blocks = content.split("---")
                for block in fault_blocks:
                    if block.strip():
                        self.faults_db.append(block.strip())
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء قراءة ملف الأعطال: {e}")

    def create_widgets(self):
        # عنوان التطبيق العلوي
        header_frame = tk.Frame(self.root, bg="#1e293b", height=70)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="🚗 CarDoctor Mobile", fg="white", bg="#1e293b", font=("Arial", 16, "bold"))
        title_label.pack(pady=15)

        # منطقة البحث السريع
        search_frame = tk.Frame(self.root, bg="#f4f6f9")
        search_frame.pack(fill=tk.X, padx=15, pady=15)
        
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), justify="right")
        self.search_entry.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(5, 0))
        
        search_btn = tk.Button(search_frame, text="بحث", font=("Arial", 12, "bold"), bg="#2563eb", fg="white", command=self.search_fault)
        search_btn.pack(side=tk.LEFT)

        # شاشة العرض والنتيجة
        display_frame = tk.Frame(self.root, bg="#f4f6f9")
        display_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        
        self.result_area = scrolledtext.ScrolledText(display_frame, font=("Arial", 11), wrap=tk.WORD, bg="white")
        self.result_area.pack(fill=tk.BOTH, expand=True)
        self.result_area.insert(tk.END, "مرحباً بك في تطبيق CarDoctor!\nابحث عن أي عطل أو رمز خطأ (مثل P0300) ليعرض لك التشخيص الفوري والخطورة.")

        # أزرار التنقل السفلية (ملائمة للمس)
        footer_frame = tk.Frame(self.root, bg="#f4f6f9", height=80)
        footer_frame.pack(fill=tk.X, padx=15, pady=15)
        
        list_btn = tk.Button(footer_frame, text="عرض كل الأعطال", font=("Arial", 11, "bold"), bg="#10b981", fg="white", height=2, command=self.show_all_faults)
        list_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        clear_btn = tk.Button(footer_frame, text="مسح الشاشة", font=("Arial", 11, "bold"), bg="#ef4444", fg="white", height=2, command=self.clear_screen)
        clear_btn.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=5)

    def search_fault(self):
        query = self.search_entry.get().strip().lower()
        if not query:
            messagebox.showwarning("تنبيه", "الرجاء إدخال كلمة أو رمز للبحث عنه.")
            return
        
        self.result_area.delete(1.0, tk.END)
        found = False
        
        for fault in self.faults_db:
            if query in fault.lower():
                self.result_area.insert(tk.END, f"📌 نتيجة البحث:\n{fault}\n\n" + "="*30 + "\n\n")
                found = True
                
        if not found:
            self.result_area.insert(tk.END, f"عذراً، لم يتم العثور على نتائج تطابق: '{query}'")

    def show_all_faults(self):
        self.result_area.delete(1.0, tk.END)
        self.result_area.insert(tk.END, f"📋 قائمة جميع الأعطال المسجلة (إجمالي: {len(self.faults_db)}):\n\n" + "="*30 + "\n\n")
        for i, fault in enumerate(self.faults_db, 1):
            self.result_area.insert(tk.END, f"العطل رقم {i}:\n{fault}\n\n" + "-"*20 + "\n\n")

    def clear_screen(self):
        self.search_entry.delete(0, tk.END)
        self.result_area.delete(1.0, tk.END)
        self.result_area.insert(tk.END, "تم مسح الشاشة. جاهز لعملية بحث جديدة.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarDoctorMobileApp(root)
    root.mainloop()