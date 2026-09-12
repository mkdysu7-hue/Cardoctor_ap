import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog

def load_faults():
    try:
        with open("faults.txt", "r", encoding="utf-8") as file:
            content = file.read()
        raw_faults = content.split("[رقم العطل:")
        faults_list = []
        for item in raw_faults:
            if item.strip():
                faults_list.append("[رقم العطل:" + item.strip())
        return faults_list
    except FileNotFoundError:
        return []

def search_fault(query_text=None):
    if query_text:
        entry_query.delete(0, tk.END)
        entry_query.insert(0, query_text)
    
    query = entry_query.get().strip().lower()
    if not query:
        messagebox.showwarning("تنبيه", "الرجاء إدخال كلمة للبحث أو اختيار قسم من الأزرار!")
        return
        
    faults = load_faults()
    if not faults:
        messagebox.showerror("خطأ", "ملف faults.txt غير موجود أو فارغ!")
        return
        
    results = []
    for fault in faults:
        if query in fault.lower():
            results.append(fault)
            
    text_result.config(state=tk.NORMAL)
    text_result.delete("1.0", tk.END)
    
    if results:
        text_result.insert(tk.END, f"تم العثور على {len(results)} نتيجة مطابقة لـ '{query}':\n\n" + "="*50 + "\n\n")
        for r in results:
            # إضافة نظام تصنيف الخطورة بصرياً بناءً على الكلمات المفتاحية
            severity = "🟢 عطل بسيط (آمن القيادة)"
            color_tag = "green"
            
            r_lower = r.lower()
            if any(w in r_lower for w in ["حرارة", "فرامل", "مكابح", "محرك", "زيت المحرك", "انفجار", "توقف مفاجئ"]):
                severity = "🔴 عطل خطير جداً (توقف عن القيادة فوراً!)"
                color_tag = "red"
            elif any(w in r_lower for w in ["بطارية", "شحن", "دينامو", "قير", "ناقل الحركة", "مكيف"]):
                severity = "🟠 عطل متوسط (يحتاج فحص قريباً)"
                color_tag = "orange"
                
            text_result.insert(tk.END, f"مستوى الخطورة: {severity}\n")
            text_result.insert(tk.END, r + "\n\n" + "-"*50 + "\n\n")
    else:
        text_result.insert(tk.END, f"عذراً، لم يتم العثور على أي عطل مطابق لـ '{query}'. حاول استخدام كلمات أخرى.")
        
    text_result.config(state=tk.DISABLED)

# دالة حفظ النتائج في ملف نصي
def save_report():
    text_content = text_result.get("1.0", tk.END).strip()
    if not text_content or "أهلاً بك!" in text_content or "لم يتم العثور" in text_content:
        messagebox.showwarning("تنبيه", "لا توجد نتائج مطابقة أو صحيحة لحفظها كتقرير!")
        return
        
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        initialfile="CarDoctor_Report.txt"
    )
    
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text_content)
            messagebox.showinfo("نجاح", "تم حفظ التقرير بنجاح في جهازك!")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الحفظ: {e}")

# واجهة المستخدم الرسومية (GUI)
root = tk.Tk()
root.title("دكتور السيارات الاحترافي - CarDoctor v2")
root.geometry("800x740")
root.config(bg="#f8f9fa")

# العنوان الرئيسي
title_label = tk.Label(root, text="🚗 نظام CarDoctor الذكي لتشخيص أعطال السيارات (مع تحديد الخطورة)", font=("Arial", 13, "bold"), bg="#f8f9fa", fg="#2c3e50")
title_label.pack(pady=10)

# إطار التصنيفات والأزرار الشاملة
frame_quick = tk.LabelFrame(root, text=" تصنيفات الأعطال الشاملة (اضغط للبحث الفوري) ", font=("Arial", 10, "bold"), bg="#f8f9fa", fg="#c0392b")
frame_quick.pack(pady=5, padx=15, fill=tk.X)

# الصف الأول من الأزرار
row1 = tk.Frame(frame_quick, bg="#f8f9fa")
row1.pack(pady=4, fill=tk.X)

tk.Button(row1, text="🔥 حرارة", font=("Arial", 9, "bold"), bg="#e74c3c", fg="white", width=12, command=lambda: search_fault("حرارة")).pack(side=tk.RIGHT, padx=3)
tk.Button(row1, text="🔋 بطارية", font=("Arial", 9, "bold"), bg="#f39c12", fg="white", width=12, command=lambda: search_fault("بطارية")).pack(side=tk.RIGHT, padx=3)
tk.Button(row1, text="❄️ مكيف", font=("Arial", 9, "bold"), bg="#3498db", fg="white", width=12, command=lambda: search_fault("مكيف")).pack(side=tk.RIGHT, padx=3)
tk.Button(row1, text="🛑 فرامل", font=("Arial", 9, "bold"), bg="#9b59b6", fg="white", width=12, command=lambda: search_fault("فرامل")).pack(side=tk.RIGHT, padx=3)

# الصف الثاني من الأزرار
row2 = tk.Frame(frame_quick, bg="#f8f9fa")
row2.pack(pady=4, fill=tk.X)

tk.Button(row2, text="⚙️ محرك", font=("Arial", 9, "bold"), bg="#2c3e50", fg="white", width=12, command=lambda: search_fault("محرك")).pack(side=tk.RIGHT, padx=3)
tk.Button(row2, text="⛽ وقود", font=("Arial", 9, "bold"), bg="#16a085", fg="white", width=12, command=lambda: search_fault("وقود")).pack(side=tk.RIGHT, padx=3)
tk.Button(row2, text="🔌 كهرباء", font=("Arial", 9, "bold"), bg="#d35400", fg="white", width=12, command=lambda: search_fault("كهرباء")).pack(side=tk.RIGHT, padx=3)
tk.Button(row2, text="🛞 إطارات وعلق", font=("Arial", 9, "bold"), bg="#7f8c8d", fg="white", width=12, command=lambda: search_fault("إطار")).pack(side=tk.RIGHT, padx=3)

# منطقة البحث التقليدية
frame_top = tk.Frame(root, bg="#f8f9fa")
frame_top.pack(pady=8)

label_instruction = tk.Label(frame_top, text="أو ابحث بنفسك:", font=("Arial", 11), bg="#f8f9fa")
label_instruction.pack(side=tk.RIGHT, padx=5)

entry_query = tk.Entry(frame_top, font=("Arial", 12), width=22, justify="right")
entry_query.pack(side=tk.RIGHT, padx=5)
entry_query.bind("<Return>", lambda event: search_fault())

btn_search = tk.Button(frame_top, text="بحث مخصص", font=("Arial", 10, "bold"), bg="#2980b9", fg="white", padx=10, command=lambda: search_fault())
btn_search.pack(side=tk.RIGHT, padx=5)

# مساحة عرض النتائج
frame_middle = tk.Frame(root)
frame_middle.pack(pady=5, fill=tk.BOTH, expand=True, padx=15)

text_result = scrolledtext.ScrolledText(frame_middle, wrap=tk.WORD, font=("Arial", 11), bg="white", fg="#333", padx=10, pady=10)
text_result.pack(fill=tk.BOTH, expand=True)
text_result.insert(tk.END, "أهلاً بك! اضغط على أي زر تصنيف بالأعلى أو ابحث بكلمة مفتاحية لتظهر لك الأعطال مع مستوى خطورتها فوراً...")
text_result.config(state=tk.DISABLED)

# زر حفظ التقرير في الأسفل
frame_bottom = tk.Frame(root, bg="#f8f9fa")
frame_bottom.pack(pady=8)

btn_save = tk.Button(frame_bottom, text="💾 حفظ النتيجة كتقرير نصي", font=("Arial", 11, "bold"), bg="#27ae60", fg="white", padx=15, pady=4, command=save_report)
btn_save.pack(side=tk.RIGHT, padx=5)

root.mainloop()