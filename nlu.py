import os 
import json
import numpy as np
import json
import openpyxl


class Nlu(object):
    def __init__(self, dataset):
        workbook = openpyxl.load_workbook(dataset)
        sheet = workbook.active
        tones = []
        listaa = []
        for i in range(1,209):
            listaa.append(sheet.cell(i,2).value)

        for k in range(0,len(listaa)):
            input = {'text':[]}
            input['text'] = listaa[k]
            out_file = open("input_json.json", "w")
            json.dump(input, out_file, indent = 4, sort_keys = False)
            out_file.close()

            s = open('input_json.json', "r")
            text = json.loads(s.read())
            text=text['text'].replace('\'',' ')
            text=text.replace('\"',' ')
            text=text.replace('..',' ')
            text=text.replace('...',' ')
            text=text.replace('....',' ')
            text=text.replace('&',' ')
            text=text.replace('#',' ')
            text=text.replace('%',' ')
            text=text.replace('?',' ')
            print(text)
            os.system('''curl -X POST -u "apikey:iXniQYS4afHEvMn5qqS4Gvyhk9e5Y_qbkBOtt7waaN3R" \
                --header "Content-Type: application/json" \
                --data '{
                "text":  "'''+ str(text) +'''",
                "features": {
                    "sentiment": {}
                },
                "language" : "en"
                }' \
                "https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com/instances/7561112d-ef92-492f-af9a-674fbcd10b3a/v1/analyze?version=2019-07-12" > output.json ''')

            s.close()

            f = open ('output.json', "r")
            data = json.loads(f.read())
            tones.append(data['sentiment']['document']['label'])

        with open('tones', 'w') as f:
            #f.write(str(labels))
            for i in range(len(tones)):
                f.write(str(tones[i]))
                f.write('\n') 
        

