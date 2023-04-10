import re

def parseGcode(pathToFile):
        file = open(pathToFile)
        gcodeList = []
        for line in file:
              a = re.split(r'\(', str(line))
              b = a[0]
              c = re.findall(r'[GXYZPFRMDLIJKL0-9.-]+', b)
              if c!=[]:
                gcodeList.append(c)
        return gcodeList