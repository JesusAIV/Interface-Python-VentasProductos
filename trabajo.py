from tkinter import *
from tkinter import ttk

tablap = []

class Ventas:
    def __init__(self, ventana):
        self.window = ventana
        self.window.title('Perú Delivery')
        self.window.iconbitmap("comida.ico")
        self.window.geometry("700x350")
        self.window.resizable(0, 0)
        self.window.configure(bg="#FDF19B")

        self.name = Label(self.window, text="Nombre: ", background="#FF958E")
        self.name.place(x=20, y=40)
        self.txtname = Entry(self.window, background="#E4E3E2")
        self.txtname.place(x=100, y=40)

        self.price = Label(self.window, text="Precio:",background="#FF958E" )
        self.price.place(x=20, y=80)
        self.txtprice = Entry(self.window, background="#E4E3E2")
        self.txtprice.place(x=100, y=80)

        self.cant = Label(self.window, text="Cantidad:",background="#FF958E")
        self.cant.place(x=20, y=120)
        self.txtcant = Entry(self.window, background="#E4E3E2")
        self.txtcant.place(x=100, y=120)

        self.submit = Button(self.window, text="Guardar Producto",background="#BBB5B4", command=self.Agregar)
        self.submit.place(x=75, y=170)

        self.btnTotal = Button(self.window, text="Total a Pagar",background="#BBB5B4", command=self.Total)
        self.btnTotal.place(x=535, y=280)

        self.tabla = ttk.Treeview(self.window, columns=("col1", "col2", "col3"))
        self.tabla.place(x=270, y=20)
        self.tabla.column("#0", width=90, anchor=CENTER)
        self.tabla.column("col1", width=90, anchor=CENTER)
        self.tabla.column("col2", width=80, anchor=CENTER)
        self.tabla.column("col3", width=80, anchor=CENTER)

        self.tabla.heading("#0", text="Producto", anchor=CENTER)
        self.tabla.heading("col1", text="Precio", anchor=CENTER)
        self.tabla.heading("col2", text="Cantidad", anchor=CENTER)
        self.tabla.heading("col3", text="SubTotal", anchor=CENTER)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#6EDCB8",
                        foreground="black",
                        fieldbackground="#6EDCB8"
                        )
        style.map('Treeview', background=[('selected', '#D4470F')])


    def Agregar(self):

        self.prod = self.txtname.get()
        self.precio = self.txtprice.get()
        self.cant = self.txtcant.get()

        self.productos = {"prod":self.prod, "precio":self.precio, "cant":self.cant}

        self.total = float(self.productos["precio"]) * int(self.productos["cant"])

        self.productos.update({"total":self.total})

        tablap.append(self.productos)
        print(tablap)

        self.tabla.insert("", END, text=self.productos["prod"], values=(self.productos["precio"], self.productos["cant"], self.total))


    def Total(self):
        self.totales = 0
        for list in tablap:
            self.totales = self.totales + list["total"]

        self.igv = round(self.totales*0.18, 2)
        self.totalcigv = round(self.totales + self.igv, 2)

        self.name = Label(self.window, text="Total: ")
        self.name.place(x=20, y=230)
        self.txtname = Label(self.window, text=round(self.totales))
        self.txtname.place(x=100, y=230)

        self.price = Label(self.window, text="IGV: ")
        self.price.place(x=20, y=270)
        self.txtprice = Label(self.window, text=self.igv)
        self.txtprice.place(x=100, y=270)

        self.cant = Label(self.window, text="Total incuido IGV: ")
        self.cant.place(x=20, y=310)
        self.txtcant = Label(self.window, text=self.totalcigv)
        self.txtcant.place(x=130, y=310)

if __name__ == '__main__':
    ventana = Tk()
    app = Ventas(ventana)
    ventana.mainloop()