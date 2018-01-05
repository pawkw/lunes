import ephem
import datetime

# An "observer" for Kitchener
kitchener = ephem.Observer()
kitchener.lat = '43:29'
kitchener.lon = '-80:20'
kitchener.elevation = 300
kitchener.compute_pressure()

# Global moon object.
moon = ephem.Moon()

# Time corrected to local time.
def correctTime(date):
    return ephem.date(ephem.localtime(date).replace(microsecond=0)) # This is painful.

# Lunar "day" object.
# A lunar "day" is from moon rise to moon rise.
# Expects a ephem.Observer, location, with the date set to before the moon rise.
# Returns with the location date set to the moon rise of that day.
class lune(object):
    def __init__(self, location, month, number):
        moon.compute(location)
        start = location.next_rising(moon)
        self.phase = moon.moon_phase
        self.RA = moon.ra
        location.date = start
        end = location.next_rising(moon)
        self.hours = (end - start) * 24
        location.date = start
        self.start = correctTime(start)
        self.end = correctTime(end)
        self.month = month
        self.lune = number

    def __str__(self):
        return str(self.month)+'/'+str(self.lune) \
        +" Start: "+str(self.start)+" end: "+str(self.end) \
               + " hours: %.2f" % self.hours \
               + " phase: %.2f" % self.phase

    def detail(self):
        print(self)

# Lunar month object.
# A lunar month is from new moon to new moon.
# Expects the location date to be set to some time before the new moon.
# Returns with location date set to the moon rise of the last lune of the month.
class luneMonth(object):
    def __init__(self, location, number):
        self.luneList = []
        newMoon = ephem.next_new_moon(location.date) - 0.5
        location.date = newMoon
        moon.compute(location)
        nextMonth = ephem.next_new_moon(location.date+3) - 0.5
        count = 0
        while location.next_rising(moon) < nextMonth:
            count += 1
            self.luneList.append(lune(location, number, count))
        self.lunes = len(self.luneList)
        self.start = self.luneList[0].start
        self.end = self.luneList[-1].end
        self.number = number

    def __str__(self):
        return "Start: "+str(self.start)+" end: "+str(self.end)+" lunes: " \
               +str(self.lunes)

    def detail(self):
        for x in self.luneList:
            print(x)
        print('='*10)
        print(self)

    def summary(self):
        print(self)

class luneYear(object):
    def __init__(self, year):
        self.monthList = []
        # TODO: Allow the user to pick their own location.
        self.location = kitchener
        self.start = self.getStart(year) - 1.0
        end = self.getStart(year + 1) - 5.0
        self.location.date = self.start
        count = 0
        while self.location.date < end:
            count += 1
            self.monthList.append(luneMonth(self.location, count))
        self.start = self.monthList[0].start
        self.end = self.monthList[-1].end
        self.months = len(self.monthList)
        self.year = year
        self.lunes = 0
        for x in self.monthList:
            self.lunes += x.lunes

    def getStart(self, year):
        start = ephem.date(str(year)+'/1/1')
        start = ephem.next_vernal_equinox(start)
        start = ephem.previous_new_moon(start)
        self.location.date = start
        moon.compute(self.location)
        start = self.location.next_rising(moon)
        return start
    
    def detail(self):
        count = 1
        for month in self.monthList:
            print(count, month)
            count += 1
        print('='*10)
        print(self)

    def summary(self):
        print(self)

    def month(self, month):
        return self.monthList[month-1]

    def lune(self, month, lune):
        return self.month(month).luneList[lune-1]

    def find(self, month, day, hour=0, minute=0, second=0, year = 0):
        if year == 0:
            date = ephem.date((self.year, month, day, hour, minute, second))
            if date < self.start or date > self.end:
                date = ephem.date((self.year+1, month, day, hour, minute, second))
        else:
            date = ephem.date((year, month, day, hour, minute, second))
        
        if date < self.start or date > self.end:
            return False
        
        month = 0
        for x in self.monthList:
            month += 1
            if date < x.end:
                break
        lune = 0
        for x in self.month(month).luneList:
            lune += 1
            if date < x.end:
                break
        if lune == 0:
            print("Lune could not be found.")
            quit()
        return month, lune

    def printLunes(self, month, day, hour=0, minute=0, second=0):
        x = self.find(month, day, hour, minute, second, self.year)
        if x:
            print(self.lune(*x))
        x = self.find(month, day, hour, minute, second, self.year+1)
        if x:
            print(self.lune(*x))

    def __str__(self):
        return "Start: "+str(self.start)+" end: "+str(self.end)+" months: " \
               +str(self.months)+" lunes: "+str(self.lunes)
        
# Main subroutine
if __name__ == "__main__":
    kitchener.date = datetime.datetime.now()
    # Extract the current year.
    year = luneYear(kitchener.date.tuple()[0])
    year.detail()
