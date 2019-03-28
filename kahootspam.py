import time
import random
import os
import urllib
import urllib2
import webbrowser

def spam(amount, pin):
    data = urllib.urlencode({'q': pin})
    kahoot = "https://kahoot.it"
    url = urllib.request()
