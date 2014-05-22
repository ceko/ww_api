from django.conf.urls import patterns, url


urlpatterns = patterns('ww_api.views',
    url(r'^leaderboard/weekly/(?P<player_id>\d+?)/$', 'leaderboard.weekly', name='ww_api:leaderboard-weekly'),        
)