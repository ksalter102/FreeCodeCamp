def add_time(start, duration, dow="False"):
    rep = start.replace(":", " ")  # obtain values
    spl = rep.split()
    shour = spl[0]
    smnts = spl[1]
    sam = spl[2]
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # dict?
    pday = 0

    if sam == "AM":
        isam = True
    else:
        isam = False

    dspl = duration.split(":")  # obtain values
    dhour = dspl[0]
    dmnts = dspl[1]

    nhour = int(shour) + int(dhour)  # calculate new values
    nmnts = int(smnts) + int(dmnts)

    while nmnts > 60:  # minutes create new hours
        nmnts = nmnts - 60
        nhour = nhour + 1
    while nhour > 12:  # 12 hours swaps AM and PM - NEED TO COUNT DAYS LATER
        nhour = nhour - 12
        if isam:
            isam = False
        else:
            isam = True
            pday = pday + 1
    if nhour == 12:
        if isam:
            isam = False
        else:
            isam = True
            pday = pday + 1

    nmnts = str(nmnts)  # add 0 to single digit minute
    if len(nmnts) < 2:
        nmnts = "0" + nmnts

    if isam:  # converting isam from bool to str
        isam = "AM"
    elif not isam:
        isam = "PM"

    if dow != "False":
        dayi = days.index(dow.lower())
        newdayi = dayi + pday
        while newdayi > 6:
            newdayi = newdayi - 7
        newdow = days[newdayi].title()

    if dow == "False" and pday == 0:  # calculate new time
        new_time = str(nhour) + ":" + str(nmnts) + " " + isam
    elif dow == "False" and pday == 1:
        new_time = str(nhour) + ":" + str(nmnts) + " " + isam + " (next day)"
    elif dow == "False" and pday > 1:
        new_time = str(nhour) + ":" + str(nmnts) + " " + isam + " (" + str(pday) + " days later)"
    elif dow != "False" and pday == 0:
        new_time = str(nhour) + ":" + str(nmnts) + " " + isam + ", " + dow
    elif dow != "False" and pday == 1:
        new_time = str(nhour) + ":" + str(nmnts) + " " + isam + ", " + newdow + " (next day)"
    else:
        new_time = str(nhour) + ":" + str(nmnts) + " " + isam + ", " + newdow + " (" + str(pday) + " days later)"

    return new_time