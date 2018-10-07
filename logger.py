import logging
import logging.handlers
from pytz import timezone
from datetime import datetime
import os
import sys
import traceback
class logger(object):
    CMD_Path = str(os.path.dirname(__file__)) + '/LOGS/'
    if not os.path.exists(CMD_Path):
        os.makedirs(CMD_Path)
    Paris_time = datetime.now(timezone('Europe/Paris'))
    Formatted_time = Paris_time.strftime('%d.%m.%Y_%HH%M')
    LogName = CMD_Path + 'OSERIS_HISTORY_' + Formatted_time + '.log'
    def __init__(self,name=LogName):
        #Spécification du chemin de la log
        # création de l'objet logger qui va nous servir à écrire dans les logs
        self.logger = logging.getLogger()
        # on met le niveau du logger à DEBUG, comme ça il écrit tout
        self.logger.setLevel(logging.DEBUG)
        # création d'un formateur qui va ajouter le temps, le niveau
        # de chaque message quand on écrira un message dans le log
        self.formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
        # création d'un handler qui va rediriger une écriture du log vers      
        # un fichier en mode 'append', avec 1 backup et une taille max de 10Mo    
        self.filehandler = logging.handlers.RotatingFileHandler(name,'a',10000000,1,'UTF-16')
        # on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
        self.filehandler.setLevel(logging.DEBUG)
        self.filehandler.setFormatter(self.formatter)
        # créé précédement et on ajoute ce handler au logger
        self.logger.addHandler(self.filehandler)
        #creation d'un handler pour la console
        self.consoleHandler = logging.StreamHandler()
        # adopter le meme formatteur que le fileHandler
        self.consoleHandler.setFormatter(self.formatter)
        # Ajouter le console Handler au logger
        self.logger.addHandler(self.consoleHandler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)
    
    def extract_function_name(self):
        #Extracts failing function name from Traceback
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        fname = stk[0][2]
        fline = stk[0][3]
        return fname, fline

    def ExceptionErr(self,e,*var):
        self.logger.error("Function '{function_name}{arguments}' raised an error at line '{function_line}' :: CAUSE : {exception_docstring} :: MESSAGE : {exception_message}".format(
        function_name = self.extract_function_name()[0], #this is optional
        function_line = self.extract_function_name()[1], #error line in function
        arguments= str(var),
        exception_docstring = e.__doc__,
        exception_message = str(e)))

