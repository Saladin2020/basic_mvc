import requests
from bs4 import BeautifulSoup
from nltk.corpus import words


class UrlFetchError(Exception):
    """Raised when the target URL cannot be fetched."""
    pass


class Cwordurl:
    def __init__(self, url):
        self.__is_word = {}
        self.__not_word = {}
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as exc:
            # Ensure object has empty results on failure
            self.__is_word = {}
            self.__not_word = {}
            raise UrlFetchError(f"Failed to fetch URL: {url}") from exc

        self.__soup = BeautifulSoup(response.content, 'html.parser')
        self.__dat = self.__prepocess()
        self.__process()

    def __prepocess(self):
        s = self.__soup.get_text().split()
        d = {}
        for x in s:
            if x not in d.keys():
                d[x] = 1
            else:
                d[x] = d[x]+1
        return d

    def __process(self):
        is_word = {}
        not_word = {}
        for key, value in sorted(self.__dat.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
            if key in words.words():
                is_word[key] = value
                #is_word = is_word + key + " : " + value.__str__()+"<br>"
            else:
                not_word[key] = value
                #not_word = not_word + key + " : " + value.__str__()+"<br>"
            self.__is_word = is_word
            self.__not_word = not_word

    def get_isword(self):
        return self.__is_word

    def get_notword(self):
        return self.__not_word
