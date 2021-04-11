class Luncher:
    def __init__(self,transducteur,fileToTranslate):
        self.transducteur=transducteur
        self.fileName=fileToTranslate
        self.filaToTranslate=fileToTranslate
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