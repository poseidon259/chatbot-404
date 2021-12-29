
import webbrowser


def open_google_and_search(search_for):
    url = "https://www.google.com.vn/search?q=" + search_for
    return webbrowser.open(url)

#open_google_and_search('Python')

    