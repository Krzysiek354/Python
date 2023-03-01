import Tkinter as tk
import ttk as ttk
import tkMessageBox as msb

class apl:
	def __init__(self):
		self.window=tk.Tk()
		self.window.title("Przelicznik_mA_")
		self.window.geometry("300x300")
		self.cb_value=tk.StringVar()
		self.combobox=ttk.Combobox(self.window, textvariable=self.cb_value)
		self.combobox.place(x=70,y=0,width=100)
		self.combobox['values']=('4-20mA','0-20mA')
		self.combobox.bind("<<ComboboxSelected>>", self.zmiana)
		self.label=tk.Label(self.window,text="ZAKRES")
		self.label.place(x=0,y=20)
		self.labelpr=tk.Label(self.window,text="PRAD")
		self.labelpr.place(x=140,y=20)
		self.przel=tk.Button(self.window,text="PRZELICZ",command=self.przelicz)
		self.przel.place(x=140,y=80)
		self.e1=tk.Entry(self.window,width=10)
		self.e1.place(x=0,y=40)
		self.e2=tk.Entry(self.window,width=10)
		self.e2.place(x=140,y=40)
		self.labelwy=tk.Label(self.window,text="WYNIK",fg="green")
		self.labelwy.place(x=0,y=80)


		self.window.mainloop()

	def zmiana(self,event):
		msb.showinfo("Info",self.cb_value.get())
	def przelicz(self):
		if self.combobox.current() == 0:
			wynik=float(self.e1.get())*(float(self.e2.get())-4)/16
			self.labelwy.config(text=round(wynik,3))
		elif self.combobox.current() == 1:
			wynik=float(self.e1.get())*(float(self.e2.get()))/20
			self.labelwy.config(text=round(wynik,3))
			
		


aplicat=apl()

