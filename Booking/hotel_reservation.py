# coding=utf-8
"""
You are building a small command-line application to calculate hotel availability for a city.
Your application reads in two (2) data files, and outputs its answer to STDOUT.
Your application will read in:
· a list of hotels along with how many rooms each contains (in no particular order)
· a list of bookings that have been made (in no particular order)
Your application will then print the list of all hotels which have availability for check-in and check- out date range, if any.
Do not worry about whether a specific room is available in a hotel for the entire booking period without switching rooms:
availability is defined as the hotel having at least one (1) available room for each night of the target stay,
regardless of whether it's the same room from day to day.

Data Files
hotels.csv
# Name, Rooms
Westin, 10
Best Western, 20
Hilton, 10
...

bookings.csv
# Name, Checkin, Checkout
Hilton, 2015-04-02, 2015-04-03
Hilton, 2015-04-02, 2015-04-04
Westin, 2015-05-01, 2015-05-20

http://www.careercup.com/question?id=5724864499417088
http://pastebin.com/zfeDGTPU
"""
import datetime
import csv


class Hotel:
    def __init__(self, hotel, free):
        self.hotels = {hotel: free}

    def reserve(self, hotel, start, end):
        start_d = self._dateParse(start)
        end_d = self._dateParse(end)
        # num = self._datesDifferance(start_d, end_d)

        if self.hotels[hotel] > 0:
            self.hotels[hotel] -= 1
            self.hotels[hotel].rooms[hotel].append({'f': start_d, 't': end_d})
        else:
            print "No Rooms"

    def _dateParse(self, d):
        return datetime.datetime.strftime(d, '%Y-%m-%d')

    def _datesDifferance(self, d1, d2):
        assert d2 > d1
        return abs((d2 - d1)).days

dict = {}
def readHotels():
    with open('hotel_reservation', 'rb') as csvfile:
        sreader = csv.reader(csvfile, delimiter=',')
        for line in sreader:
            dict[line[0]] = Hotel(line[0], int(line[1]))

    x = 0


readHotels()

class hisHotel:
    def __init__(self, rooms):
        self.rooms = [rooms]


class HotelsCalculater(object):
    def __init__(self):
        self.__hotels = {}

    def getDate(self, str):
        return datetime.date(*map(int, str.strip().split('-')))

    def readHotels(self):
        with open('hotel_reservation', 'rb') as csvfile:
            sreader = csv.reader(csvfile, delimiter=',')
            for line in sreader:
                self.__hotels[line[0]] = hisHotel(int(line[1]))

        with open('hotel_reservation_booking', 'rb') as csvfile:
            sreader = csv.reader(csvfile, delimiter=',')
            for line in sreader:
                # print line
                # print self.__hotels
                date1 = self.getDate(line[1])
                date2 = self.getDate(line[2])
                self.__hotels[line[0]].rooms.append((date1, 1))
                self.__hotels[line[0]].rooms.append((date2, 0))

        for hotel in self.__hotels:
            currCount = 0
            self.__hotels[hotel].rooms = sorted(self.__hotels[hotel].rooms)
            for i in xrange(len(self.__hotels[hotel].rooms)):
                if self.__hotels[hotel][i][1]:
                    currCount += 1
                    self.__hotels[hotel][i] = (self.__hotels[hotel].rooms[i][0], currCount)
                else:
                    self.__hotels[hotel][i] = (self.__hotels[hotel].rooms[i][0], currCount)
                    currCount -= 1

    def getHotels(self, startTime, endTime):
        assert startTime < endTime
        result = []
        for hotel in self.__hotels:
            bookedRoomC = [0]
            for time, rCount in self.__hotels[hotel].rooms:
                if (time >= startTime and time <= endTime) or (time <= startTime) or (time >= endTime):
                    bookedRoomC.append(rCount)
            bookedRoomC = max(bookedRoomC)
            print self.__hotels[hotel].roomCount, bookedRoomC
            if self.__hotels[hotel].roomCount > bookedRoomC:
                result.append(hotel)
        return result

x = HotelsCalculater()
x.readHotels()
print x.getHotels()
