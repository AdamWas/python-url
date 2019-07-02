from tkinter import *
from tkinter import scrolledtext as tkscrolled

import urlparser

#window display config.
window = Tk()
window.title("URL keywords finder")
window.geometry('680x400')

#label config.
label = Label(window, text="Paste URL (with 'http/https://')")
label.grid(column=0, row=0)

#elements padding settings
_padx=10
_pady=10

#url input config.
urlInput = Entry(window, width=80)
urlInput.grid(column=0, row=1, padx=_padx, pady=_pady)
urlInput.focus()

#button method
def clicked():
    result.config(state=NORMAL)
    result.delete(1.0,END)
    parsedHtml = urlparser.parse(urlInput.get())
    if 'keywords' not in parsedHtml:
        for key, value in parsedHtml.items():
            result.insert('insert', key + ' -> ' + value)
            result.insert('end', '\n')
    else:
        counted = urlparser.countWords(parsedHtml['keywords'],
                                    parsedHtml['fulltext'])
        for keyword, number in counted.items():
            result.insert('insert', keyword + ' -> ' + number)
            result.insert('end', '\n')
    result.config(state=DISABLED)

#button config.
btn = Button(window, text="Find website keywords", command=clicked)
btn.grid(column=0, row=2, padx=_padx, pady=_pady)

#result display config.
result = tkscrolled.ScrolledText(window, height=10, width=80)
result.grid(column=0, row=4, padx=_padx, pady=_pady)

window.mainloop()
