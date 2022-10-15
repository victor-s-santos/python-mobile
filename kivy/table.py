from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class TableApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        screen = MDScreen()
        table = MDDataTable(
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            size_hint = (0.6, 0.5),
            column_data = [
                ("First Name", dp(25)),
                ("Last Name", dp(25)),
                ("Phone Number", dp(25)),
            ],
            row_data = [
                ("Noob", "Saibot", "14999003361"),
                ("Dunga", "Rafael", "14997012566"),
                ("Katarina", "Katrina", "14999003361"),
                ("Megg", "Ti", "14999003361"),
                ("Flanela", "Flanzinho", "14999003361"),
                ("Mia", "Miaú", "14999003361"),
            ]
        )
        screen.add_widget(table)
        return screen

if __name__ == "__main__":
    TableApp().run()