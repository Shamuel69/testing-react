from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Search:
    def __init__(self, prompt=str, titles=True, **kwargs):
        self.prompt = prompt
        self.data = titles
        self.results = self.search_results()
    
    def search_results(self) -> list:
        bing = []
        for url in search(self.prompt, num_results=20):
            try:
                if self.data is True:
                    soup = BeautifulSoup(urlopen(url), features="html.parser")
                    combo = (soup.title.get_text().strip(), url)
                    bing.append(combo)
            except:
                pass
        return bing