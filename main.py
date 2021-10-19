from kivy.clock import Clock
import datetime
import scrape
import threading
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class Main(App):
    def build(self):
        self.firstTime = True
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(self.layout)

        self.repeat()
        print("Root returned")
        return root


    def update_row(self):
        data = scrape.get_data()
        self.layout.clear_widgets()
        now = datetime.datetime.now().strftime("%H:%M:%S")
        last_updated = Label(text=f"Last Updated: {now}", font_size=17, padding_y=30)
        self.layout.add_widget(Label(text=""))
        self.layout.add_widget(last_updated)
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)[:20]
        for i in sorted_data:
            self.layout.add_widget(Label(text=f"{i[0]} : {i[1]}", size_hint_y=None, height=40))
        
    
    def start(self, dt):
        threading.Thread(target=self.update_row, daemon=True).start()
    
    def repeat(self):
        if self.firstTime:
            self.layout.add_widget(Label(text="Please Wait..."))
            self.start(None)
            self.firstTime = False
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)
        Clock.schedule_interval(self.start, 120)

        

   

if __name__ == "__main__":
    a = Main()
    a.run()
    a.start()
    