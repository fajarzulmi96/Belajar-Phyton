#Belajar keyword
#**atttributes untuk mendeskripsikan keyword argumen list
#masukan nama argumennya tapi harus disebutkan nama parameter lau di combine menjadi sebuah dictionary
#Create tag html sangat dinamis
def create_html (tag, text, **attributes) :
    html = f"<{tag}"
    for key, value in attributes.items():
        html = html + f"{key} = '{value}'"
    html = html + f">{text}</{tag}"
    print(attributes)
    return html

html = create_html("p", "Hello Python", style = "Paragraf")
print(html)
html = create_html("a", "Hello Python", href = "www.google.com", style="Link")
print(html)
