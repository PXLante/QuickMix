import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from json.decoder import JSONDecodeError


# Get the username from terminal
username = 'bigdog-90'
#client_id = '8f1b32cf9f294638855d631a18c7739d'
#client_secret = '2484e2860a0947fe94e8f8587ad25a2b'


scope = 'user-library-read playlist-modify-public'
token = util.prompt_for_user_token(username, scope)
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()




#print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
followers = user['followers']['total']

if token:
    
    results = spotifyObject.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)

while True:

    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print()
    choice = input("Your choice: ")
    print(choice)

    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        print()

        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        #print(json.dumps(searchResults, sort_keys=True, indent=4))
        

        # Artist details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']
        


        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        #extract album data
        albumResults = spotifyObject.artist_albums(artistID)

        pID = '4mTOrj2YF40z5j0TDps2DK'
        print()
        
        

        playlists = spotifyObject.playlist_tracks(pID, None, 100, 0, None)
        #print(json.dumps(playlists, sort_keys=True, indent=4))




        #track = playlists['items'][0]['track']
        
        
        #print((track['name']))
        
        #print(json.dumps(audioAnalysus, sort_keys=True, indent=4))
       
        songCatalog = []
        #print('trackDetail')
        for i in range(len(playlists)):
            track = playlists['items'][i]['track']
            trackInfo = {}
                 
            try :
    
                audioAnalysus = spotifyObject.audio_analysis(track['id'])
                key = audioAnalysus['track']['key']
                bpm = audioAnalysus['track']['tempo']
                trackInfo["id"] = track["id"]
                trackInfo["bpm"] = round(bpm)
                trackInfo["key"] = key
                songCatalog.append(trackInfo)   

                
                

            except :
                pass

            
            
            
        pprint(songCatalog)  
        print("=" * 50)
        jsonCatalog = sorted(songCatalog, key = lambda track: (track['bpm'], track['key']))
        print("=" * 50)
        pprint(jsonCatalog)
        print("=" * 50)
        #print(json.dumps(jsonCatalog, sort_keys=True, indent=4))      
        

        
        newPlaylist = spotifyObject.user_playlist_create(username, "DjQKMX", True, 'DJ QKMX currate playlist')
        #print(json.dumps(newPlaylist, sort_keys=True, indent=4))
        curratedPlaylistId = newPlaylist['id']
        #print(curratedPlaylistId)



        sortedTrackIDS = []
        
        for i in range(len(jsonCatalog)):
            sortedTrackIDS.append(jsonCatalog[i]['id'])
            
        


        

       
        addMix = spotifyObject.user_playlist_add_tracks(username, curratedPlaylistId, sortedTrackIDS  ) 
       
        


        
        

        
        
        





        



    if choice == "1":
        break