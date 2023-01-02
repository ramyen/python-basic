
import array


templist = [1,"스트링",4.0,]
for i in range(len(templist)):
    print(templist[i])

tempArray = array.array('u', ['ㄱ', 'ㅏ'])
for element in tempArray:
    print(element)

print(tempArray.typecode)