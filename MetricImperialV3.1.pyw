"""
Last Update: 2020.3.26
v1: mm + inch + feet&inch
v2: + pixel pitch
v3: able to write python expressions in Entries
v3.1: size adaptive to window
"""

from tkinter import *
from sys import platform


# system check
if platform == "win32":
	font = "Arial"
	fsize = 10
	wsize = '270x150'
	bWidth = 2
	p = 3  #padding of cells
else: 
	font = "Futura"
	fsize = 14
	wsize = '280x135'
	bWidth = 0.5
	p = 0  #padding of cells



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
	mm -> inch
	"""
	return round(u1/25.4, 2)

def u2u3(u2):
	"""
	inch -> feet & inch
	u3 is a tuple of (feet, inch)
	"""
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
	inch -> mm
	"""
	u1 = int(round(u2 * 25.4, 0))
	return u1

def u3u2(u3):
	"""
	feet & inch -> inch
	"""
	f = u3[0]
	if f == None: f = 0

	i = u3[1]
	if i == '': i = 0
	else: i = round(convert_to_float(u3[1]), 2)

	u2 = f*12 + i

	return u2

def u1u4(u1, u4):
	"""
	mm, pitch -> pixel
	u4 = (pitch, pixel)
	"""
	if u4[0]:
		pitch = u4[0]
		if pitch == 0: 
			return (pitch, None)
		else: 
			pixel = round(u1 / pitch, 2)
			return (pitch, pixel)
	else:
		return (None, None)

def u4u1(u4):
	"""
	pixel pitch -> mm
	u4 = (pitch, pixel)
	"""
	u1 = round( u4[0] * u4[1], 2)
	return u1

def clear():
	txt1.delete(0, END)
	txt2.delete(0, END)
	txt3.delete(0, END)
	txt4.delete(0, END)
	txt5.delete(0, END)
	txt6['state'] = 'normal'
	txt6.delete(0, END)
	txt6['state'] = 'readonly'

def refresh(u1,u2,u3,u4):
	"""
	clear all values in entries then re-insert ones in storage
	"""
	clear()
	txt1.insert(0, str(u1))
	txt2.insert(0, str(u2))
	txt3.insert(0, str(u3[0]))
	txt4.insert(0, str(u3[1]))
	if u4[0]:
		txt5.insert(0, str(u4[0]))
	if u4[1]:
		txt6['state'] = 'normal'
		txt6.insert(0, str(u4[1]))
		txt6['state'] = 'readonly'


def u1Update(event):
	u1 = abs(eval(txt1.get()))
	u2 = u1u2(u1)
	u3 = u2u3(u2)
	if txt5.get():
		u4 = (eval(txt5.get()), None)
		u4 = u1u4(u1, u4)
	else: u4 = (None, None)
	refresh(u1,u2,u3,u4)

def u2Update(event):
	u2 = abs(eval(txt2.get()))
	u1 = u2u1(u2)
	u3 = u2u3(u2)
	if txt5.get():
		u4 = (eval(txt5.get()), None)
		u4 = u1u4(u1, u4)
	else: u4 = (None, None)
	refresh(u1,u2,u3,u4)

def u3Update(event):
	if txt3.get():
		u3 = (eval(txt3.get()), txt4.get())
	else:
		u3 = (None, txt4.get())
	u2 = u3u2(u3)
	u3 = u2u3(u2)
	u1 = u2u1(u2)
	if txt5.get():
		u4 = (eval(txt5.get()), None)
		u4 = u1u4(u1, u4)
	else: u4 = (None, None)
	refresh(u1,u2,u3,u4)

def u4Update(event):
	u4 = (eval(txt5.get()), eval(txt6.get()))
	u1 = u4u1(u4)
	u2 = u1u2(u1)
	u3 = u2u3(u2)
	refresh(u1,u2,u3,u4)

def pitchUpdate(event):
	if txt1.get(): u1Update(event)
	elif txt2.get(): u2Update(event)
	elif txt3.get() or txt4.get(): u3Update(event)
	else: pass

window = Tk()
window.title("Metric⥊Imperial")
window.geometry(wsize)

# millimeter entry
txt1 = Entry(window, width = 8, borderwidth = bWidth, font = (font, fsize))
txt1.grid(column = 0, row = 0, sticky=W+E, padx = p, pady = p)
lbl1 = Label(window, text = "mm", font = (font, fsize))
lbl1.grid(column = 1, row = 0, sticky=W)

# inch entry
txt2 = Entry(window, width = 8, borderwidth = bWidth, font = (font, fsize))
txt2.grid(column = 0, row = 1, sticky=W+E, padx = p, pady = p)
lbl2 = Label(window, text = "inch", font = (font, fsize))
lbl2.grid(column = 1, row = 1, sticky=W, padx = p, pady = p)

# feet and inch entry
txt3 = Entry(window, width = 8, borderwidth = bWidth, font = (font, fsize))
txt3.grid(column = 0, row = 2, sticky=W+E, padx = p, pady = p)
lbl3 = Label(window, text = "foot", font = (font, fsize))
lbl3.grid(column = 1, row = 2, sticky=W, padx = p, pady = p)
txt4 = Entry(window, width = 9, borderwidth = bWidth, font = (font, fsize))
txt4.grid(column = 2, row = 2, sticky=W+E, padx = p, pady = p)
lbl4 = Label(window, text = "inch", font = (font, fsize))
lbl4.grid(column = 3, row = 2, sticky=W, padx = p, pady = p)

# pixel pitch entry
txt5 = Entry(window, width = 8, borderwidth = bWidth, font = (font, fsize))
txt5.grid(column = 0, row = 3, sticky=W+E, padx = p, pady = p)
lbl5 = Label(window, text = "pitch:mm", font = (font, fsize))
lbl5.grid(column = 1, row = 3, sticky=W, padx = p, pady = p)
txt6 = Entry(window, width = 8, borderwidth = bWidth, state = 'readonly', font = (font, fsize))
txt6.grid(column = 2, row = 3, sticky=W+E, padx = p, pady = p)
lbl6 = Label(window, text = "pixel", font = (font, fsize))
lbl6.grid(column = 3, row = 3, sticky=W, padx = p, pady = p)

# buttons
b1 = Button(window, text = "Clear", command = clear, font = (font, fsize))
b1.grid(column = 0, row = 4, padx = p, pady = p)

# version number
lbl7 = Label(window, text = "(Version 3.1)", font = (font, fsize-3))
lbl7.grid(column = 1, row = 4, sticky=W, padx = p, pady = p)

# runtime!!
txt1.bind("<Return>", u1Update)
txt2.bind("<Return>", u2Update)
txt3.bind("<Return>", u3Update)
txt4.bind("<Return>", u3Update)
txt5.bind("<Return>", pitchUpdate)
txt6.bind("<Return>", u4Update)

# adaptive
window.grid_columnconfigure(0, weight=3)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=3)
window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)

# keep window open
window.mainloop()
