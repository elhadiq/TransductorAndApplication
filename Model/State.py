class State:
    ## Toutes les etats sont determinises
    def __init__(self,number):
        self.number=number
        self.succesors=dict()

    def affect(self,inputCharacters,outputCharacters,destinationStates):
        if not( len(inputCharacters)-len(outputCharacters)==len(outputCharacters)-len(destinationStates)):
            raise Exception("Not the same lenght for input output and distination")
        for inputChar,outputChar,destination in zip(inputCharacters,outputCharacters,destinationStates):
            self.succesors[inputChar]=(outputChar,destination)

    def __eq__(self,state):
        ##Deux etats qui ont le meme nom sont identiques
        return self.number==state.number
    def final(self,isFinal=False):
        self.__setattr__("final",isFinal)
    def isFinal(self):
        return self.final
