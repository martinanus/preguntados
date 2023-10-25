from tkinter import *

root = Tk()
root.title("Preguntas")
root.geometry("375x570+450+70")
root["bg"]="dim gray"

def start():
    root.destroy()    
    import Preguntas
    
Label(root,text="Juego de preguntas \n y respuestas \n",font=("Arial",30),fg="red",bg="dim gray").pack()            ######TITRE##########
Label(root,text="Consignas: ",font=("Arial",15),fg="white",bg="dim gray").pack()            ######TITRE##########

Label(root,text="Tenés que contestar correctamente \n la mayor cantidad de preguntas \n", fg="blue",font=("Times New Roman", 18),bg="dim gray").pack()
#######CONSIGNES SUR LABELS, #######3
Label(root,text="Tenés 20 segundos por pregunta \n para contestar \n \n", fg="lime green",font=("Times New Roman", 18),bg="dim gray").pack()



Label(root,text="¿¡¿Estás listo?!?",font=("Arial Black",37),bg="dim gray").pack()
Button(root,text="EMPEZAR",font=("",23),command=start).pack()




root.mainloop()
