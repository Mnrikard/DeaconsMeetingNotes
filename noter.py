#!/usr/bin/env python
import time
import sys

class noter:
    deaconFile = "/home/rugg/deacons"
    staffFile = "/home/rugg/churchStaff"

    template = """# Deacons Meeting
#### tttttt

***attendance***
mmmmmm

## Old Business

_oldBusinessGoesHere_

## New Business

_newBusinessGoesHere_

## Pastor's Time

_pastorsTimeGoesHere_
"""
    def getMeetingDate(self):
        localtime   = time.localtime()
        timeString  = time.strftime("%b %d, %Y", localtime)
        print("Date: ["+timeString+"]:")
        promptedTime = sys.stdin.readline()
        if(promptedTime.strip() != ""):
            timeString = promptedTime
        return timeString

    def getSpecificAttendance(self, arrFile, arrName):
        output = "**"+arrName+" Present:**"
        absent = []
        present = []

        attendees = open(arrFile,"r")
        arr = attendees.readlines()

        for d in arr:
            print(d+"[Yn]:")
            here = sys.stdin.readline()
            if(here.lower().strip() == "n"):
                absent.append(d)
            else:
                present.append(d)

        output = output + (", ".join(present)) + "\n\n"

        if len(absent) > 0:
            output = output + "**"+arrName+" Absent:**"
            output = output + (", ".join(absent)) + "\n\n"
        return output

    def getAttendance(self):
        return self.getSpecificAttendance(self.deaconFile, "Deacons") + self.getSpecificAttendance(self.staffFile, "Staff")

    def getMinutes(self):
        print("When was the meeting called to order?")
        start = sys.stdin.readline().strip()
        print("When were prayer requests started?")
        prayerRequest = sys.stdin.readline().strip()
        print("When did the prayer start?")
        prayer = sys.stdin.readline().strip()
        print("When did the prayer cease?")
        cease = sys.stdin.readline().strip()
        print("When were the minutes reviewed?")
        review = sys.stdin.readline().strip()
        print("When was old/new business?")
        biz = sys.stdin.readline().strip()
        print("When did the pastor's time start?")
        pastor = sys.stdin.readline().strip()
        print("When was the benediction?")
        benediction = sys.stdin.readline().strip()

        return """| Time | Event                                   |
|------|-----------------------------------------|
| """+start+""" | Meeting called to order.                |
| """+prayerRequest+""" | Prayer requests started                 |
| """+prayer+""" | Prayer started                          |
| """+cease+""" | Prayer fulfilled.                       |
| """+review+""" | Minutes missing from last meeting       |
| """+biz+""" | Old business/New business               |
| """+pastor+""" | Pastor's time                           |
| """+benediction+""" | Benediction                             |
"""

def getYear(time):
    import re
    return re.search("\d{4}", time).group(0)

def getMonth(time):
    import re
    return re.search("\w+", time).group(0)

if __name__ == "__main__":
    n = noter()
    output = n.template
    time = n.getMeetingDate()
    output = output.replace("tttttt",time)
    output = output.replace("***attendance***",n.getAttendance())
    output = output.replace("mmmmmm", n.getMinutes())
    
    outfile = "archivedNotes/"+getYear(time)+"/"+getMonth(time)+".md"
    f = open(outfile,"w")
    f.write(output)
    f.close()

    print(outfile)



