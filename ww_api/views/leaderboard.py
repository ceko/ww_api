from django.http import HttpResponse
import ww_api.endpoints
import urllib
from bs4 import BeautifulSoup

def weekly(request, player_id):
    #@todo: validate integer
    #endpoint = ww_api.endpoints.WEEKLY_LEADERBOARD_TEMPLATE % player_id
    #web_handle = urllib.urlopen(endpoint)
    #contents = web_handle.read()
    
    import os; 
    fp = os.path.join(os.path.dirname(__file__), os.pardir, 'testing/example_leaderboard_response.html')
    f = open(fp)
    contents = f.read()
    f.close()

    soup = BeautifulSoup(contents)
    
    score_column = soup.find("div", {"class": "column_score"})
    print(score_column)
    player_li = score_column.find("li", {"class": "logged-in"})
    
    print player_li
    
    return HttpResponse('test')