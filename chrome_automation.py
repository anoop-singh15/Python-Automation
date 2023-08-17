import webbrowser

web=input("Enter web path\n")
url=f"{web}"
url2="youtube.com"


chrome_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)