import justpy as jp

def page():
    page = jp.QuasarPage()
    heading = jp.QDiv(a = page, text = "Analysis of Book Prices", classes = "text-h1 text-center q-pa-md ")
    p = jp.QDiv(a = page, text = "Graphs represent the prices of books", classes = "text-h6 text-center q-pa-md")
    

    return page

jp.justpy(page)