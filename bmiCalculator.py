import tkinter
from tkinter import *
from tkinter.ttk import *

topWindow = tkinter.Tk()
topWindow.title("BMI Calculator")
topWindow.config(padx=30,pady=30)

def write_result(bmi):
    result_string = f"BMI : {round(bmi,2)}, you're "

    if bmi <=18.5:
        result_string+="severely thin."
    elif 18.5<bmi<=25:
        result_string+="normal."
    elif 25<bmi<=30:
        result_string+="overweight."
    elif 30<bmi<=35:
        result_string+="obese class-I."  
    elif 35<bmi<=40:
        result_string+="obese class-II."      
    elif 40<bmi:
        result_string+="obese class-III."    
    
    return result_string

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Inputs are empty!")
    else:
        try:
            bmi = float(weight) / ((float(height)/100) ** 2) 
            result_label.config(text=write_result(bmi))
        except:
            result_label.config(text="Inputs are invalid!")

#ui
logo = PhotoImage(file = "/home/enes/Works/PythonStudies/bmiLogo.png")            
logo_button = tkinter.Button(image=logo)
logo_button.pack()

weight_input_label = tkinter.Label(text="Enter your weigth (kg)")
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your heigth (cm)")
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()


topWindow.mainloop()


