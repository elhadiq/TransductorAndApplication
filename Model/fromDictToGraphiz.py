from os import write
from samples import *
import pydotplus

def toDot(transDict,name):
    config="""
digraph finite_state_machine {
rankdir=LR;
size="8,5"
node [shape = doublecircle];initial;
node [shape = circle];"""
    for state in transDict["Transitions"]:
        for inptword in transDict["Transitions"][state]:
            output,destination,pile=transDict["Transitions"][state][inptword]
            inpc="\\"+inptword if inptword in ['\n','\t'] else inptword
            outputc="\\"+output if output in ['\n','\t'] else output
            pilec="\\"+pile if pile in ['\n','\t'] else pile
            config+="\n"+state+" -> "+destination+' [label = "{}|{}|{}"];'.format(inpc,outputc,pilec)
    config+="\n}"
    with open(name+".dot","w") as f:
        f.write(config)

if __name__=="__main__":
    toDot(quoteSolverDict,"tograph")
    graph_a=pydotplus.graph_from_dot_file('tograph.dot')
    graph_a.write_pdf("tograph.pdf")