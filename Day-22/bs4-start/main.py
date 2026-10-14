from bs4 import BeautifulSoup
import lxml
with open ("website.html", "r") as f:
    content = f.read()

soup = BeautifulSoup(content, "lxml")