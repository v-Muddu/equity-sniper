

# Function to find the pivot low with alternating pivots or finding the highest between two pivots low or vice cersa
def find_pivot(pivottype, df):
    pivots =[]
    dates = []
    counter = 0
    Range = [0 for _ in range(10)]
    dateRange = [0 for _ in range(10)]

    for i in df.index:
        currentMin = min(Range,default = 0)
        currentMax = max(Range,default = 0)
        value = round(df[pivottype][i], 2)
        Range = Range[1:9]
        Range.append(value)
        dateRange = dateRange[1:9]
        dateRange.append(i)

        if currentMax == max(Range, default=0):
            counter = counter + 1
        elif currentMin == min(Range, default=0):
            counter = counter + 1
        else:
            counter = 0

        if counter == 5:
            lastPivot = currentMin
            if pivottype == "High":
                lastPivot = currentMax
            dateloc = Range.index(lastPivot)
            lastDate = dateRange[dateloc]
            pivots.append(lastPivot)
            dates.append(lastDate)
            
    return pivots,dates


def pivothigh(df):
    """ Function to find the pivot high with alternating pivots or fidning the lowest between two pivots high or vice cersa"""

    pivots =[]
    dates = []
    counter = 0
    lastPivot = 0
    Range = [0,0,0,0,0,0,0,0,0,0]
    daterange = [0,0,0,0,0,0,0,0,0,0]

    for i in df.index:

        currentMax = max(Range,default = 0)
        value=round(df["High"][i],2)

        Range=Range[1:9]
        Range.append (value)
        daterange=daterange[1:9]
        daterange.append(i)

        if currentMax == max(Range , default=0):
            counter = counter + 1
        else:
            counter = 0

        if counter == 5:

            lastPivot=currentMax
            dateloc =Range.index(lastPivot)
            lastDate = daterange[dateloc]
            pivots.append(lastPivot)
            dates.append(lastDate)
            
    return pivots,dates


def pivotlow(df):
    pivots1 =[]
    dates1 = []
    counter = 0
    lastPivot = 0
    Range = [0,0,0,0,0,0,0,0,0,0]
    daterange = [0,0,0,0,0,0,0,0,0,0]

    for i in df.index:

        currentMin = min(Range,default = 0)
        value = round(df["Low"][i],2)

        Range = Range[1:9]
        Range.append (value)
        daterange = daterange[1:9]
        daterange.append(i)

        if currentMin == min(Range ,default=0):
            counter = counter + 1
        else:
            counter = 0

        if counter == 5:

            lastPivot = currentMin
            dateloc = Range.index(lastPivot)
            lastDate = daterange[dateloc]
            pivots1.append(lastPivot)
            dates1.append(lastDate)
            
    return pivots1,dates1