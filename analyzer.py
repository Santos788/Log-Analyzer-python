import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

LOG_FILE = "logs.txt"


def garantir_arquivo():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w"):
            pass


def adicionar_log():
    ip = entry_ip.get()
    status = entry_status.get()

    if not ip or not status:
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{ip} - {status} - {data}"

    with open(LOG_FILE, "a") as f:
        f.write(log + "\n")

    entry_ip.delete(0, tk.END)
    entry_status.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Log adicionado!")


def analisar_logs():
    if not os.path.exists(LOG_FILE):
        messagebox.showwarning("Erro", "Arquivo não encontrado!")
        return

    ips = {}

    with open(LOG_FILE, "r") as f:
        for linha in f:
            partes = linha.strip().split(" - ")

            if len(partes) < 2:
                continue

            ip, status = partes[0], partes[1]

            if status.lower() == "failed":
                ips[ip] = ips.get(ip, 0) + 1

    resultado.delete("1.0", tk.END)

    resultado.insert(tk.END, "📊 Resultado:\n")

    suspeitos = []

    for ip, total in ips.items():
        resultado.insert(tk.END, f"{ip} -> {total} falhas\n")

        if total >= 3:
            suspeitos.append((ip, total))

    resultado.insert(tk.END, "\n🚨 Suspeitos:\n")

    if suspeitos:
        for ip, total in suspeitos:
            resultado.insert(tk.END, f"{ip} ({total})\n")
    else:
        resultado.insert(tk.END, "Nenhum suspeito\n")


# Interface
garantir_arquivo()

janela = tk.Tk()
janela.title("Log Analyzer PRO")

tk.Label(janela, text="IP:").pack()
entry_ip = tk.Entry(janela)
entry_ip.pack()

tk.Label(janela, text="Status (failed/success):").pack()
entry_status = tk.Entry(janela)
entry_status.pack()

tk.Button(janela, text="Adicionar Log", command=adicionar_log).pack(pady=5)
tk.Button(janela, text="Analisar Logs", command=analisar_logs).pack(pady=5)

resultado = tk.Text(janela, height=15, width=40)
resultado.pack()

janela.mainloop()