class Luncher:
    def __init__(self,transducteur,fileToTranslate):
        self.transducteur=transducteur
        self.fileName=fileToTranslate
        self.filaToTranslate=fileToTranslate
    
    def lunch(self):
        if "#OTHER" in self.transducteur.inAlphabet:
            self.sequencer2()
        else:
            self.sequencer() 

    def sequencer(self):
        currentState=self.transducteur.states['0']
        translation=""
        with open(self.filaToTranslate,"r") as ffile:
            for charachter in ffile.read():
                outputchar,currentStateNumber=currentState.succesors[charachter]
                translation+=outputchar
                currentState=self.transducteur.states[currentStateNumber]
        with open("result.txt","w") as resultFile:
            resultFile.write(translation)
        #print(translation)

    def sequencer2(self):
        currentState=self.transducteur.states['0']
        translation=""
        with open(self.filaToTranslate,"r") as ffile:
            for charachter in ffile.read():
                tCharachter=charachter if charachter in self.transducteur.inAlphabet[:-1] else "#OTHER"
                toutputchar,currentStateNumber=currentState.succesors[tCharachter]
                outputchar= toutputchar if tCharachter!="#OTHER" else charachter
                translation+=outputchar
                currentState=self.transducteur.states[currentStateNumber]
        with open("result.txt","w") as resultFile:
            resultFile.write(translation)
        #print(translation)
import os
from transducteur import Transducteur
## voila un petit transducteur qui permet de d'effacer les occurences multiples de la lettre b
trans1=Transducteur()
trans1.readTransducteur("Model/examples/transductorsDir/spaceDeleter.txt")
ln=Luncher(trans1,"Model/examples/inputFiles/testFile.txt")
ln.lunch()