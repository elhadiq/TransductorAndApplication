from tkinter import *
import os

def Traduire():
    r=texte_input.get(1.0,END)
    texte_output.delete('1.0', END)
    texte_output.insert(INSERT,"bonjour"+'\n'+r)


#__________________________________INTERFACE GRAPHIQUE
Mafenetre = Tk()
Mafenetre.title("Analyse lexicale & syntaxique d'un algorithme")

frame_entree= Frame(Mafenetre,borderwidth=2,relief=GROOVE,width=800,height=200)
frame_entree.pack_propagate(False)
frame_entree.pack(side=TOP,padx=10,pady=10)

texte_input = Text(frame_entree)
vsb = Scrollbar(frame_entree,orient="vertical", command=texte_input.yview)
vsb.pack(side="right", fill="y")
texte_input.configure(yscrollcommand=vsb.set)
texte_input.pack(side=TOP,padx=2,pady=10,ipady=45,ipadx=40)


frame_bouton= Frame(Mafenetre,borderwidth=2,relief=GROOVE,width=800,height=70)
frame_bouton.pack_propagate(False)
frame_bouton.pack(side=TOP,padx=10,pady=10)

frame_sortie= Frame(Mafenetre,borderwidth=2,relief=GROOVE,width=800,height=200)
frame_sortie.pack_propagate(False)
frame_sortie.pack(side=TOP,padx=10,pady=10)

texte_output = Text(frame_sortie)
vsb = Scrollbar(frame_sortie,orient="vertical", command=texte_output.yview)
vsb.pack(side="right", fill="y")
texte_output.configure(yscrollcommand=vsb.set)
texte_output.pack(side=TOP,padx=2,pady=10,ipady=45,ipadx=40)


Button(frame_bouton,text="Traduire",fg='navy',command=Traduire).pack(side=LEFT,padx=320,pady=0.5,ipady=20,ipadx=30)
Mafenetre.mainloop()

if __name__=="__main__":
    # transExp=Transducteur("test",pourTrans)
    # TransRefactor=Transducteur("Refactor",UnderScoreAndNewlineDeleter)
    # tr1=transExp.translateFromFile("Model/forFile.txt")
    # translation=TransRefactor.translate(tr1)
    # print(translation)
    # with open("result.py","w") as f:
    #     f.write(translation)
    print(os.getcwd())