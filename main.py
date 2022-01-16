import os 
from nlu import Nlu
from toneanalyzer import ToneAnalyzer
from excelconversion import ExcelConversion
from action import Action

if __name__ == "__main__":
    dataset = 'dataset.xlsx'
    #Nlu(dataset)
    #ToneAnalyzer(dataset)
    #ExcelConversion(dataset)
    #os.system('python3 classifier.py')
    wyniki = 'wyniki'
    Action(wyniki)
