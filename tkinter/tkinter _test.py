"""
    https://pythonbuch.com/gui.html


"""


from tkinter import *


# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def button_action():
    anweisungs_label.config(text="Ich wurde geändert!")



# Ein Fenster erstellen
fenster = Tk()

# Den Fenstertitle erstellen
fenster.title("Nur ein Fenster")
fenster.geometry("500x200")  # Größe Hauptformular
fenster.config(bg="#4682B4")  # Farbe Hauptformular

# Label und Buttons erstellen.
change_button = Button(fenster, text="Ändern", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)
anweisungs_label = Label(fenster, text="Ich bin eine Anweisung:\nKlicke auf 'Ändern'.")
info_label = Label(fenster, text="Ich bin eine Info:\nDer Beenden Button schliesst das Programm.")

# Nun fügen wir die Komponenten unserem Fenster
# in der gwünschten Reihenfolge hinzu.
anweisungs_label.grid(row=0, column=0, pady = 20)
change_button.grid(row=0, column=1, pady = 20)
info_label.grid(row=1, column=0, pady = 20)
exit_button.grid(row=1, column=1, pady = 20)

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()

