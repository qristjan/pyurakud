import cryptocurrency.information.coingecko_api as ca
import tkinter as tk

coin_info = {coin.name: coin for coin in ca.list_coins()}

top = tk.Tk()
top.title("Coingecko")
top.geometry("300x500")

listbox = tk.Listbox(top)
listbox.pack(expand=1, side=tk.LEFT, fill=tk.BOTH)
scrollbar = tk.Scrollbar(top, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)


def open_coin_window(coin):
    coin_top = tk.Toplevel(top)
    coin_top.title(coin.name)
    coin_top.geometry("300x300")
    info = ca.get_coin_info(coin)
    coin_text = tk.Text(coin_top, height=5, width=100)
    coin_text.pack()
    coin_text.insert(tk.END, info)


def select(evt):
    open_coin_window(coin_info[listbox.get(tk.ANCHOR)])


listbox.bind('<<ListboxSelect>>', select)

for ci in coin_info.keys():
    listbox.insert(tk.END, ci)

top.mainloop()
