from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import json

#note_text, note_list, tag_list
#note_create, note_delete, note_save
#tag_list_add, tag_list_unpin, tag_list_search
#line_edit_tag

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.notes = {
            "G'day sir!": {
                "taxt" : "Shitteen",
                "tags" : ["wan", "tu"]
            }
        }
        self.ui.note_list.itemClicked.connect(self.show_note)
        self.ui.note_create.clicked.connect(self.add_note)
        self.ui.note_delete.clicked.connect(self.del_note)
        self.ui.note_save.clicked.connect(self.save_note)

        self.ui.tag_list_add.clicked.connect(self.add_tag)
        self.ui.tag_list_unpin.clicked.connect(self.del_tag)
        self.ui.tag_list_search.clicked.connect(self.search_tag)
        

    def show_note(self):
        key = self.ui.note_list.selectedItems()[0].text()
        self.ui.note_text.setText(self.notes[key]["taxt"])
        self.ui.tag_list.clear()
        self.ui.tag_list.addItems(self.notes[key]["tags"])

    def load_notes(self):
        try:
            with open("notes_data.json", "r") as file:
                self.notes = json.load(file)
            self.ui.note_list.addItems(self.notes)
        except:
            with open("notes_data.json", "w") as file:
                json.dump(self.notes, file)

    def add_note(self):
        self.note_name, ok = QInputDialog.getText(self, "Add", "Name:")
        if ok and self.note_name != "":
            self.notes[self.note_name] = {"taxt" : "", "tags" : []}
            self.ui.note_list.addItem(self.note_name)
            self.ui.tag_list.addItems(self.notes[self.note_name]["tags"])
            print(self.notes)

    def del_note(self):
        if self.ui.note_list.selectedItems():
            key = self.ui.note_list.selectedItems()[0].text()
            del self.notes[key]
            self.ui.note_list.clear()
            self.ui.tag_list_label.clear()
            self.ui.note_text.clear()
            self.ui.note_list.addItems(self.notes)
            with open("notes_data.json", "w", encoding= "utf-8")as file:
                json.dump(self.notes, file, sort_keys = True, ensure_ascii = False)
            print(self.notes)
        else:
            print('Замітка не обрана!!!')

    def save_note(self):
        if self.ui.note_list.selectedItems():
            self.key = self.ui.note_list.selectedItems()[0].text()
            self.notes[self.key]["taxt"] = self.ui.note_text.toPlainText()
            with open("notes_data.json", "w",encoding= "utf-8")as file:
                json.dump(self.notes, file, sort_keys = True, ensure_ascii = False)
            print(self.notes)
        else:
            print('Замітка не обрана!!!')

    def add_tag(self):
        if self.ui.note_list.selectedItems():
            key = self.ui.note_list.selectedItems()[0].text()
            tag = self.ui.line_edit_tag.text()
            if not tag in self.notes[key]["tags"]:
                self.notes[key]["tags"].append(tag)
                self.ui.tag_list.addItem(tag)
                self.ui.line_edit_tag.clear()
            with open("notes_data.json", "w", encoding = "UTF-8") as file:
                json.dump(self.notes, file, sort_keys= True, ensure_ascii=False)
            print(self.notes)
        else:
            print("no")

    def del_tag(self):
        if self.ui.tag_list.selectedItems():
            if self.ui.note_list.selectedItems():
                key = self.ui.note_list.selectedItems()[0].text()
                tag = self.ui.tag_list.selectedItems()[0].text()
                self.notes[key]["tags"].remove(tag)
                self.ui.tag_list.clear()
                self.ui.tag_list.addItems(self.notes[key]["tags"])
                with open("notes_data.json", "w", encoding='utf-8') as file:
                    json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
            else:
                print("no")
        else:
            print("no")

    def search_tag(self):
        print(self.ui.tag_list_search.text())
        tag = self.ui.line_edit_tag.text()
        if self.ui.tag_list_search.text() == "Шукати нотатки по тегу" and tag:
            print(tag)
            notes_filtered = {}
            for note in self.notes:
                if tag in self.notes[note]["tags"]:
                    notes_filtered[note] = self.notes[note]
            self.ui.tag_list_search.setText("Скинути пошук")
            self.ui.note_list.clear()
            self.ui.tag_list.clear()
            self.ui.note_list.addItems(notes_filtered)
            print(self.ui.tag_list_search.text())
        elif self.ui.tag_list_search.text() == "Скинути пошук":
            self.ui.line_edit_tag.clear()
            self.ui.note_list.clear()
            self.ui.tag_list.clear()
            self.ui.note_list.addItems(self.notes)
            self.ui.tag_list_search.setText("Шукати замітку")
            print(self.ui.tag_list_search.text())
        else:
            pass


if __name__ == "__main__":
    app = QApplication([])
    ex = Widget()
    ex.show()
    app.exec_()