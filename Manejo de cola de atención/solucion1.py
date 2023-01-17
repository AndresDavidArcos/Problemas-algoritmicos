import numpy as np

def minMax(array):
     min = array[0]
     max = array[0]

     for i in range(1, len(array)):
        if(array[i]>max):
            max = array[i]
        elif(array[i]<min):
            min = array[i]  

     return {'min': min,'max': max}

def countingSort(arr):
    minMaxDictionary = minMax(arr)
    min = minMaxDictionary['min']
    max = minMaxDictionary['max']
    countArrayLength = max-min+1
    countArray = np.zeros(shape=countArrayLength)
    for key, element in enumerate(arr):
        countArray[element-min] = countArray[element-min]+1

    arrIndex = 0
    for i in range(countArrayLength):
        while(countArray[i]>0):
            arr[arrIndex] = i+min
            countArray[i] = countArray[i]-1
            arrIndex = arrIndex + 1
print("____countingSort Test____")
testArr = [5,3,8,12,23,-2,-5,-2,0]
print(testArr)
countingSort(testArr)
print(testArr)
print("____countingSort Test____End")

def selectBigOfLessThan(orderedTimes, lessThan):
    response = -1
    if(lessThan == 0):
        return response
    for i in range(len(orderedTimes)):  
            client = orderedTimes[i]
            if(client['timeRequired'] == lessThan):
                response = {'killPosition': i, 'client': client}
                break
            elif(client['timeRequired'] < lessThan):
                response = {'killPosition': i, 'client': client}
            else:
                break
    return response

def labelClients(clients):
    for arrivalOrder in range(len(clients)):
        timeRequired = clients[arrivalOrder]
        clients[arrivalOrder] = {'arrivalOrder': arrivalOrder, 'timeRequired': timeRequired}


def findTimeAndReturnLabel(timeRequired, clientsLabels):
    for i in range(len(clientsLabels)):
        clientLabelTime = clientsLabels[i]
        if(timeRequired == clientLabelTime):
            return i
    return -1

def labelOrderedClients(orderedTimes, timesArr):
    arrHelper = timesArr.copy()
    for i in range (len(orderedTimes)):
        timeRequired = orderedTimes[i]        
        labelFinded = findTimeAndReturnLabel(timeRequired, arrHelper)
        arrHelper[labelFinded] = -1
        orderedTimes[i] = {'arrivalOrder': labelFinded, 'timeRequired': timeRequired}

def findClient(arrivalOrderSearched, clients):
    for i in range(len(clients)):
        client = clients[i]
        arrivalOrder = client['arrivalOrder']
        if(arrivalOrderSearched == arrivalOrder):
            return i
    return -1
 
def selectBestAttentionPost(numClients, tMax, timesArr):
    finalResponse = []

    orderedTimes = timesArr.copy()
    countingSort(orderedTimes)
    labelOrderedClients(orderedTimes, timesArr)
    labelClients(timesArr)

    timesArrLength = len(timesArr)
    while(timesArrLength!=0):
            client = timesArr[0]
            del timesArr[0]
            timeRequired = client['timeRequired']
            arrivalOrder = client['arrivalOrder']
            officeBucket = []
            officeBucket.append(client)
            killPosition = findClient(arrivalOrder, orderedTimes)
            del orderedTimes[killPosition]

            response = selectBigOfLessThan(orderedTimes, tMax-timeRequired)
            totalOfficeTime = timeRequired
            while(response != -1 and totalOfficeTime != tMax):
                killOrderPosition = response['killPosition']
                clientResponse = response['client']
                killTimesArrPosition = findClient(clientResponse['arrivalOrder'], timesArr)

                officeBucket.append(clientResponse)
                del orderedTimes[killOrderPosition]
                del timesArr[killTimesArrPosition]
                totalOfficeTime = totalOfficeTime + clientResponse['timeRequired']
                response = selectBigOfLessThan(orderedTimes, tMax-totalOfficeTime)
                

            finalResponse.append(officeBucket)
            timesArrLength = len(timesArr)


    return finalResponse       

def printPrettyInfo(offices):
    officesLength = len(offices)
    print("Si tenemos", officesLength, "oficinas, podemos atender a los clientes de la siguiente manera: \n")
    for officeNum in range(officesLength):
        office = offices[officeNum]
        officeTotalTimes = 0
        clientsBeforeMe = []
        for clientPosition in range(len(office)):
            client = office[clientPosition]
            arrivalOrder = client['arrivalOrder']+1
            timeRequired = client['timeRequired']
            if(clientPosition == 0):
                print("- El cliente", arrivalOrder, "llega al puesto", officeNum+1, "su atención demora", timeRequired, "unidades de tiempo.")
                officeTotalTimes += timeRequired
                clientsBeforeMe.append(arrivalOrder)
            else:
                officeTotalTimes += timeRequired

                print("- El cliente", arrivalOrder, "llega al puesto", officeNum+1, "su atención demora", timeRequired, "unidades de tiempo,\n pero debe esperar", officeTotalTimes-timeRequired, "más a que terminela atención del ")
                for clientNum in clientsBeforeMe:
                    print("cliente", clientNum, ",")
                print(" por lo que en total serían", officeTotalTimes, "unidades de tiempo.")                
                clientsBeforeMe.append(arrivalOrder)
                


            
print("____selectBestAttentionPost Test____")
offices = selectBestAttentionPost(5,8,[4,7,8,6,4]) 
print(offices)
print("____selectBestAttentionPost Test____End")

printPrettyInfo(offices)




