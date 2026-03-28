import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleSpellCheck(self, e):
        txtCurrentSentence = self._view.txtInput.value
        if txtCurrentSentence == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Add a sentence!"))
            return

        language = self._view.ddLanguage.value
        print(language)
        modality = self._view.ddSelectModality.value
        print(modality)

        if language == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select language!"))
            return
        if modality == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select modality!"))
            return

        parole, elapsedTime = self.handleSentence(txtCurrentSentence,language, modality)

        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text("Frase inserita: " + txtCurrentSentence))
        self._view.txtOut.controls.append(ft.Text("Parole errate: " + parole))
        self._view.txtOut.controls.append(ft.Text(value = "Tempo richiesto dalla ricerca: " + str(elapsedTime)))

        self._view.update()

    def handleSelectSearchMode(self, e):
        print("handle dropdown modality called")
        self._view.txtOut.controls.append(ft.Text(value="Search mode correctly selected: " + self._view.ddSelectModality.value))
        self._view.update()

    def handleLanguageSelection(self, e):
        print("handle Dropdown language called")
        self._view.txtOut.controls.append(ft.Text(value="Language correctly selected: " + self._view.ddLanguage.value))
        self._view.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text