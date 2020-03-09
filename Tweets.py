import tkinter as tk
import tweepy
from afinn import Afinn

class CButton:
    def __init__(self,value,button):
        self.value = value
        self.button = button
        
def getTweetsFromKeyword(keyword):
    k = keyword + " -filter:retweets"
    afinn = Afinn(language='fr')
    with open("result.txt", "a", encoding="utf-8") as f:
        search_results = api.search(q=k, count=100, geocode="46.27155,2.627197,350km",result_type="recent", lang="fr", tweet_mode ="extended")
        maxid = 0
        c = 0
        for x in range(1,100):
            print(x)
            print("x")
            for i in search_results:
                if(maxid != i.id):
                    c+=1
                    print(c)
                    print(i.retweet_count)
                    print(i.favorite_count)
                    print(i.id)
                    print(i.full_text)
                    print(afinn.score(i.full_text))
                    print('\n')
                    f.write(i.id_str + " ")
                    f.write(i.full_text)
                    f.write('\n------------------------------------------------------------\n')
                    maxid = i.id
                else:
                    print(i.id)
                    f.close()
                    return
                search_results  = api.search(q=k, count=100, geocode="46.27155,2.627197,350km",result_type="recent", lang="fr", tweet_mode ="extended", max_id = maxid-1)
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
    
CONSUMER_KEY = 'aQwJP4kxuRRrbOblx4DuXrFGk'
CONSUMER_SECRET = 'mQilj1fiZ4cDqehXDegrGK8URfvxZgTplH7z4ZJHsYMXYjs50N'
ACCESS_KEY = '874999178056933376-4OyTKX8gneHJ93yUr6j8XPcUjzAmhZ8'
ACCESS_SECRET = 'GtOFxjeG4vxGKtR3dk6zDX6bR701jgU9DiTQAET2FhoTi'

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