from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import json

#note_text, note_list, tag_list
#note_create, note_delete, note_save
#tag_list_add, tag_list_unpin, tag_list_search
#line_tag_edit

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.notes = {
            "G'day sir!": {
                "taxt" : "Shitteen",
                "tegs" : ["wan", "tu"]
            }
        }
        self.ui.note_list.itemClicked.connect(self.show_note)
        self.load_notes() # reads text
        self.ui.note_create.itemClicked.connect(self.add_note)
        self.ui.note_delete.itemClicked.connect(self.del_note)
        self.ui.note_save.itemClicked.connect(self.save_note)

        self.ui.tag_list_add.itemClicked.connect(self.add_tag)
        self.ui.tag_list_unpin.itemClicked.connect(self.del_tag)
        self.ui.tag_list_search.itemClicked.connect(self.search_tag)
        

        def show_note(self):
            key = self.ui.note_list.selectItems()[0].text()
            self.ui.note_text.setText(self.notes[key]["taxt"])
            self.ui.tag_list.clear()
            self.ui.tag_list.addItems(self.notes[key]["tegs"])

        def load_notes(self):
            try:
                with open("notes_data.json", "r") as file:
                    self.notes = json.load(file)
                self.ui.note_list.addItems(self.notes)
            except:
                with open("notes_data.json", "w") as file:
                    json.dump(self.notes, file)

        def add_note(self):
            self.note_name, ok = QInputDialog.getText(self.notes_win, "Add", "Name:")
            if ok and self.note_name != "":
                self.notes[self.note_name] = {"taxt" : "", "tegs" : []}
                self.ui.note_list.addItem(self.note_name)
                self.ui.tag_list.addItems(self.notes[self.note_name]["tegs"])
                print(self.notes)

        def save_note(self):
            if self.ui.note_list.selectedItems():
                self.key = self.ui.note_list.selectedItems()[0].text()
                self.notes[self.key]["taxt"] = self.ui.note_text.toPlainText()
                with open("notes_data.json", "w")as file:
                    json.dump(self.notes, self.file, sort_keys = True, ensure_ascii = False)
                print(self.notes)
            else:
                print('no')

        def add_tag(self):
            if self.ui.note_list.selectedItems():
                key = self.ui.note_list.selectedItems()[0].text()
                tag = self.ui.line_tag_edit.text()
                if not tag in self.notes[key]["teg"]:
                    self.notes[key]["teg"].append(tag)
                    self.ui.tag_list.addItem(tag)
                    self.ui.line_tag_edit.clear()
                with open("notes_data.json", "w", encoding = "UTF-8") as file:
                    json.dump(self.notes, file, sort_keys= True, ensure_ascii=False)
                print(self.notes)
            else:
                print("no")

        def del_tag(self):
            if self.ui.tag_list.selectedItems():
                if self.ui.note_list.selectedItems():
                    key = self.ui.note_list.selectedItems()[0].text()
                    teg = self.ui.tag_list.selectedItems()[0].text()
                    self.notes[key]["tegs"].remove(teg)
                    self.ui.tag_list.clear()
                    self.ui.tag_list.addItems(self.notes[key]["tegs"])
                    with open("notes_data.json", "w", encoding='utf-8') as file:
                        json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
                else:
                    print("no")
            else:
                print("no")

        def search_tag(self):
            print(self.ui.tag_list_search.text())
            teg = self.ui.line_tag_edit.text()
            if self.ui.tag_list_search.text() == "Шукати нотатки по тегу" and teg:
                print(teg)
                notes_filtered = {}
                for note in self.notes:
                    if teg in self.notes[note]["tegs"]:
                        notes_filtered[note] = self.notes[note]
                self.ui.tag_list_search.setText("Скинути пошук")
                self.ui.note_list.clear()
                self.ui.tag_list.clear()
                self.ui.note_list.addItems(notes_filtered)
                print(self.ui.tag_list_search.text())
            elif self.ui.tag_list_search.text() == "Скинути пошук":
                self.ui.line_tag_edit.clear()
                self.ui.note_list.clear()
                self.ui.tag_list.clear()
                self.ui.note_list.addItems(self.notes) #допиши


if __name__ == "__main__":
    app = QWidget.QApplication([])
    ex = Widget()
    ex.show()
    app.exec_()