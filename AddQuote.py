import csv

i = [input("Enter a quote")]
# TODO parse through the input to make sure that it is in the format of "'QUOTE' - Author"

# reads the quote file
''' fedora-server file location '''
#quotes = open('/home/alishan/Nextcloud/Projects/SelfEmail/Quotes.csv', 'a', newline='')
''' mac file location '''
quotes = open(
    '/Users/alishan/Nextcloud/Projects/SelfEmail/Quotes.csv', 'a', newline='')
quoteWriter = csv.writer(quotes)
quoteWriter.writerow(i)


# increment quotes count by 1
# read quote count file
quoteCountRead = open(
    '/Users/alishan/Nextcloud/Projects/SelfEmail/QuotesCount.txt', 'r')
count = str(int(quoteCountRead.read()) + 1)

# writes new count value
quoteCountWrite = open(
    '/Users/alishan/Nextcloud/Projects/SelfEmail/QuotesCount.txt', 'w')
quoteCountWrite.write(count)
