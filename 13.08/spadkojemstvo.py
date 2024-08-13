class Widget():
    def __init__(self, title, corx, cory):
        self.title = title
        self.corx = corx
        self.cory = cory
    def print_info(self):
        print("Напис:", self.title)
        print("Розташування:", self.corx, self.cory)

class Button(Widget):
    def __init__(self, title, corx, cory, is_clicked_bool):
        super().__init__(title, corx, cory)
        self.is_clicked = is_clicked_bool
    def clicked(self):
        self.is_clicked =True
        print("Ви зареєструвались")

button_1 = Button("Брати участь", 100, 100, False)
button_1.print_info()

questi = input("Хочете зареєструватися? (так / ні):")

if questi == "так":
    button_1.clicked()
else:
    print("А шкода!")