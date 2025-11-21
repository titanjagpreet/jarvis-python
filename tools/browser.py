import webbrowser

def open_website(url):
    webbrowser.open(url)

def search_google(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)

def search_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    webbrowser.open(url)
