import os 
import json
import numpy as np
import json
import openpyxl


class ToneAnalyzer(object):
    def __init__(self, dataset):
        workbook = openpyxl.load_workbook(dataset)
        sheet = workbook.active
        features = []

        listaa = []
        for i in range(1,209):
            listaa.append(sheet.cell(i,2).value)

        for k in range(0,len(listaa)):
            input = {'text':[]}
            input['text'] = listaa[k]
            out_file = open("input_json.json", "w")
            json.dump(input, out_file, indent = 4, sort_keys = False)
            out_file.close()
            os.system('curl -X POST -u "apikey:QrIBRLIWwew1m_y8i8NQTRFmcM_9OA9a7AdYVvDv-zrj" \
            --header "Content-Type: application/json" \
            --data-binary @/home/hekatetrivia/hackaton/input_json.json \
            "https://api.au-syd.tone-analyzer.watson.cloud.ibm.com/instances/ab96e30a-8c4e-4e56-af33-05f26ae39bea/v3/tone?version=2017-09-21" > output.json')

            f = open ('output.json', "r")
            data = json.loads(f.read())
            
            if data.get('sentences_tone') != None:
                lista = []
                for j in range(0,len(data['sentences_tone'])):
                    #print(data['sentences_tone'][j])
                    vector = [0, 0, 0, 0, 0, 0, 0]
                    for i in range(0,len(data['sentences_tone'][j]['tones'])):
                        if data['sentences_tone'][j]['tones'][i]['tone_id'] == 'anger':
                            vector[0] = data['sentences_tone'][j]['tones'][i]['score']
                        if data['sentences_tone'][j]['tones'][i]['tone_id'] == 'fear':
                            vector[1] = data['sentences_tone'][j]['tones'][i]['score']
                        if data['sentences_tone'][j]['tones'][i]['tone_id'] == 'joy':
                            vector[2] = data['sentences_tone'][j]['tones'][i]['score']
                        if data['sentences_tone'][j]['tones'][i]['tone_id'] == 'sadness':
                            vector[3] = data['sentences_tone'][j]['tones'][i]['score']
                        if data['sentences_tone'][j]['tones'][i]['tone_id'] == 'analytical':
                            vector[4] = data['sentences_tone'][j]['tones'][i]['score']
                        if data['sentences_tone'][j]['tones'][i]['tone_id'] == 'confident':
                            vector[5] = data['sentences_tone'][j]['tones'][i]['score']
                        if data['sentences_tone'][j]['tones'][i]['tone_id'] == 'tentative':
                            vector[6] = data['sentences_tone'][j]['tones'][i]['score']

                    lista.append(vector)    
                lista = np.array(lista)
                lista = np.max(lista, axis = 0)
                lista = list(lista)

            else:
                vector = [0, 0, 0, 0, 0, 0, 0]
                for i in range(0,len(data['document_tone']['tones'])):
                        if data['document_tone']['tones'][i]['tone_id'] == 'anger':
                            vector[0] = data['document_tone']['tones'][i]['score']
                        if data['document_tone']['tones'][i]['tone_id'] == 'fear':
                            vector[1] = data['document_tone']['tones'][i]['score']
                        if data['document_tone']['tones'][i]['tone_id'] == 'joy':
                            vector[2] = data['document_tone']['tones'][i]['score']
                        if data['document_tone']['tones'][i]['tone_id'] == 'sadness':
                            vector[3] = data['document_tone']['tones'][i]['score']
                        if data['document_tone']['tones'][i]['tone_id'] == 'analytical':
                            vector[4] = data['document_tone']['tones'][i]['score']
                        if data['document_tone']['tones'][i]['tone_id'] == 'confident':
                            vector[5] = data['document_tone']['tones'][i]['score']
                        if data['document_tone']['tones'][i]['tone_id'] == 'tentative':
                            vector[6] = data['document_tone']['tones'][i]['score']
                lista = vector


            features.append(lista)
            f.close()

        #with open('features', 'w') as f:
        #    f.write(str(features))

        with open('features', 'w') as f:
            #f.write(str(labels))
            for i in range(len(features)):
                f.write(str(features[i]))
                f.write('\n')    