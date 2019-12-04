from colour import Color

def tagToColor(tags: list): #a list of tags by store
    colorDict = {"Food and Dining":"red",
    "Shopping":"blue", 
    "Home":"blue",
    "Entertainment":"purple",
    "Auto and Transport":"green"}
    return list(map (lambda x : colorDict[x], tags))
def create_hue(colours: list): # a list of colors by store
    hueDict = {"red":0, "blue":(245/360),"green":(117/360),"purple":(291/360)}
    return list(map (lambda x : hueDict[x], colours))
def create_lumin(freq: list): # a list of freq by store
    minv, maxv = min(freq), max(freq)
    diff = maxv-minv
    return list(map (lambda x : (120-(50+(x-minv) / (diff) * 20))/100 , freq)) 
def create_color(hue:list, lum:list): # return a list of colors in hex
    colors = []
    sat = 1
    huelumTuples = zip(hue,lum)
    for h, l in huelumTuples:
        colors.append(Color(hsl=(h, sat, l)))
    return list(map(lambda c: c.hex, colors))

#testing data
#tags = ["Food and Dining", "Shopping", "Entertainment", "Auto and Transport"] # get tag list
#freqs = [20, 5, 10, 20, 50] # get freq list

#colors = create_color(create_hue(tagToColor(tags)), create_lumin(freqs))
#print(colors)
