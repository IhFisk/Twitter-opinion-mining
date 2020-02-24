import tkinter as tk
import tweepy

class CButton:
    def __init__(self,value,button):
        self.value = value
        self.button = button
        
"récupère les 100 derniers tweets contenant un mot-clé passé en paramètre et les écris dans un fichier texte"
def getTweetsFromKeyword(keyword):
    keyword = keyword + " -filter:retweets"
    with open("result.txt", "a", encoding="utf-8") as f:
        search_results = api.search(q=keyword, count=100, geocode="46.27155,2.627197,350km",result_type="recent", lang="fr", tweet_mode ="extended")
        maxid = 0
        c = 0
        for x in range(1,100):
            for i in search_results:
                if(maxid != i.id):
                    c+=1
                    print(c)
                    print(i.id)
                    print(i.full_text)
                    print('\n')
                    f.write(i.id_str + " ")
                    f.write(i.full_text)
                    f.write('\n------------------------------------------------------------\n')
                    maxid = i.id
                else:
                    print(i.id)
                    f.close()
                    return
            search_results  = api.search(q=keyword, count=100, result_type="recent", tweet_mode ="extended", max_id = maxid-1)
    f.close()
    
def searchTweets(checkButtons):
     for cb in checkButtons:
         if cb.value.get():
             search = cb.button.cget("text")
             print(search)
             getTweetsFromKeyword(search)

"récupère les tendances proche d'un endroit passé en paramètre"
def getTrends(WOEID):
	trendsP = api.trends_place(WOEID) #Renvoi les tendances sous forme de JSON
	data = trendsP[0] #Récupère le contenu du JSON
	trends = data['trends'] #Récupère les éléments 'trends' du JSON
	names = [trend['name'] for trend in trends] #Récupère l'élément 'name' de chaque tendance
	return names
    
CONSUMER_KEY = 'v2pSMP8Qq6jpLhk731RdMGSvA'
CONSUMER_SECRET = 'VLkKvIU2rSh6P5c8suoU8UGLS4NwtEiwOEhqq5W7pbKfe3Bz7P'
ACCESS_KEY = '1571137290-g61gc41oZtpETZIg2Q4KVP6XVYSNvMzSk57mKm1'
ACCESS_SECRET = 'iQKVmVk6Vg8SdaXkDhkuAYGHBUB3jpcyXMCXLy9n3rCXa'

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
