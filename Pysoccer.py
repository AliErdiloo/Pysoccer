import tkinter as tk
from tkinter import messagebox

# تابع محاسبه امتیاز بر اساس پست
def calc_score(player):
    position = player["position"].lower()
    goals = player["goals"]
    assists = player["assists"]
    defense = player["defense"]

    if position == "مهاجم":
        return goals * 4 + assists * 2
    elif position == "هافبک":
        return goals * 3 + assists * 3 + defense * 1
    elif position == "مدافع":
        return goals * 2 + assists * 1 + defense * 4
    elif position == "دروازه‌بان":
        return defense * 5 + goals * 1
    else:
        return 0

# کلاس برنامه
class FootballEvaluator:
    def __init__(self, root):
        self.root = root
        self.root.title("🏆 ارزیابی تیم فوتبال")

        self.team = []

        # فرم اطلاعات تیم و بازیکن
        tk.Label(root, text="نام تیم:").grid(row=0, column=0, sticky='e')
        self.team_entry = tk.Entry(root)
        self.team_entry.grid(row=0, column=1)

        tk.Label(root, text="نام بازیکن:").grid(row=1, column=0, sticky='e')
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1)

        tk.Label(root, text="پست (مهاجم/هافبک/مدافع/دروازه‌بان):").grid(row=2, column=0, sticky='e')
        self.position_entry = tk.Entry(root)
        self.position_entry.grid(row=2, column=1)

        tk.Label(root, text="تعداد گل:").grid(row=3, column=0, sticky='e')
        self.goals_entry = tk.Entry(root)
        self.goals_entry.grid(row=3, column=1)

        tk.Label(root, text="تعداد پاس گل:").grid(row=4, column=0, sticky='e')
        self.assists_entry = tk.Entry(root)
        self.assists_entry.grid(row=4, column=1)

        tk.Label(root, text="عملکرد دفاعی (۰ تا ۱۰):").grid(row=5, column=0, sticky='e')
        self.defense_entry = tk.Entry(root)
        self.defense_entry.grid(row=5, column=1)

        # دکمه‌ها
        tk.Button(root, text="➕ افزودن بازیکن", command=self.add_player).grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(root, text="📊 ارزیابی تیم", command=self.show_report).grid(row=7, column=0, columnspan=2, pady=5)

    def add_player(self):
        try:
            player = {
                "name": self.name_entry.get(),
                "position": self.position_entry.get(),
                "goals": int(self.goals_entry.get()),
                "assists": int(self.assists_entry.get()),
                "defense": int(self.defense_entry.get())
            }
            player["score"] = calc_score(player)
            self.team.append(player)

            # پاکسازی فرم
            self.name_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)
            self.goals_entry.delete(0, tk.END)
            self.assists_entry.delete(0, tk.END)
            self.defense_entry.delete(0, tk.END)

            messagebox.showinfo("✅ موفق", "بازیکن با موفقیت اضافه شد.")
        except ValueError:
            messagebox.showerror("❌ خطا", "مقادیر عددی را صحیح وارد کنید.")

    def show_report(self):
        if not self.team:
            messagebox.showwarning("⚠️ هشدار", "هنوز بازیکنی وارد نشده است.")
            return

        team_name = self.team_entry.get() or "بدون نام"
        total_score = sum(p["score"] for p in self.team)
        report_lines = [f"{p['name']} ({p['position']}) - امتیاز: {p['score']}" for p in self.team]
        report = f"📋 گزارش ارزیابی تیم {team_name}:\n\n" + "\n".join(report_lines)
        report += f"\n\n✅ امتیاز نهایی تیم: {total_score}"

        messagebox.showinfo("📊 ارزیابی تیم", report)

# اجرای برنامه
root = tk.Tk()
app = FootballEvaluator(root)
root.mainloop()

