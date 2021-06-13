pourTrans={
    'ExtractionMode':'word',
    'InputAlphabet': {'afficher','pour','dans','fair','#O','#E'},
    #O : Other segnifie tout autre charactere non declaree 
    #E : except previous ie #E=all input alphabet except what montiend
    'OutputAlphabet':{'print(','for','in',':','#O'},
    'States':{'initial','forState','varState','inState','listState','faireState','SyntaxError'},
        #On Ajout les groups pour minimiser la declaration des transitions unitiles
        #par exepmple si un ensemble des etetas peuvent aller vers un etate ei par le meme ou les meme ensemble
        # de caracteres ou mots, alors on les mets dans un groupe porte un nom significatif et on declare une seule
        # transition au lieux d'une transition par etate
    'Transitions':{
        'initial':{
            '#O':('#O','initial',''),
            'pour':('for','forState',''),
            'afficher':('print("','stringToPrint','")\n')
        },
        'stringToPrint':{
            '#O':('#O','initial',''),
        },
        'forState':{
            '#O':('#O','varState','')
        },
        'varState':{
            'dans':('in','inState','')
        },
        'inState':{
            '#O':('#O','listState','')
        },
        'listState':{
            'faire':(':','initial','\t')
        },

}}
test={
    'ExtractionMode':'word',
    'InputAlphabet': {'#O'},
    #O : Other segnifie tout autre charactere non declaree 
    #E : except previous ie #E=all input alphabet except what montiend
    'OutputAlphabet':{'#O'},
    'States':{'initial'},
    'Transitions':{
        'initial':{
            # inAlphabet : (Outlphabet,OngoingState,PileElement)
            '#O':('#O','initial','')
}
    }
}
quoteSolverDict={
    'ExtractionMode':'character',
    'InputAlphabet': {' ','"','#O'},
    #O : Other segnifie tout autre charactere non declaree 
    #E : except previous ie #E=all input alphabet except what montiend
    'OutputAlphabet':{' ','_','#O'},
    'States':{'initial','changerState'},
    'Transitions':{
        'initial':{
            # inAlphabet : (Outlphabet,OngoingState,PileElement)
            '#O':('#O','initial',''),
            '"':('','changerState','')
        },
        'changerState':{
            '#O':('#O','changerState',''),
            ' ':('_','changerState',''),
            '"':('','initial','')
        }
}}