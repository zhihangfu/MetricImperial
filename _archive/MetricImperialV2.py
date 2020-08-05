"""
Last Update: 2020.3.25
v1: mm + inch + feet&inch
v2: + pixel pitch
"""

from tkinter import *
from sys import platform


# system check
if platform == "win32":
	font = "Arial"
	fsize = 10
	wsize = '235x150'
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
	else: f = float(f)

	i = u3[1]
	if i == '': i = 0
	else: i = round(convert_to_float(u3[1]), 2)

	u2 = f*12 + i

	return str(u2)

def u1u4(u1, u4):
	"""
	mm to pixel pitch
	u4 = (pitch, pixel)
	"""
	if u4[0]:
		pitch = float(u4[0])
		if pitch == 0: 
			return (str(pitch), None)
		else: 
			pixel = round(float(u1) / pitch, 2)
			return (str(pitch), str(pixel))
	else:
		return (None, None)

def u4u1(u4):
	"""
	pixel pitch to mm
	u4 = (pitch, pixel)
	"""
	u1 = round( float(u4[0]) * float(u4[1]), 2)
	return str(u1)

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
	txt1.insert(0, u1)
	txt2.insert(0, u2)
	txt3.insert(0, u3[0])
	txt4.insert(0, u3[1])
	if u4[0]:
		txt5.insert(0, u4[0])
	if u4[1]:
		txt6['state'] = 'normal'
		txt6.insert(0, u4[1])
		txt6['state'] = 'readonly'


def u1Update(event):
	u1 = txt1.get()
	u4 = (txt5.get(), txt6.get())
	u2 = u1u2(u1)
	u3 = u2u3(u2)
	u4 = u1u4(u1, u4)
	refresh(u1,u2,u3,u4)

def u2Update(event):
	u2 = txt2.get()
	u4 = (txt5.get(), txt6.get())
	u1 = u2u1(u2)
	u3 = u2u3(u2)
	u4 = u1u4(u1, u4)
	refresh(u1,u2,u3,u4)

def u3Update(event):
	u4 = (txt5.get(), txt6.get())
	u3 = (txt3.get(), txt4.get())
	u2 = u3u2(u3)
	u3 = u2u3(u2)
	u1 = u2u1(u2)
	u4 = u1u4(u1, u4)
	refresh(u1,u2,u3,u4)

def u4Update(event):
	u4 = (txt5.get(), txt6.get())
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
window.title("Metric-Imperial")
window.geometry(wsize)

# millimeter entry
txt1 = Entry(window, width = 8, borderwidth = bWidth)
txt1.grid(column = 0, row = 0, sticky = "w", padx = p, pady = p)
lbl1 = Label(window, text = "mm", font = (font, fsize))
lbl1.grid(column = 1, row = 0, sticky = "w")

# inch entry
txt2 = Entry(window, width = 8, borderwidth = bWidth)
txt2.grid(column = 0, row = 1, sticky = "w", padx = p, pady = p)
lbl2 = Label(window, text = "inch", font = (font, fsize))
lbl2.grid(column = 1, row = 1, sticky = "w", padx = p, pady = p)

# feet and inch entry
txt3 = Entry(window, width = 8, borderwidth = bWidth)
txt3.grid(column = 0, row = 2, sticky = "w", padx = p, pady = p)
lbl3 = Label(window, text = "foot", font = (font, fsize))
lbl3.grid(column = 1, row = 2, sticky = "w", padx = p, pady = p)
txt4 = Entry(window, width = 9, borderwidth = bWidth)
txt4.grid(column = 2, row = 2, sticky = "w", padx = p, pady = p)
lbl4 = Label(window, text = "inch", font = (font, fsize))
lbl4.grid(column = 3, row = 2, sticky = "w", padx = p, pady = p)

# pixel pitch entry
txt5 = Entry(window, width = 8, borderwidth = bWidth)
txt5.grid(column = 0, row = 3, sticky = "w", padx = p, pady = p)
lbl5 = Label(window, text = "pitch:mm", font = (font, fsize))
lbl5.grid(column = 1, row = 3, sticky = "w", padx = p, pady = p)
txt6 = Entry(window, width = 8, borderwidth = bWidth, state = 'readonly')
txt6.grid(column = 2, row = 3, sticky = "w", padx = p, pady = p)
lbl6 = Label(window, text = "pixel", font = (font, fsize))
lbl6.grid(column = 3, row = 3, sticky = "w", padx = p, pady = p)

# buttons
b1 = Button(window, text = "Clear", command = clear)
b1.grid(column = 0, row = 4, padx = p, pady = p)

# instruction
# lbl4 = Label(window, text = "type&enter", font = (font, fsize))
# lbl4.grid(column = 0, row = 4, sticky = "w")

# runtime!!
txt1.bind("<Return>", u1Update)
txt2.bind("<Return>", u2Update)
txt3.bind("<Return>", u3Update)
txt4.bind("<Return>", u3Update)
txt5.bind("<Return>", pitchUpdate)
txt6.bind("<Return>", u4Update)

# keep window open
window.mainloop()
