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
            self.outAlphabet.extend(a_src[1].split(',')[1:])
            self.states = {number:State(number) for number in a_src[2].split(',')[1:]}
            for line in a_src[4:]:
                split_line = line.split(':')
                self.states[split_line[0]].affect([split_line[1]],[split_line[2]],[split_line[3]])