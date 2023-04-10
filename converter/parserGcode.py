import re

def parseGcode(pathToFile):
        gcodeList = []
        for line in pathToFile:
              a = re.split(r'\(', str(line))
              b = a[0]
              c = re.findall(r'[GXYZPFRMDLIJKL0-9.-]+', b)
              if c!=[]:
                gcodeList.append(c)
        return gcodeList

# parseGcode('Z:\нехаккатон\пиранья (300на150).tap')