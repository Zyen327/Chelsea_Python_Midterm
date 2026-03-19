import tkinter as tk
from tkinter import messagebox
import db

saved_player = None


def get_player():
    global saved_player

    pid = entry_id.get()

    if not pid.isdigit():
        messagebox.showerror("Error", "Player ID must be an integer.")
        clear_fields()
        return

    player = db.get_player(int(pid))

    if not player:
        messagebox.showerror("Error", "Player not found.")
        clear_fields()
        return

    saved_player = player

    _, _, first, last, pos, ab, hits = player

    entry_first.delete(0, tk.END)
    entry_last.delete(0, tk.END)
    entry_pos.delete(0, tk.END)
    entry_ab.delete(0, tk.END)
    entry_hits.delete(0, tk.END)

    entry_first.insert(0, first)
    entry_last.insert(0, last)
    entry_pos.insert(0, pos)
    entry_ab.insert(0, ab)
    entry_hits.insert(0, hits)


def save_changes():
    global saved_player

    if not saved_player:
        messagebox.showerror("Error", "No player loaded.")
        return

    pid = saved_player[0]
    first = entry_first.get()
    last = entry_last.get()
    pos = entry_pos.get()
    ab = entry_ab.get()
    hits = entry_hits.get()

    if not ab.isdigit() or not hits.isdigit():
        messagebox.showerror("Error", "At bats and hits must be integers.")
        return

    db.update_player(pid, first, last, pos, int(ab), int(hits))
    messagebox.showinfo("Saved", "Player updated.")
    clear_fields()
    saved_player = None


def cancel_changes():
    global saved_player

    if saved_player:
        _, _, first, last, pos, ab, hits = saved_player
        entry_first.delete(0, tk.END)
        entry_last.delete(0, tk.END)
        entry_pos.delete(0, tk.END)
        entry_ab.delete(0, tk.END)
        entry_hits.delete(0, tk.END)

        entry_first.insert(0, first)
        entry_last.insert(0, last)
        entry_pos.insert(0, pos)
        entry_ab.insert(0, ab)
        entry_hits.insert(0, hits)


def clear_fields():
    entry_first.delete(0, tk.END)
    entry_last.delete(0, tk.END)
    entry_pos.delete(0, tk.END)
    entry_ab.delete(0, tk.END)
    entry_hits.delete(0, tk.END)


root = tk.Tk()
root.title("Baseball Team Manager")
root.geometry("350x250")

tk.Label(root, text="Player ID").grid(row=0, column=0, sticky="e")
tk.Label(root, text="First Name").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Last Name").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Position").grid(row=3, column=0, sticky="e")
tk.Label(root, text="At Bats").grid(row=4, column=0, sticky="e")
tk.Label(root, text="Hits").grid(row=5, column=0, sticky="e")

entry_id = tk.Entry(root)
entry_first = tk.Entry(root)
entry_last = tk.Entry(root)
entry_pos = tk.Entry(root)
entry_ab = tk.Entry(root)
entry_hits = tk.Entry(root)

entry_id.grid(row=0, column=1)
entry_first.grid(row=1, column=1)
entry_last.grid(row=2, column=1)
entry_pos.grid(row=3, column=1)
entry_ab.grid(row=4, column=1)
entry_hits.grid(row=5, column=1)

tk.Button(root, text="Get Player", command=get_player).grid(row=0, column=2)
tk.Button(root, text="Save Changes", command=save_changes).grid(row=6, column=0)
tk.Button(root, text="Cancel", command=cancel_changes).grid(row=6, column=1)

root.mainloop()