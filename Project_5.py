
import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("360x285")
root.configure(background='skyblue')

# Data
inputs = []
firstNum = None
secondNum = None
result = None
operator = ''

def refreshNum():
	tmp = ''.join(inputs)
	entryBox.delete(1.0, tk.END)
	entryBox.insert(tk.END, str(tmp))

def clicked0():
	inputs.append('0')
	refreshNum()

def clicked1():
	inputs.append('1')
	refreshNum()

def clicked2():
	inputs.append('2')
	refreshNum()

def clicked3():
	inputs.append('3')
	refreshNum()

def clicked4():
	inputs.append('4')
	refreshNum()

def clicked5():
	inputs.append('5')
	refreshNum()

def clicked6():
	inputs.append('6')
	refreshNum()

def clicked7():
	inputs.append('7')
	refreshNum()

def clicked8():
	inputs.append('8')
	refreshNum()

def clicked9():
	inputs.append('9')
	refreshNum()

def clickedDot():
	inputs.append('.')
	refreshNum()	

#========================
def clickedSign(sign):
	global firstNum
	global operator	
	if (firstNum == None):
		tmp = ''.join(inputs)
		firstNum = float(tmp)
		inputs.clear()
		operator = sign
	elif (firstNum != None) and (operator != '') and (len(inputs) != 0):
		tmp = ''.join(inputs)
		tmpSecondNum = 0
		tmpSecondNum = float(tmp)
		tmpResult = 0
		if operator == '+':
			tmpResult = firstNum + tmpSecondNum
		elif operator == '-':
			tmpResult = firstNum - tmpSecondNum
		elif operator == '*':
			tmpResult = firstNum * tmpSecondNum
		elif operator == '/':
			tmpResult = firstNum / tmpSecondNum

		tmpResult = round(tmpResult, 3)
		entryBox.delete(1.0, tk.END)
		entryBox.insert(tk.END, str(tmpResult))		

		inputs.clear()
		firstNum = tmpResult
		operator = sign


def clickedAdd():
	clickedSign('+')

def clickedSubtract():
	clickedSign('-')	

def clickedMultipy():
	clickedSign('*')

def clickedDivid():
	clickedSign('/')

def chickedCancel():
	global firstNum
	firstNum = None	
	global secondNum
	secondNum = None
	global result
	result = None
	global operator
	operator = ''	
	global inputs
	inputs.clear()
	entryBox.delete(1.0, tk.END)
	entryBox.insert(tk.END, '0.0')

def clickedEqual():
	if (firstNum == None) and (operator == ''):
		return
	elif (firstNum != None) and (operator != '') and (len(inputs) != 0):
		tmp = ''.join(inputs)
		global secondNum
		secondNum = float(tmp)
		global result
		if operator == '+':
			result = firstNum + secondNum
		elif operator == '-':
			result = firstNum - secondNum
		elif operator == '*':
			result = firstNum * secondNum
		elif operator == '/':
			result = firstNum / secondNum

		result = round(result, 3)
		entryBox.delete(1.0, tk.END)
		entryBox.insert(tk.END, str(result))
		inputs.clear()

	elif (firstNum != None) and (operator != '') and (len(inputs) == 0):
		tmpResult = round(firstNum, 3)
		entryBox.delete(1.0, tk.END)
		entryBox.insert(tk.END, str(tmpResult))

#########################
# Starts Here
for i in range(12):
	root.grid_columnconfigure(i, minsize=30)

for j in range(6):
	root.grid_rowconfigure(j, minsize=40)

entryBox = tk.Text(root, height=1, width=30, background="skyblue", font=("Helvetica", 18, "bold"), borderwidth=12, relief="ridge")
entryBox.insert(tk.END, "0.0")
entryBox.grid(row=0, columnspan=12, padx=0, pady=0, sticky=tk.NSEW)

btnC=tk.Button(root,text=" C ",command=chickedCancel).grid(row=1, columnspan=12, rowspan=1, sticky=tk.NSEW)

btn7=tk.Button(root,text=" 7 ",command=clicked7).grid(row=2,column=0, columnspan=3, rowspan=1, sticky=tk.NSEW)
btn8=tk.Button(root,text=" 8 ",command=clicked8).grid(row=2,column=3, columnspan=3, sticky=tk.NSEW)
btn9=tk.Button(root,text=" 9 ",command=clicked9).grid(row=2,column=6, columnspan=3, sticky=tk.NSEW)
btnDivid=tk.Button(root,text=" / ",command=clickedDivid).grid(row=2,column=9, columnspan=3, sticky=tk.NSEW)

btn4=tk.Button(root,text=" 4 ",command=clicked4).grid(row=3,column=0, columnspan=3, sticky=tk.NSEW)
btn5=tk.Button(root,text=" 5 ",command=clicked5).grid(row=3,column=3, columnspan=3, sticky=tk.NSEW)
btn6=tk.Button(root,text=" 6 ",command=clicked6).grid(row=3,column=6, columnspan=3, sticky=tk.NSEW)
btnMultiply=tk.Button(root,text=" * ",command=clickedMultipy).grid(row=3,column=9, columnspan=3, sticky=tk.NSEW)

btn1=tk.Button(root,text=" 1 ",command=clicked1).grid(row=4,column=0, columnspan=3, sticky=tk.NSEW)
btn2=tk.Button(root,text=" 2 ",command=clicked2).grid(row=4,column=3, columnspan=3, sticky=tk.NSEW)
btn3=tk.Button(root,text="3 ",command=clicked3).grid(row=4,column=6, columnspan=3, sticky=tk.NSEW)
btnSubtract=tk.Button(root,text=" - ",command=clickedSubtract).grid(row=4,column=9, columnspan=3, sticky=tk.NSEW)

btn0=tk.Button(root, text=" 0 ",command=clicked0).grid(row=5,column=0, columnspan=4, sticky=tk.NSEW)
btnDot=tk.Button(root, text=" . ",command=clickedDot).grid(row=5,column=4, columnspan=4, sticky=tk.NSEW)
btnAdd=tk.Button(root, text=" + ",command=clickedAdd).grid(row=5,column=8, columnspan=4, sticky=tk.NSEW)

btnEqual=tk.Button(root,text=" = ",command=clickedEqual).grid(row=6, columnspan=12, sticky=tk.NSEW)

root.mainloop()
