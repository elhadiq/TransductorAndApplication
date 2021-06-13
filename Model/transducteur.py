from samples import *
class Transducteur:
    def __repr__(self) -> str:
        return self.name
    def __init__(self,name,dictionary):
        self.name=name
        self.inAlphabet=dictionary["InputAlphabet"]
        self.outAlphabet=dictionary["OutputAlphabet"]
        self.states=dictionary["States"]
        self.transitions=dictionary["Transitions"]
        self.extactionMode=dictionary["ExtractionMode"]
        self.pile=""
    
    @staticmethod
    def extractInpuSequence(textfile,modeExtraction="w"):
        """ 
        le mode d'extraction par defaut est le w
        character: caractere par caractere
        word: mot par mot separés, on prend les mots separes par les espaces
        """
        entree=[]
        with open(textfile,"r") as f:
            a=f.read()
            if modeExtraction=="character":
                return a
            #On utilse notre transducteur deja defini 
            quoteSolverTrans=Transducteur("quoteSolverTrans",quoteSolverDict)
            a=quoteSolverTrans.translate(a)
            a=a.split("\n")
            b=[]
            for i in a:
                #effacer les saut de ligne
                if (i!=""):
                    b.append(i)
            b=[l.split(' ') for l in b]#devision par rapport aux espaces
            for l in b:
                for i in l:
                    #supression des espacess
                    if i!='':
                        entree.append(i)
                entree.append("\n")
        return entree

    def translateFromFile(self,textfile,extactionMode=None):
        if extactionMode is None:
            extactionMode=self.extactionMode
        entree=Transducteur.extractInpuSequence(textfile,extactionMode)
        return self.translate(entree)

    def translate(self,entree):
        currentState='initial'
        translation=""
        for word in entree:
            if word in self.transitions[currentState]:
                out,currentState,empile=self.transitions[currentState][word]
            elif  "#O" in self.transitions[currentState]:
                out,currentState,empile=self.transitions[currentState]["#O"]
                if out=="#O":
                    out=word
            else:
                raise SyntaxError("la transition (%s,%s) n'existe pas "%(currentState,word)) 
            translation+=empile+out if self.extactionMode=="character" else " "+out+self.pile
            self.pile=empile
        return translation
            
if __name__=="__main__":     
    transExp=Transducteur("test",pourTrans)
    print(transExp.translateFromFile("Model/forFile.txt",))
