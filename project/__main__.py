import tkinter as tk
from PIL import Image, ImageTk
from project.services.location import get_similar_location
from project.services.weather import ForecastFetcher


class Weatherh8su:
    def __init__(self, master):
        self.master = master
        master.title("Weather h8su")
        # Variables
        self.main_canvas = None
        self.top_frame = None
        self.glass = None
        self.search_bar = None
        self.search_icon = None
        self.f = None
        self.gear = None
        self.settings = None
        self.todays_content = None
        self.todays_frame = None
        self.todays_label = None
        self.tomorrows_frame = None
        self.tomorrows_label = None
        self.tomorrows_content = None

        self.create_widgets()

    def create_widgets(self):
        self.background_image = None
        self.main_canvas = tk.Canvas(self.master)
        self.main_canvas.create_image(0, 0, image=self.background_image)
        self.main_canvas.pack()
        self.top_frame = tk.Frame(self.main_canvas)
        self.top_frame.pack()
        self.glass = Image.open("data/glass.png")
        self.glass = ImageTk.PhotoImage(self.glass)
        self.search_icon = tk.Label(self.top_frame, image=self.glass)
        self.search_icon.grid(row=0, column=0)
        self.search_bar = tk.Entry(self.top_frame, width=70)
        self.search_bar.bind("<Return>", lambda e: self.search_function())
        self.search_bar.grid(row=0, column=1)
        self.f = tk.Frame(self.top_frame, width=26, height=30)
        self.f.grid(column=2, row=1)
        self.gear = Image.open("data/gear.png")
        self.gear = ImageTk.PhotoImage(self.gear)
        self.settings = tk.Label(self.top_frame, image=self.gear)
        self.settings.bind("<Enter>", lambda e: self.annoy())
        self.settings.bind("<Leave>", lambda e: self.de_annoy())
        self.f.bind("<Leave>", lambda e: self.de_annoy())
        self.settings.grid(column=2, row=0)
        self.todays_frame = tk.Frame(self.main_canvas)
        self.todays_label_frame = tk.Frame(self.todays_frame)
        self.todays_label_frame.pack(side=tk.LEFT)
        self.todays_content_frame = tk.Frame(self.todays_frame)
        self.todays_content_frame.pack(side=tk.LEFT)
        self.todays_frame.pack(side=tk.LEFT)
        self.todays_label = tk.Label(self.todays_label_frame, text="TODAY:",
                                     font=(None, 30), height=2, anchor="s")
        self.todays_label.pack()
        self.todays_content = tk.Label(
            self.todays_content_frame, text="content\nhere", font=(None, 15))
        self.todays_content.pack(side=tk.LEFT)
        self.tomorrows_frame = tk.Frame(self.main_canvas)
        self.tomorrows_frame.pack()
        self.tomorrows_label = tk.Label(
            self.tomorrows_frame, text="TOMORROW:", font=(None, 30))
        self.tomorrows_label.pack()
        self.tomorrows_content = tk.Label(
            self.tomorrows_frame, text="content\nhere", font=(None, 15))
        self.tomorrows_content.pack(side=tk.LEFT)

    def annoy(self):
        self.settings.grid(row=1)
        self.f.grid(row=0)

    def de_annoy(self):
        if self.mouse_on(self.settings) or self.mouse_on(self.f):
            return
        self.settings.grid(row=0)
        self.f.grid(row=1)

    def mouse_on(self, widget):
        if self.master.winfo_containing(
                *self.master.winfo_pointerxy()) == widget:
            return True
        return False

    def search_function(self):
        """
        Called with someone presses the
        `enter`-button.
        """

        search_string = self.search_bar.get()
        location = get_similar_location(search_string)
        weather = ForecastFetcher("OWM_API_KEY")
        weather = weather.fetch_forecast_7_days(location, "random")

        # We put todays weather tomorrow, and tomorrows weather today
        today = weather[1]
        tomorrow = weather[0]
        todays_weather = today['weather_status']

        self.todays_content.config(
            text=f"Day temperature: {today['day temperature']}\n"
            f" Evening temperature: {today['evening temperature']}\n"
            f" High: {today['highest temperature']}, "
            f"Low: {today['lowest temperature']}"
        )
        self.tomorrows_content.config(
            text=f"Day temperature: {tomorrow['day temperature']}\n"
            f" Evening temperature: {tomorrow['evening temperature']}\n"
            f" High: {tomorrow['highest temperature']}, "
            f"Low: {tomorrow['lowest temperature']}"
        )

        # Also change the background:
        todays_weather(todays_weather)

    def change_background(self, which_image: str):
        """
        Changes background according to the weather
        """
        # if which_image.lower() is "clear", snow, and so on..
        # change background image to x
        # else: take random image


root = tk.Tk()
app = Weatherh8su(root)
root.mainloop()
