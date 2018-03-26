import urllib

def read_text():
    quotes = open(r'D:\Documents\1map\my-python-code\movie_quotes\movie_quotes.txt')
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_heck):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_heck)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print ("Profanity Alert!")
    elif "false" in output:
        print ("The document does not have curse words!")
    else:
        print ("Could not check the document properly.")

read_text()

