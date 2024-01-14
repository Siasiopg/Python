import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


def run_simulation():
    initial_rabbits = int(initial_rabbits_var.get())
    initial_wolves = int(initial_wolves_var.get())
    repetitions = int(repetitions_var.get())
    a = float(a_var.get())
    b = float(b_var.get())
    c = float(c_var.get())

    rabbits_population = [initial_rabbits]
    wolves_population = [initial_wolves]

    for t in range(1, repetitions + 1):
        rabbits_next = rabbits_population[t-1] + (a * rabbits_population[t-1] - (
            b * rabbits_population[t-1] * wolves_population[t-1]))
        wolves_next = wolves_population[t-1] + (
            b * wolves_population[t-1] * rabbits_population[t-1] - c * wolves_population[t-1])

        rabbits_population.append(max(rabbits_next, 0))
        wolves_population.append(max(wolves_next, 0))

    ax.clear()
    ax.plot(range(t + 1), rabbits_population, label='Rabbits', color='pink')
    ax.plot(range(t + 1), wolves_population, label='Wolves', color='red')

    ax.set_xlabel('Time (days)')
    ax.set_ylabel('Population')
    ax.set_title('Lotka-Volterra Simulation')
    ax.legend()

    canvas.draw()


root = tk.Tk()
root.title('Lotka-Volterra Simulator')

labels = ['początkowa wartośc zająców:', 'początkowa wartośc wilków:',
          'parametr a:', 'parametr b:', 'parametr c:', 'ilość miesięcy: ']
default_values = [100, 30, 0.02, 0.0005, 0.05, 300]

initial_rabbits_var = tk.StringVar(value=str(default_values[0]))
initial_wolves_var = tk.StringVar(value=str(default_values[1]))
a_var = tk.StringVar(value=str(default_values[2]))
b_var = tk.StringVar(value=str(default_values[3]))
c_var = tk.StringVar(value=str(default_values[4]))
repetitions_var = tk.StringVar(value=str(default_values[5]))

for i, label_text in enumerate(labels):
    label = ttk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

    default_value_label = ttk.Label(
        root, text=f'(Default: {default_values[i]})')
    default_value_label.grid(row=i, column=2, padx=10, pady=5, sticky='w')

for i, default_value in enumerate(default_values):
    entry_var = None
    if i == 0:
        entry_var = initial_rabbits_var
    elif i == 1:
        entry_var = initial_wolves_var
    elif i == 2:
        entry_var = a_var
    elif i == 3:
        entry_var = b_var
    elif i == 4:
        entry_var = c_var
    elif i == 5:
        entry_var = repetitions_var

    entry = ttk.Entry(root, textvariable=entry_var)
    entry.grid(row=i, column=1, padx=10, pady=5)

run_button = ttk.Button(root, text='Run Simulation', command=run_simulation)
run_button.grid(row=len(labels), column=0, columnspan=3, pady=10)

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=len(labels) + 1, column=0,
                   columnspan=3, padx=10, pady=10)

root.mainloop()
