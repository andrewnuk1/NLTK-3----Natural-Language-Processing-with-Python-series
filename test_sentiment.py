import sentiment_mod as s
import xlrd
import xlwt

with open("justeat2017070120170930nodates.txt") as f:
    tweets = [x.strip('\n') for x in f.readlines()]

result = []

for i in range(len(tweets)):
    result.append(s.sentiment(tweets[i]))
    if i/1000 == int(i/1000):
        print(str(i) + str(" of ") + str(len(tweets)))

print(len(tweets))
print("starting workbook")

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('sentiment')



for ii in range(len(result)):
    sheet.write(ii - 50000*(int(ii/50000)),5*(int(ii/50000))+0,tweets[ii])
    sheet.write(ii - 50000*(int(ii/50000)),5*(int(ii/50000))+1,result[ii][0])
    sheet.write(ii - 50000*(int(ii/50000)),5*(int(ii/50000))+2,result[ii][1])
    if ii/1000 == int(ii/1000):
        print("workbook " + str(ii))

print(len(result))

workbook.save('outputresultjusteat2017070120170930try2.xls')
