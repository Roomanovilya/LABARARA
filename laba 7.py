import random
import tkinter as tk
from tkinter import ttk

'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую библиотеку питона.  
Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
Пират хочет зарыть K кладов на T островах.
Каждый клад имеет свою стоимость.
Общая стоимость кладов должна быть не меньше M.
Сформируйте разные варианты размещения кладов.
'''
# Функция для генерации вариантов размещения кладов
def generate_treasure_arrangements(K, T, M):
    a = []
    cost = []  
    maxcost = 0
    for i in range((T + 1) ** K):
        a1 = []
        i1 = i
        cost1 = []
        total_cost = 0
        for _ in range(K):
            island = i1 % (T + 1)
            a1.append(island)
            if island != 0:
                cost_val = random.randint(0, 10)
                cost1.append(cost_val)
                total_cost += cost_val
            else:
                cost1.append(0)
            i1 //= (T + 1)
        if total_cost >= M:
            a.append(a1)
            cost.append(cost1)  
            maxcost = max(maxcost, total_cost)
    return a, cost, maxcost


def calculate_arrangements():
    K = int(entry_k.get())  
    T = int(entry_t.get())
    M = int(entry_m.get())
    a, cost, maxcost = generate_treasure_arrangements(K, T, M)
    
    if not a:
        table.delete(*table.get_children())
        table.insert("", "end", values=("Нет вариантов удовлетворяющих условию"))
    else:
        table.delete(*table.get_children())
        
        header = ["№ Варианта", "Общая стоимость"] + [f"Остров {i}" for i in range(1, T + 1)]
        table["columns"] = header
        table.heading("#0", text="", anchor="w")
        for col in header:
            table.heading(col, text=col, anchor="w")
            table.column(col, anchor="w", width=100)
        
        for idx, (a1, cost1) in enumerate(zip(a, cost)):  
            row = [f"Вариант {idx + 1}"]
            island_clads = [[] for _ in range(T)]
            total_cost = sum(cost1)  
            for j, (island, cost_val) in enumerate(zip(a1, cost1)):
                if island != 0:
                    island_clads[island - 1].append(f"{j + 1}({cost_val})")
            row.append(str(total_cost))
            for island in island_clads:
                if island:
                    row.append(", ".join(island))
                else:
                    row.append("0")

            table.insert("", "end", values=row)

    max_cost_label.config(text=f'Максимальная общая стоимость: {maxcost}')

# основное окно
root = tk.Tk()
root.title("Пиратский клад")
root.configure(bg="#CD8162")

frame = tk.Frame(root, bg="#CD8162")
frame.pack(padx=10, pady=10)

# ввод
tk.Label(frame, text="Количество кладов :", bg="#CD8162").grid(row=0, column=0, padx=5, pady=5)
entry_k = tk.Entry(frame)
entry_k.grid(row=0, column=1, padx=5, pady=5)
entry_k.configure(bg="#EEDFCC")

tk.Label(frame, text="Количество островов :", bg="#CD8162").grid(row=1, column=0, padx=5, pady=5)
entry_t = tk.Entry(frame)
entry_t.grid(row=1, column=1, padx=5, pady=5)
entry_t.configure(bg="#EEDFCC")

tk.Label(frame, text="Минимальная общая стоимость :", bg="#CD8162").grid(row=2, column=0, padx=5, pady=5)
entry_m = tk.Entry(frame)
entry_m.grid(row=2, column=1, padx=5, pady=5)
entry_m.configure(bg="#EEDFCC")

# Кнопка для расчетов
calculate_button = tk.Button(frame, text="Рассчитать", command=calculate_arrangements, bg="#EEDFCC")
calculate_button.grid(row=3, columnspan=2, padx=5, pady=5)

max_cost_label = tk.Label(frame, text="", bg="#CD8162")
max_cost_label.grid(row=4, columnspan=2, padx=5, pady=5)

table_frame = tk.Frame(root)
table_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Настройка стилей для таблицы
style = ttk.Style()
style.configure("Treeview", 
                background="#EEDFCC", 
                foreground="black",
                rowheight=25,
                fieldbackground="#EEDFCC")
style.map('Treeview', background=[('selected', '#CDB79E')], foreground=[('selected', 'white')])

table = ttk.Treeview(table_frame, show="headings")
table.pack(side="left", fill="both", expand=True)

# скроллбар
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
scrollbar.pack(side="right", fill="y")
table.configure(yscrollcommand=scrollbar.set)

root.mainloop()
