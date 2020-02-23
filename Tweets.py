import tkinter as tk
import tweepy

class CButton:
    def __init__(self,value,button):
        self.value = value
        self.button = button
        
def getTweetsFromKeyword(keyword):
    search_results = api.search(q=keyword, count=100, geocode="46.27155,2.627197,350km",lang="fr")
    with open("result.txt", "a", encoding="utf-8") as f:
        for i in search_results:
            print(i.text)
            print('\n')
            f.write(i.text)
            f.write('\n------------------------------------------------------------\n')
    f.close()

def searchTweets(checkButtons):
     for cb in checkButtons:
         if cb.value.get():
             search = cb.button.cget("text")
             print(search)
             getTweetsFromKeyword(search)

def getTrends(WOEID):
	trendsP = api.trends_place(WOEID) #Renvoi les tendances sous forme de JSON
	data = trendsP[0] #Récupère le contenu du JSON
	trends = data['trends'] #Récupère les éléments 'trends' du JSON
	names = [trend['name'] for trend in trends] #Récupère l'élément 'name' de chaque tendance
	return names
    
CONSUMER_KEY = 'tRdGwCfgXhXji5B61iJG3YabW'
CONSUMER_SECRET = 'YM6abr5ro8UYozbhg7PrDxari3zZVEnfHGipdlGo8F923JsY1c'
ACCESS_KEY = '874999178056933376-hun4QxdS5DR7oypJUR610IojjgcyL6S'
ACCESS_SECRET = '69vlQ3LfENLkkymsNEgjYzKeNqxraHMdJYUBnT34RVWLw'

PARIS_WOEID = 615702

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

top = tk.Tk()
 
names = getTrends(PARIS_WOEID)

i = 0
j = 0
checkbuttons = []
for name in names:
    checkVar = tk.IntVar()
    checkbox = tk.Checkbutton(top, text = name, variable = checkVar, onvalue = 1, offvalue = 0)
    checkbuttons.append(CButton(checkVar,checkbox))
    checkbox.grid(row=i,column=j)
    i = i +1
    if i == 10:
        i = 0
        j = j + 1
    
searchButton = tk.Button(top, text ="Search tweets", command = lambda: searchTweets(checkbuttons))
searchButton.grid(row = 11,column = 1)



top.mainloop()