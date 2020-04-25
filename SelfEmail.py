import yagmail
import datetime
import random
import csv

yag = yagmail.SMTP('!! ENTER THE EMAIL YOU WANT TO SEND IT FROM HERE !!')
test = False

# creates dated subject line
date = datetime.date.today()
today = date.strftime('%B') + ' ' + str(date.day) + ' ' + str(date.year)
subject = f"Daily Briefing - {today}"


# selects a quote to send
''' if testing on mac, opens the mac file location; else opens production location '''
# chooses random quote
if test:
    quoteCountFile = open(
        './QuotesCount.txt', 'r')
    quoteFile = open(
        './Quotes.csv', 'r')
else:
    quoteCountFile = open(
        './QuotesCount.txt', 'r')
    quoteFile = open(
        './Quotes.csv', 'r')
quoteReader = csv.reader(quoteFile, delimiter=' ')
quoteCount = int(quoteCountFile.read())
randNum = random.randint(0, quoteCount-1)

c = 0
contents = ''
for row in quoteReader:
    if c == randNum:
        contents = row[0]
        break
    c += 1

if test:
    print(subject)
    print('\n')
    print(contents)
else:
    yag.send('!! ENTER THE EMAIL YOU WANT TO SEND IT TO HERE !!', subject, contents)
