import rnribeiro as rr

#Main window
window = rr.tk.Tk()
window.title('Enquadrador de valores')
window.geometry('1050x450')

global int0a25
global int25a50
global int50a75
global int75a100
int0a25 = []
int25a50 = []
int50a75 = []
int75a100 = []
global count
count = 0
global numberofvalues

#Function that loops through the number of values and frames them at the same time
def next_value(): 
        global values_input 
        global count
              
        try :          
                value = int(values_input.get()) 
                if int(values_input.get()) < 0 or int(values_input.get()) > 100:
                        raise Exception                                                
        except:
                rr.messagebox.showinfo("ERRO!", "Insira um número inteiro entre 0 e 100!")
                proceed = rr.messagebox.askyesno("ERRO!", "Pretende continuar?")                             
                if proceed == True:
                        values_input.delete(0, rr.tk.END)
                        values_input.insert(0,'')
                        numbers_window.lift()
                        return
                else:
                        quit()
                        
                        
        if int(value) > 75:                         
                int75a100.append(int(value))
        elif int(value) > 50:                        
                int50a75.append(int(value))
        elif int(value) > 25:                        
                int25a50.append(int(value))
        else:
                int0a25.append(int(value))
                
        count += 1
        if count == numberofvalues: 
                _0_25_label['text'] = "O número de valores inseridos na classe [0-25] é " + str(len(int0a25)) + " que corresponde a: " + str(round((len(int0a25)/int(numberofvalues)*100),1)) + " % do total de números inseridos."
                _25_50_label['text'] = "O número de valores inseridos na classe ]25-50] é " + str(len(int25a50)) + " que corresponde a: " + str(round((len(int25a50)/int(numberofvalues)*100),1)) + " % do total de números inseridos."
                _50_75_label['text'] = "O número de valores inseridos na classe ]50-75] é " + str(len(int50a75)) + " que corresponde a: " + str(round((len(int50a75)/int(numberofvalues)*100),1))+ " % do total de números inseridos."
                _75_100_label['text'] = "O número de valores inseridos na classe ]75-100] é " + str(len(int75a100)) + " que corresponde a: " + str(round((len(int75a100)/int(numberofvalues)*100),1)) + " % do total de números inseridos."
                numbers_window.destroy()
                
        else:
                values_input.delete(0, rr.tk.END)
                values_input.insert(0,'')

#Opens input numbers window
def check_button_click():
        global numberofvalues
        global numbers_window
        global values_input
        global count
        count = 0
        global int0a25
        global int25a50
        global int50a75
        global int75a100
        int0a25 = []
        int25a50 = []
        int50a75 = []
        int75a100 = []
        _0_25_label['text'] = "O número de valores inseridos na classe [0-25] é ... que corresponde a: ... % do total de números inseridos."
        _25_50_label['text'] = "O número de valores inseridos na classe ]25-50] é ... que corresponde a: ... % do total de números inseridos."
        _50_75_label['text'] = "O número de valores inseridos na classe ]50-75] é ... que corresponde a: ... % do total de números inseridos."
        _75_100_label['text'] = "O número de valores inseridos na classe ]75-100] é ... que corresponde a: ... % do total de números inseridos."
        
        #Valid number
        try:
                numberofvalues = int(numberofvalues_input.get())
                if numberofvalues <= 0:  raise Exception                        
        except: 
                rr.messagebox.showinfo("ERRO!", "Insira um número inteiro positivo!")
                proceed = rr.messagebox.askyesno("ERRO!", "Pretende continuar?")                             
                if proceed == True:
                        numberofvalues_input.delete(0, rr.tk.END)
                        numberofvalues_input.insert(0,'')
                        return
                else:
                        quit()  
        
        
        #Input numbers window and widgets
        numbers_window = rr.tk.Tk()
        numbers_window.title('Enquadrador de valores')
        numbers_window.geometry('400x100')

        label = rr.tk.Label(numbers_window, 
                        text = 'Digite o valor a enquadrar: ',
                        font = ('Arial' , 13)
                        )
        label.place(relx=0.03, rely=.4, anchor="w")

        values_input = rr.tk.Entry(numbers_window,
                                        width = 10,
                                        font = ('Arial', 13)
                                        )
        values_input.place(relx=0.6, rely=.4, anchor="w")

        bt = rr.tk.Button(numbers_window,
                command = next_value,
                text= 'Próximo valor'
                )
        bt.place(relx=0.5, rely=.75, anchor="c") 
        

#Title Label
title_label = rr.tk.Label(window, 
                        text ='Enquadrador de valores',
                        font = ('Arial' , 20),
                        fg = "#ff0000"
                        )
title_label.place(x = 40, y = 25)


#Type in number of numbers label
numberofvalues_label = rr.tk.Label(window,
                                text = 'Digite o números de valores que pretende enquadrar:',
                                font = ('Arial' , 14)
                                )
numberofvalues_label.place(x = 55, y= 100)

#Number of values input box
global numberofvalues_input
numberofvalues_input = rr.tk.Entry(window,
                                width = 10,
                                font = ('Arial', 13)
                                )
numberofvalues_input.place(x = 520, y = 100, height = 30, width = 110)

#Check button
check_button = rr.tk.Button(window,
                        command = check_button_click
                        )
check_button.place(x = 650, y = 93, height = 42, width = 42)

#Result labels   
_0_25_label = rr.tk.Label(window,
                text = "O número de valores inseridos na classe [0-25] é ... que corresponde a: ... % do total de números inseridos.",
                font = (15)
                )
_0_25_label.place(x = 50, y = 200)
_25_50_label= rr.tk.Label(window,
                text = "O número de valores inseridos na classe ]25-50] é ... que corresponde a: ... % do total de números inseridos.",
                font = (15)
                )
_25_50_label.place(x = 50, y = 250)
_50_75_label = rr.tk.Label(window,
                text = "O número de valores inseridos na classe ]50-75] é ... que corresponde a: ... % do total de números inseridos.",
                font = (15)
                )
_50_75_label.place(x = 50, y = 300)
_75_100_label =rr.tk.Label(window,
                text = "O número de valores inseridos na classe ]75-100] é ... que corresponde a: ... % do total de números inseridos.",
                font = (15)
                )
_75_100_label.place(x = 50, y = 350)
window.mainloop()

