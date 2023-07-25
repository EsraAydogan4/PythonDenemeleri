html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wep Syfam</title>
</head>
<body>
    <h1 id="header">
        Python Kursu
    </h1>
    <div class="grup 1">
        <h2>
            Programlama
        </h2>   
        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>
    <div class="grup 2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>
    <img src="Bakugan.jpg" alt="">
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify() # html i düzenler sıra kaymaları kalkar
result = soup.title
result = soup.body # tek tek başlıkları alabiliriz
result = soup.title.string

result = soup.find_all("h2")
result = soup.find_all("h2")[0] # aynı isimde 2 tane h2 olduğu için sadece ilki gelir ama yenına sıra vererek isdeğimiz h2 yi getirebilriz

result = soup.find_all("div")[1].ul.find_all("li") #liler listelendi hepsi geldi
result = soup.div.findChildren()
result = soup.div.findNextSibling().findPreviousSibling() # buu methotlar ile ileri geri kardeşler arası gezinilebilir

print(result)
