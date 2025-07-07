import tkinter as tk

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
        
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

def press(num):
    entry.insert(tk.END,str(num))


# Create and configure the main window

window =tk.Tk()
window.title("CALCULATOR")
window.geometry("300x400")

# Entry Widget
entry =tk.Entry(window,width=35,font=("Arial", 35))
entry.pack(pady=10)

# Frame to hold all calculator buttons
frame=tk.Frame(window)
frame.pack()

btn_opts={'padx':15,'pady':15,'width':4,'height':2,'bg':'black','fg':'white','font':("Arial", 20, "bold")
}
# ROW 1
button_7=tk.Button(frame,text="7",command=lambda:press(7),**btn_opts)
button_7.grid(row=1,column=0,padx=5, pady=5)
button_8=tk.Button(frame,text="8",command=lambda:press(8),**btn_opts)
button_8.grid(row=1,column=1,padx=5, pady=5)
button_9=tk.Button(frame,text="9",command=lambda:press(9),**btn_opts)
button_9.grid(row=1,column=2,padx=5, pady=5)
button_add=tk.Button(frame,text="+",command=lambda:press("+"),**btn_opts)
button_add.grid(row=1,column=3,padx=5, pady=5)
button_sub=tk.Button(frame,text="-",command=lambda:press("-"),**btn_opts)
button_sub.grid(row=1,column=4,padx=5, pady=5)

# ROW 2
button_4=tk.Button(frame,text="4",command=lambda:press(4),**btn_opts)
button_4.grid(row=2,column=0,padx=5, pady=5)
button_5=tk.Button(frame,text="5",command=lambda:press(5),**btn_opts)
button_5.grid(row=2,column=1,padx=5, pady=5)
button_6=tk.Button(frame,text="6",command=lambda:press(6),**btn_opts)
button_6.grid(row=2,column=2,padx=5, pady=5)
button_mul=tk.Button(frame,text="*",command=lambda:press("*"),**btn_opts)
button_mul.grid(row=2,column=3,padx=5, pady=5)
button_div=tk.Button(frame,text="/",command=lambda:press("/"),**btn_opts)
button_div.grid(row=2,column=4,padx=5, pady=5)

# ROW 3
button_1=tk.Button(frame,text="1",command=lambda:press(1),**btn_opts)
button_1.grid(row=3,column=0,padx=5, pady=5)
button_2=tk.Button(frame,text="2",command=lambda:press(2),**btn_opts)
button_2.grid(row=3,column=1,padx=5, pady=5)
button_3=tk.Button(frame,text="3",command=lambda:press(3),**btn_opts)
button_3.grid(row=3,column=2,padx=5, pady=5)
button_mod=tk.Button(frame,text="%",command=lambda:press("%"),**btn_opts)
button_mod.grid(row=3,column=3,padx=5, pady=5)
button_pow=tk.Button(frame,text="**",command=lambda:press("**"),**btn_opts)
button_pow.grid(row=3,column=4,padx=5, pady=5)
# ROW 4
button_0=tk.Button(frame,text="0",command=lambda:press(0),**btn_opts)
button_0.grid(row=4,column=0,padx=5, pady=5)
button_00=tk.Button(frame,text="00",command=lambda:press(00),**btn_opts)
button_00.grid(row=4,column=1,padx=5, pady=5)
button_dot=tk.Button(frame,text=".",command=lambda:press("."),**btn_opts)
button_dot.grid(row=4,column=2,padx=5, pady=5)
button_flordiv=tk.Button(frame,text="//",command=lambda:press("//"),**btn_opts)
button_flordiv.grid(row=4,column=3,padx=5, pady=5)
button_ans = tk.Button(frame, text="=",  command=evaluate, bg="green", fg="white", padx=25, pady=25, width=4, height=2, font="20")
# Clear button to erase the input field
button_ans.grid(row=4,column=4,padx=5, pady=5)
button_clear = tk.Button(
    frame, text="C", command=clear, bg="red", fg="white",
    padx=25, pady=25, width=4, height=2, font="20")
button_clear.grid(row=4, column=5, padx=5, pady=5)

window.mainloop()
