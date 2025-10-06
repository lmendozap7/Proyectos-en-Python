import datetime

meses = {"JANUARY": 1, "FEBRUARY": 2, "MARCH": 3, "APRIL": 4, "MAY": 5, "JUNE": 6, "JULY": 7, "AUGUST": 8,
         "SEPTEMBER": 9, "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12}
dias = {1: "MONDAY", 2: "TUESDAY", 3: "WEDNESDAY", 4: "THURSDAY", 5: "FRIDAY", 6: "SATURDAY", 7: "SUNDAY"}

num = input()
while num > 0:
    cad = raw_input().split(" ")
    Date = datetime.datetime(int(cad[0]), meses[cad[1]], int(cad[2]))
    print dias[Date.isoweekday()]
    num -= 1
