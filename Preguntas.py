#!/usr/bin/python
#-*- coding: utf8 -*-

from tkinter import *                   ######IMPORTATION DES BIBLIOTEQUES NECESAIRES
from random import shuffle

root = Tk()                     #######     CREATION ET CONFIGURATION DE LA PAGE ##########
root.title("Preguntas")
root.geometry("375x570+450+70")
root["bg"]="dim gray"



foto=PhotoImage(file="bandera.gif")             #####VARIABLES GLOBAL, COMPTEURS######
count=0
correct=0

titulo="        HISTORIA"                   ########################### 1ER BLOQUE DE VARIABLES A INTRODUIRE DANS FONCTION#######
question="¿Por qué color se suele representar \n al partido comunista?"
r1="Azul"
r2="Rojo"
r3="Negro"
r4="Verde"



def start(a,b,c,d,e,f):                             #######FONCTION PRINCIPAL DU PROGRAMME######



##################################################
        ################################
#     INTERFACE GRAPGIQUE, FRAMES ET LABELS
    ####################################
###################################################



    encabezado=Frame(root,bg="black")            ######FRAME BARRA SUPERIOR
    encabezado.grid(row=1,column=1)


    global foto                                                         ######################CONFIG FOTO + LABELS (TITULO + TIEMPO)
    Label(encabezado,image=foto,anchor="w").grid(row=1,column=1)

    Label(encabezado,text=a,fg="white",font="Arial 15 bold",bg="black",width=17,height=1,anchor="n").grid(row=1,column=2)

    time=Label(encabezado,fg="white",font="Arial 14 bold",bg="black",width=8,height=2)
    time.grid(row=1,column=3)



    pregunta=Frame(root,bg="dim gray")                  #########FRAME QUESTION + REPONSE
    pregunta.grid(row=2,column=1)


    Label(pregunta,bg="dim gray").grid(row=1,column=1)
    preg=Label(pregunta,text=b, font="Arial 14 bold",bg="white", height=8,width=30)         ######QUESTION PLUS ESPACES BLANC POUR VISUALISATION
    preg.grid(row=2,column=1)

    Label(pregunta,text="",font=("",30),bg="dim gray").grid(row=4,column=1)



    bouttons=Frame(root,bg="dim gray")                      ######FRAME POUR BOUTONS REPONSE
    bouttons.grid(row=3,column=1)




    realAns=0

    def answer(answ):                           ########ACTIVATION AVEC UNE REPONSE OU PAS DE TEMPS
        nonlocal realAns
        global correct
        if realAns==0:              ####POUR VERIFIER UNE REPONSE PAR QUESTION
            if answ==a1 or answ==a3 or answ==a4:
                result="INCORRECTO"             ####SI INCORRECT, RESULTATA ET COULEUR CONFIGURÉ
                color="red"
            elif answ==a2:

                result="CORRECTO"                   ######SI CORRECT, RESULTAT ET COULEUT CONFIGURE
                color="green"
                correct+=1
                print(correct)

            elif answ==sec:
                result="TE QUEDASTE SIN TIEMPO"                 ####SI PAS DE TEMPS, RESULTAT ET COULEUT CONFIGURE
                color="red"


            if answ!=sec:
                answ.config(bg="red3",foreground="white")           ###SI REPONSE MARQUE, EN ROUGE
            a2.config(bg="green4",foreground="white")           ####REPONSE CORRECT EN VERT (REMPLACE SI C'ETAIT CORRECT LE ROUGE)
            realAns+=1                      #####EMPECHE CLIQUER A NOUVEAU
            Label(pregunta,text=result, font="Arial 18 bold",bg="white",fg=color, width=24).grid(row=3,column=1)
            preg.config(height=7)                                       ########LABEL REPONSE AVEC COULEUR ET RESULTAT

            suivant=Button(bouttons,text="Siguiente",font=("bold",13),fg="orange",bd=4,width=15,bg="black",command=lambda: start(titulo,question,r1,r2,r3,r4))
            suivant.grid(row=8,column=1)                            ###########3BOUTON POUR PASSER A SUIVANTE QUESSTION





    sec=-1
    def tick():                                         ############# FONCTION COMPTEUR#################
        nonlocal sec
        sec += 1
        time["text"]=20-sec                 #####REGRESIVE
        time.after(1000, tick)
        if time["text"]<=-1:
            time["text"]=0                  ####CONFIG LABEL QUI MONTRE SEC RESTANT
            answer(sec)                 ####REPONSE EN CAS DE TEMPS PASSE, APPELE ANSW#




    global count

    orden=[1,3,5,7]         ####POSIBLE LIGNE DES REPONSE

    if count<5:             ###SI PAS DERNIERE UTILISATION FONCTION
        shuffle(orden)  ######ORDRE ALEATOIRE DE REPONSE
        tick()       ####3ACTIVAION DE TICK, COMPTEUR TEMPS


##################################################
#################                   #################
#               CONFIGURATION BOUTONS
#######################################################


    a1= Button(bouttons,text=c,font=("Calibri",14),bg="white",height=1,width=35,bd=5,command= lambda: answer(a1))
    a1.grid(row=orden[0],column=1)                                                                                      #####TEXT VARIABLE + APPELLE FONCTION ASNWER

    Label(bouttons,font=("",2),bg="dim gray").grid(row=2,column=1)                  ##############ESPACE SEPARATION

    a2= Button(bouttons,text=d,font=("Calibri",14),bg="white",height=1,width=35,bd=5,command= lambda: answer(a2))
    a2.grid(row=orden[1],column=1)

    Label(bouttons,font=("",2),bg="dim gray").grid(row=4,column=1)

    a3= Button(bouttons,text=e,font=("Calibri",14),bg="white",height=1,width=35,bd=5,command= lambda: answer(a3))
    a3.grid(row=orden[2],column=1)

    Label(bouttons,font=("",2),bg="dim gray").grid(row=6,column=1)

    a4= Button(bouttons,text=f,font=("Calibri",14),bg="white",height=1,width=35,bd=5,command= lambda: answer(a4))
    a4.grid(row=orden[3],column=1)

    Label(bouttons,font=("",20),bg="dim gray").grid(row=8,column=1)


    def fin(ax):                #######DESACTIVATION DE COMMAND BOUTON
        ax.config(command="")


#########################################################
        ##########################
########## BLOQUES DES REPONSE + QUESTION + TITRE     #
        ###########################
#############################################################


    if count==0:                            ####NOUVEAU VALEUR POUR VARIABLE QUESTION + TITRE+ REPONS
        titulo="        Civica"
        question="¿Que articulo de la CN. trata \n el derecho de los trabajadores? "
        r1="14"
        r2="14bis"                  ####REPONSE CORRECTE
        r3="19"
        r4="21"

    elif count==1:
        titulo="        Geografia"
        question="¿Qué provincia está ubicada \n más al Sur de la Argentina?"
        r1="Tucumán"
        r2="Tierra del Fuego"           ####REPONSE CORRECTE
        r3="Buenos Aires"
        r4="Mendoza"

    elif count==2:

        titulo="        Deportes"
        question="¿En quá año Maradona convirtió un gol \n con la mano frente a los ingleses?"
        r1="1930"
        r2="1986"                   ########REPONSE CORRECTE
        r3="1990"
        r4="1978"

    elif count==3:
        titulo="        Ciencias"
        question="¿Que es un catión? "
        r1="Un tipo de átomo"
        r2="Un ion  con carga positiva"         ####REPONSE CORRECTE
        r3="Un antibiótico"
        r4="Una molecula de la piel"

    elif count==4:
        titulo="          Fin del Juego"            ###ANNONCE FIN DU JEU
        r1="Has contestado"
        r2=(correct,"/5")               ###MONTRE REPONSE BIEN REPONDU
        r3="respuestas"
        r4="correctamente."
        question="   RESULTADO \n FINAL"

    else:
        fin(a1),fin(a2),fin(a3),fin(a4)             ######QUAND FIN DU JEU, APPELLE FONCTION FIN POUR ANULER EFFET BOUTONS
        Button(bouttons,text="Cerrar",font=("bold",13),fg="orange",bd=4,width=15,bg="black",command=root.destroy).grid(row=8,column=1) #####BOUTON POUR TERMINER



    count+=1      ######+1 DANS LA VARIABLE POUR CHANGER A NOUVEAU VALEURS VARIABLES REPONSE + QUESTION


start(titulo,question,r1,r2,r3,r4)          #####APPELLE POUR DEMARRER LA FONCTION START, DONC DEMARRAGE DU PROGRAMME AVEC VARIABLES INITIALES


root.mainloop()             ########FIN DU PROGRAMME



####################
#    Martín Anús   #
#                  #
####################

 #          L'image du drapeau Argentin est prise de https://commons.wikimedia.org/wiki/File:Flag_of_Argentina.svg
 #          et son utilisation est libre.


