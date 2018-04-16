# https://docs.python.org/2.7/
import os
import sys
import urllib
import urlparse
# http://mirrors.kodi.tv/docs/python-docs/
import xbmcaddon
import xbmcgui
import xbmcplugin

def build_url(query):
    base_url = sys.argv[0]
    return base_url + '?' + urllib.urlencode(query)
    
def build_song_list():
    '''
http://ice10.securenetsystems.net/media/20TCM/ondemand/currentcountdown.m4a
http://ice10.securenetsystems.net/media/20TCM/ondemand/Top20ChrisTomlinSongs.m4a
http://ice10.securenetsystems.net/media/20TCM/ondemand/RichMullins20YearsLater.m4a
    '''
    song_list = []
    #20TCM
    li = xbmcgui.ListItem(label='20 The Countdown Magazine',thumbnailImage='http://cdnrf.securenetsystems.net/file_radio/stations_large/20TCM/v5/logo.png')
    li.setProperty('IsPlayable', 'true')
    li.setProperty('fanart_image', 'http://cdnrf.securenetsystems.net/file_radio/stations_large/20TCM/v5/logo.png')
    url = build_url({'mode': 'stream', 'url': 'http://ice10.securenetsystems.net/media/20TCM/ondemand/currentcountdown.m4a', 'title': '20 The Countdown Magazine'})
    song_list.append((url, li, False))


    #Top20ChrisTomlinSongs
    li = xbmcgui.ListItem(label='Top 20 Chris Tomlin Worship Songs',thumbnailImage='http://cdnrf.securenetsystems.net/file_radio/stations_large/20TCM/v5/logo.png')
    li.setProperty('IsPlayable', 'true')
    li.setProperty('fanart_image', 'http://cdnrf.securenetsystems.net/file_radio/stations_large/20TCM/v5/logo.png')
    url = build_url({'mode': 'stream', 'url': 'http://ice10.securenetsystems.net/media/20TCM/ondemand/Top20ChrisTomlinSongs.m4a', 'title': 'Top 20 Chris Tomlin Worship Songs'})
    song_list.append((url, li, False))
    
    #RichMullins20YearsLater
    li = xbmcgui.ListItem(label='Rich Mullins Tribute 20 Years Later',thumbnailImage='http://cdnrf.securenetsystems.net/file_radio/stations_large/20TCM/v5/logo.png')
    li.setProperty('IsPlayable', 'true')
    li.setProperty('fanart_image', 'http://cdnrf.securenetsystems.net/file_radio/stations_large/20TCM/v5/logo.png')
    url = build_url({'mode': 'stream', 'url': 'http://ice10.securenetsystems.net/media/20TCM/ondemand/RichMullins20YearsLater.m4a', 'title': 'Rich Mullins Tribute 20 Years Later'})
    song_list.append((url, li, False))

    # add list to Kodi per Martijn
    # http://forum.kodi.tv/showthread.php?tid=209948&pid=2094170#pid2094170
    xbmcplugin.addDirectoryItems(addon_handle, song_list, len(song_list))
    # set the content of the directory
    xbmcplugin.setContent(addon_handle, 'songs')
    xbmcplugin.endOfDirectory(addon_handle)
    
def play_song(url):
    # set the path of the song to a list item
    play_item = xbmcgui.ListItem(path=url)
    # the list item is ready to be played by Kodi
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)
    
def main():
    args = urlparse.parse_qs(sys.argv[2][1:])
    mode = args.get('mode', None)
    
    # initial launch of add-on
    if mode is None:

        # display the list of songs in Kodi
        build_song_list()
    # a song from the list has been selected
    elif mode[0] == 'stream':
        # pass the url of the song to play_song
        play_song(args['url'][0])
    
if __name__ == '__main__':
    addon_handle = int(sys.argv[1])
    main()
