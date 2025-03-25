print(__name__)
# __name__= __main__ , che succede?
# lanciare 'python {nome file}', __name__=__main__
#  se il file è lanciato indirettamente (perchè importato),  __name__!=__main__

# se non mi interessano i changes, quando chiudo i file invece che fare commit faccio discard 

# per fare questa cosa, comunque i file devonoessere nella stessa cartella
# altriemnti dà errore
# per permettere di importare da file fuori dalla cartella devo fare:
sys.path.append(os.path.abspath('..'))  
# questa riga dice ' considera cil path a partire da '..' (cioè 'torna indietro')

