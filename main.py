from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import webbrowser
import pyttsx3
import requests
import json
import wikipedia

engine = pyttsx3.init()

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.entry = TextInput(hint_text='Enter Your Command', multiline=False)
        layout.add_widget(self.entry)

        buttons = [
            ('Search on YouTube', self.search_youtube),
            ('Search on Google', self.search_google),
            ('Search on Instagram', self.search_instagram),
            ('Get Weather', self.get_weather),
            ('Get News', self.get_news),
            ('Search on Wikipedia', self.search_wikipedia),
        ]

        for btn_text, btn_callback in buttons:
            btn = Button(text=btn_text, on_press=btn_callback)
            layout.add_widget(btn)

        return layout

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    def search_youtube(self, instance):
        query = self.entry.text
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        self.speak(f"Searching YouTube for {query}")

    def search_google(self, instance):
        query = self.entry.text
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        self.speak(f"Searching Google for {query}")

    def search_instagram(self, instance):
        username = self.entry.text.replace('@', "")
        url = f"https://www.instagram.com/{username}/"
        webbrowser.open(url)
        self.speak(f"Searching Instagram for {username}")

    def get_weather(self, instance):
        try:
            weatherstack_api_key = "cad1ea6fe1649610f9184078beed8dc7"
            city = self.entry.text
            url = f"http://api.weatherstack.com/current?access_key={weatherstack_api_key}&query={city}"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200 and 'current' in data:
                temperature_celsius = data['current']['temperature']
                description = data['current']['weather_descriptions'][0]

                self.speak(f"The weather in {city} is {description} with a temperature of {temperature_celsius} Celsius.")
                webbrowser.open("https://weatherstack.com/")
            else:
                self.speak(f"Failed to fetch weather information. Status Code: {response.status_code}")
        except Exception as e:
            Popup(title='Error', content=Label(text=f"Failed to fetch weather information: {str(e)}"), size=(400, 200)).open()

    def get_news(self, instance):
        try:
            news_api_key = "e07dbcac8929485aa5676f5bde36cf73"
            news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
            response = requests.get(news_url)
            news_data = response.json()

            articles = news_data.get('articles', [])
            if articles:
                self.speak("Here are the top headlines:")
                for article in articles:
                    self.speak(article['title'])
                    webbrowser.open(article['url'])
            else:
                self.speak("No news articles found.")
        except Exception as e:
            Popup(title='Error', content=Label(text=f"Failed to fetch news information: {str(e)}"), size=(400, 200)).open()

    def search_wikipedia(self, instance):
        query = self.entry.text
        try:
            result = wikipedia.summary(query, sentences=2)
            self.speak(f"According to Wikipedia, {result}")
            webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
        except wikipedia.DisambiguationError as e:
            self.speak(f"There are multiple matches for {query}. Please be more specific.")
        except wikipedia.PageError as e:
            self.speak(f"Sorry, I couldn't find any information about {query} on Wikipedia.")

if __name__ == '__main__':
    MyApp().run()
