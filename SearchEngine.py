import webbrowser

try:
    print("What should i search?")
    content = input()
    new = 2
    tabUrl = "https://google.com/search?q="
    # term = raw_input(takeCommand())
    webbrowser.open(tabUrl + content, new=new)
except Exception as e:
    print(e)
    print("Sorry i didn't find that")
    # speak("Sorry i didn't find that")
