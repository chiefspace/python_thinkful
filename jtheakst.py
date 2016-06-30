phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

for key,val in phone_book.items():
    print("{} = {}".format(key, val))

lookUp = "Jamie Theakston"
try:
        phone_book[lookUp]
except KeyError:
        print "Aparently, {} has an unlisted phone number".format(lookUp)