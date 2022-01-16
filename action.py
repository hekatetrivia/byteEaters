from pyexpat import features
import numpy as np

class Action(object):
    def __init__(self, wyniki):


        labels = []
        f_labels = open("wyniki")
        for line in f_labels:
            line = line.replace('\n','')
            labels.append(line)
        
        username = open('username', "r")
        username = username.read().replace(' ','')
        username = username.split(',')
        f_features = open('features', "r")
        features = f_features.read()
        features = features.replace('[','')
        features = features.replace(']','')
        features = features.split('\n')
        f_tones = open('tones', "r")
        tones = f_tones.read()
        print(labels)
        emo = []
        emo.append([])
        for j in range(0,len(features)-2):
            emotions = []
            if j == 0:
                wektor = features[j].split(',')
                wektor = [s.replace(" ", "") for s in wektor]
                if float(wektor[0]) != 0.0:
                    emotions.append(" anger ")
                if float(wektor[1]) != 0.0:
                    emotions.append(" fear ")
                if float(wektor[2]) != 0.0:
                    emotions.append(" joy ") 
                if float(wektor[3]) != 0.0:
                    emotions.append(" sadness ")
                if float(wektor[4]) != 0.0:
                    emotions.append(" analytical ")
                if float(wektor[5]) != 0.0:
                    emotions.append(" confident ") 
                if float(wektor[6]) != 0.0:
                    emotions.append(" tentative ") 
                emo[0].append(emotions)
            else:
                emo.append([])
                wektor = features[j].split(',')
                wektor = [s.replace(" ", "") for s in wektor]
                if float(wektor[0]) != 0.0:
                    emotions.append("anger")
                if float(wektor[1]) != 0.0:
                    emotions.append("fear")
                if float(wektor[2]) != 0.0:
                    emotions.append("joy") 
                if float(wektor[3]) != 0.0:
                    emotions.append("sadness")
                if float(wektor[4]) != 0.0:
                    emotions.append("analytical")
                if float(wektor[5]) != 0.0:
                    emotions.append("confident") 
                if float(wektor[6]) != 0.0:
                    emotions.append("tentative") 
                emo[j].append(emotions)
        print('username ',len(username))
        print('emo ',len(emo))
        print('tones ',len(tones))
        print(labels)
        for i in range(0,len(username)):
            #print("To jest mój prawdziwy wektor : ",features[i].split(','))    
            #print(str(labels[i]))
            if str(labels[i]) == "1":
                print("Username:", username[i], "Action: This user has expressed concerning behavior. AI has detected emotions such as", emo[i],  " and the general tone of his/her commnet was", tones[i], ". This falls under category: sick/depression. Send https://mytherapybuddy.org/free-help-hotline-depression/#free-help-hotlines-for-depression-in-the-us - help hotline specific to his/her counry")
            elif str(labels[i]) == "3":
                print("Username:", username[i], "Action: AI has detected emotions such as", emo[i],  " and the general tone of his/her commnet was", tones[i], ". This falls under category: bullying. Warn or ban him!")
            elif str(labels[i]) == "2":
                print("Username:", username[i], "Action: AI has detected emotions such as", emo[i],  " and the general tone of his/her commnet was", tones[i], ". This falls under category: agression or vulgarisms. Ban him!")
            elif str(labels[i]) == "0":
                print("Username:", username[i], "Action: No action is necessary")

