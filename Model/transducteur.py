from State import State
class Transducteur:
    def __init__(self):
        self.inAlphabet=[]
        self.outAlphabet=[]
        self.states=[]
    def readTransducteur(self,file_name):
         with open(file_name, "r") as f_auto:
            a_src = f_auto.read().split('\n')[:-1]
            self.inAlphabet.extend(a_src[0].split(',')[1:])
            i=self.inAlphabet.index("\\n")
            if i!=-1:
                self.inAlphabet[i]="\n"
            self.outAlphabet.extend(a_src[1].split(',')[1:])
            i=self.outAlphabet.index("\\n")
            if i!=-1:
                self.inAlphabet[i]="\n"
            self.states = {number:State(number) for number in a_src[2].split(',')[1:]}
            for line in a_src[4:]:
                split_line = line.split(':')
                depart,inCharacter,ouCarachter,destination=tuple(split_line)
                if inCharacter=="\\n":
                    inCharacter="\n"
                if ouCarachter=="\\n":
                    ouCarachter="\n"
                self.states[depart].affect([inCharacter],[ouCarachter],[destination])