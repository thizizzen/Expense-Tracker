import sqlite3
from tkinter import messagebox
import re

class Budget:
    def __init__(self):
        self.conn = sqlite3.connect("budget.db")
        self.cur = self.conn.cursor()

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS purchases "
            "(id INTEGER PRIMARY KEY, product TEXT, price REAL CHECK (typeof(price) = 'real' AND price >= 0), category TEXT, comment TEXT)"
        )

        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def validate_price(self, price):
        pattern = re.compile(r'^\d+(\.\d{1,2})?$')
        return bool(pattern.match(price))

    def view(self):
        self.cur.execute("SELECT * FROM purchases")
        rows = self.cur.fetchall()

        formatted_rows = [(row[0], row[1], f'₱{int(row[2]):,}' if row[2].is_integer() else f'₱{row[2]:,.2f}', row[3], row[4]) for row in rows]

        return formatted_rows

    def insert(self, product, price, category, comment):
        try:
            price = ''.join(char for char in price if char.isdigit() or char == '.')

            if not self.validate_price(price):
                messagebox.showwarning(title="Incorrect value",
                                       message="Please enter a valid number for the Price field."
                                               "\n\nFor instance: 100 | 5648.55 | 456 | 0 etc.")
                return

            price = float(price)

            if price < 0:
                messagebox.showwarning(title="Incorrect value",
                                       message="Only numbers equal to or greater than 0 are allowed in the Price field."
                                               "\n\nFor instance: 100 | 5648.55 | 456 | 0 etc.")
                return

            self.cur.execute("INSERT INTO purchases VALUES (NULL,?,?,?,?)", (product, price, category, comment,))
            self.conn.commit()
        except ValueError:
            messagebox.showwarning(title="Incorrect value",
                                   message="Please enter a valid number for the Price field."
                                           "\n\nFor instance: 100 | 5648.55 | 456 | 0 etc.")

    def update(self, id, product, price, category, comment):
        try:
            price = ''.join(char for char in price if char.isdigit() or char == '.')

            if not self.validate_price(price):
                messagebox.showwarning(title="Incorrect value",
                                       message="Please enter a valid number for the Price field."
                                               "\n\nFor instance: 100 | 5648.55 | 456 | 0 etc.")
                return

            price = float(price)

            if price < 0:
                messagebox.showwarning(title="Incorrect value",
                                       message="Only numbers equal to or greater than 0 are allowed in the Price field."
                                               "\n\nFor instance: 100 | 5648.55 | 456 | 0 etc.")
                return

            self.cur.execute("UPDATE purchases SET product=?, price=?, category=?, comment=? WHERE id=?",
                             (product, price, category, comment, id,))
            self.conn.commit()
        except ValueError:
            messagebox.showwarning(title="Incorrect value",
                                   message="Please enter a valid number for the Price field."
                                           "\n\nFor instance: 100 | 5648.55 | 456 | 0 etc.")

    def delete_row(self, id):
        self.cur.execute("DELETE FROM purchases WHERE id=?", (id,))
        self.conn.commit()

    def delete_all_rows(self):
        self.cur.execute("DELETE FROM purchases")
        self.conn.commit()

    def search(self, product="", price="", category=""):
        self.cur.execute("SELECT * FROM purchases WHERE product like ? OR price like ? OR category=?",
                         (product, price, category,))
        rows = self.cur.fetchall()
        formatted_rows = [(row[0], row[1], f'₱{int(row[2]):,}' if row[2].is_integer() else f'₱{row[2]:,.2f}', row[3], row[4]) for row in rows]

        return formatted_rows