from django.shortcuts import render
import pyrebase
config = {
    'apiKey': "AIzaSyDL1k3KzsLLzK7q_8bTYYQAa9rTT1ivueo",
   ' authDomain': "service-market-c87dc.firebaseapp.com",
    'databaseURL': "https://service-market-c87dc.firebaseio.com",
    'projectId': "service-market-c87dc",
    'storageBucket': "service-market-c87dc.appspot.com",
    'messagingSenderId': "1057903508445",
    'appId': "1:1057903508445:web:35a0b389dfa0c5f4"
  }

  firebase = pyrebase.initialize.app(config)