import numpy as np

def get_tones():
    tones = []
    f_tones = open("tones")
    for line in f_tones:
        line = line.replace('\n','')
        if line == 'negative':
            num_tone = np.array([1,0,0])
        elif line == 'positive':
            num_tone = np.array([0,1,0])
        elif line == 'neutral':
            num_tone = np.array([0,0,1])
        else :
            raise NameError('Wrong tones')
        tones.append(num_tone)
    return tones

def get_data():
    # Get targets
    targets = []
    f_targets = open("labels", "r")
    for line in f_targets:
        line = line.replace("\n","")
        num_target = None
        if line == 'okay':
            num_target = 0
        elif line == 'sick':
            num_target = 1
        elif line == 'aggression':
            num_target = 2
        elif line == 'bullying':
            num_target = 3
        else :
            raise NameError('Wrong target') 
        targets.append(num_target)
    f_targets.close()
    # Get data
    data = []
    f_data = open("features1", "r") 
    for line in f_data:
        # Clear the text
        txt = line.replace(",", "")
        txt = txt.replace("[","")
        txt = txt.replace("]","")
        txt = txt.replace("\n","")
        # Split text
        values = txt.split()
        temp = []
        for i in range(len(values)):
            temp.append(float(values[i]))
        temp = np.array(temp)
        data.append(temp)
    f_data.close()
    return data, targets

def main():
    X,y = get_data()
    #print(X)
    #print(y)



if __name__ == "__main__":
    main()
import numpy as np

def get_tones():
    tones = []
    f_tones = open("tones")
    for line in f_tones:
        line = line.replace('\n','')
        if line == 'negative':
            num_tone = np.array([1,0,0])
        elif line == 'positive':
            num_tone = np.array([0,1,0])
        elif line == 'neutral':
            num_tone = np.array([0,0,1])
        else :
            raise NameError('Wrong tones')
        tones.append(num_tone)
    return tones

def get_data():
    # Get targets
    targets = []
    f_targets = open("labels", "r")
    for line in f_targets:
        line = line.replace("\n","")
        num_target = None
        if line == 'okay':
            num_target = 0
        elif line == 'sick':
            num_target = 1
        elif line == 'aggression':
            num_target = 2
        elif line == 'bullying':
            num_target = 3
        else :
            raise NameError('Wrong target') 
        targets.append(num_target)
    f_targets.close()
    # Get data
    data = []
    f_data = open("features1", "r") 
    for line in f_data:
        # Clear the text
        txt = line.replace(",", "")
        txt = txt.replace("[","")
        txt = txt.replace("]","")
        txt = txt.replace("\n","")
        # Split text
        values = txt.split()
        temp = []
        for i in range(len(values)):
            temp.append(float(values[i]))
        temp = np.array(temp)
        data.append(temp)
    f_data.close()
    return data, targets

def main():
    X,y = get_data()
    #print(X)
    #print(y)



if __name__ == "__main__":
    main()
