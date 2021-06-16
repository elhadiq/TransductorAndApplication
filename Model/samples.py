pourTrans={
    'ExtractionMode':'word',
    'InputAlphabet': {'fin','afficher','pour','dans','fair','#O','#E'},
    #O : Other segnifie tout autre charactere non declaree 
    #E : except previous ie #E=all input alphabet except what montiend
    'OutputAlphabet':{'print(','for','in',':','#O'},
    'States':{'initial','forState','varState','inState','listState','faireState','SyntaxError'},
        #On Ajout les groups pour minimiser la declaration des transitions unitiles
        #par exepmple si un ensemble des etetas peuvent aller vers un etate ei par le meme ou les meme ensemble
        # de caracteres ou mots, alors on les mets dans un groupe porte un nom significatif et on declare une seule
        # transition au lieux d'une transition par etate
    'Transitions':{
        #TODO add something to depile and empile when you want for reason of annotation
        #TODO add groups to facilitate other transitions
        'initial':{
            '#O':('#O','initial',''),
            'pour':('for','pourState',''),
            'afficher':('print("','stringToPrint','")'),
            'fin':('','finStatement','')
        },
        'finStatement':{
            'pour':('','initial','/t'),
            'si':('','initial','/t'),
            'tant':('','initial',''),
            'que':('','initial','/t')
        }
        ,
        'stringToPrint':{
            '#O':('#O','initial',''),
        },
        'pourState':{
            '#O':('#O','varState','')
        },
        'varState':{
            'dans':('in','inState',''),
            'allant':('','varState',''),
            'de':('in range(','allantDe','')
        },
        'allantDe':{
            "#O":('#O','deb','')
        },
        'deb':{
            "à":(',','Jusqua',''),
            "jusqu'à":(',','Jusqua','')
        },
        'Jusqua':{
            "#O":('#O','dernier','')

        },  
        'dernier':{
            'faire':('):','initial','\t'),
            'pas':(',','pasState','')
        },
        'pasState':{
            "#O":('#O','lePas','')
        },
        'lePas':{
            'faire':('):','initial','\t'),
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
        #pour la pile :#UC: segnifie use and and conserve 
        'changerState':{
            '#O':('#O','changerState',''),
            ' ':('_','changerState',''),
            '"':('','initial','')
        }
}}


UnderScoreAndNewlineDeleter={
    'ExtractionMode':'character',
    'InputAlphabet': {'\t','\n','_','#O'},
    #O : Other segnifie tout autre charactere non declaree 
    #E : except previous ie #E=all input alphabet except what montiend
    'OutputAlphabet':{'_','\n','#O'},
    'States':{'initial','newline','underscored'},
    'Transitions':{
        'initial':{
            # inAlphabet : (Outlphabet,OngoingState,PileElement)
            '#O':('#O','initial',''),
            '_':(' ','underscored',''),
            '\n':('\n','newline','')
            },
        'newline':{
            '#O':('#O','initial',''),
            '_':('','underscored',''),
            '\n':('','newline',''),

        },
        'underscored':{
            '#O':('#O','initial',''),
            '_':('','underscored',''),
            '\n':('\n','newline','')
        }
    }
}