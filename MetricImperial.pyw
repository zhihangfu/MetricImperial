from tkinter import *
from sys import platform

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

def u1u2(u1):
	"""
	mm to inch, all strings
	"""
	return str(round(float(u1)/25.4, 2))

def u2u3(u2):
	"""
	inch to feet&inch, all strings
	u3 is a tuple of (feet, inch)
	"""
	u2 = float(u2)
	f = u2//12
	i = u2%12
	inch_int = int(i//1)
	inch_frac = i%1
	# 1/4" accuracy
	test = round(inch_frac/0.25)
	if test == 0:
		i = str(inch_int)
	elif test == 4:
		i = str(inch_int+1)
	elif test == 2:
		i = str(inch_int) + " 1/2"
	else:
		i = str(inch_int) + " " + str(test) + "/4"

	return (str(int(f)), i)

def u2u1(u2):
	"""
	inch to mm, all strings
	"""
	u2 = float(u2)
	u1 = int(round(u2 * 25.4, 0))
	return str(u1)

def u3u2(u3):
	"""
	feet&inch to inch
	"""
	f = u3[0]
	if f == '': f = 0
	else: f = int(f)

	i = u3[1]
	if i == '': i = 0
	else: i = round(convert_to_float(u3[1]), 2)

	u2 = f*12 + i

	return str(u2)

def u1Update(event):
	u1 = txt1.get()
	u2 = u1u2(u1)
	u3 = u2u3(u2)
	txt2.delete(0, END)
	txt2.insert(0, u2)
	txt3.delete(0, END)
	txt3.insert(0, u3[0])
	txt4.delete(0, END)
	txt4.insert(0, u3[1])

def u2Update(event):
	u2 = txt2.get()
	u1 = u2u1(u2)
	u3 = u2u3(u2)
	txt1.delete(0, END)
	txt1.insert(0, u1)
	txt3.delete(0, END)
	txt3.insert(0, u3[0])
	txt4.delete(0, END)
	txt4.insert(0, u3[1])

def u3Update(event):
	u3 = (txt3.get(), txt4.get())
	u2 = u3u2(u3)
	u1 = u2u1(u2)
	txt1.delete(0, END)
	txt1.insert(0, u1)
	txt2.delete(0, END)
	txt2.insert(0, u2)

def clear():
	"""
	clear all values in entries
	"""
	txt1.delete(0, END)
	txt2.delete(0, END)
	txt3.delete(0, END)
	txt4.delete(0, END)

# system check
if platform == "win32":
	font = "Microsoft YaHei"
	fsize = 8
	wsize = '210x90'
else: 
	font = "Futura"
	fsize = 14
	wsize = '280x130'

window = Tk()
window.title("Metric - Imperial")
window.geometry(wsize)

# millimeter entry
txt1 = Entry(window, width = 8)
txt1.grid(column = 0, row = 0)
lbl1 = Label(window, text = "mm", font = ("Futura", fsize))
lbl1.grid(column = 1, row = 0)

# inch entry
txt2 = Entry(window, width = 8)
txt2.grid(column = 0, row = 1)
lbl2 = Label(window, text = "inch", font = ("Futura", fsize))
lbl2.grid(column = 1, row = 1)

# feet and inch entry
txt3 = Entry(window, width = 8)
txt3.grid(column = 0, row = 2)
lbl3 = Label(window, text = "feet", font = ("Futura", fsize))
lbl3.grid(column = 1, row = 2)
txt4 = Entry(window, width = 9)
txt4.grid(column = 2, row = 2)
lbl4 = Label(window, text = "inch", font = ("Futura", fsize))
lbl4.grid(column = 3, row = 2)

# instruction
lbl4 = Label(window, text = "type&enter", font = ("Futura", fsize))
lbl4.grid(column = 0, row = 3)


txt1.bind("<Return>", u1Update)
txt2.bind("<Return>", u2Update)
txt3.bind("<Return>", u3Update)
txt4.bind("<Return>", u3Update)

window.mainloop()