import requests
from bs4 import BeautifulSoup
import os


def to_ascii_character_string(txt):
    txt = txt.lower()
    txt = ''.join(txt.split())
    text_to_ascii = [c for c in txt if 97 <= ord(c) <= 122]
    return ''.join(text_to_ascii)


def get_article_body(country_code):
    html_response = requests.get(url=f'https://{country_code}.wikipedia.org/wiki/Special:Random')
    extractor = BeautifulSoup(html_response.content, 'html.parser')
    print(extractor.find(id="firstHeading").text)
    elements = extractor.find(id="bodyContent").find_all("p")
    return elements


def create_dir(root, dir_name):
    new_path = root + dir_name
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    return new_path


def letter_proportion(txt):
    no_of_chars = len(txt)
    unique_chars = sorted(set(txt))
    char_dict = dict.fromkeys(unique_chars, 0)
    for char in txt:
        char_dict[char] += (1 / no_of_chars)
    return char_dict


class FileProcessor:
    def __init__(self, country_codes, project_dir, articles_per_country, article_size):
        self.country_codes = country_codes
        self.project_dir = project_dir
        self.articles_per_country = articles_per_country
        self.article_size = article_size
        self.char_frequencies = dict.fromkeys(country_codes, [])
        self.country_dirs = {}

    def process(self):
        for code in self.country_codes:
            path = create_dir(self.project_dir, f"/data_{code}")
            self.country_dirs[code] = path
            for i in range(1, self.articles_per_country + 1):
                data_file = self.project_dir + f"/data_{code}/data_{i}.txt"
                file = open(data_file, 'w+')
                current_size = 0
                text = ""
                while current_size < self.article_size:
                    elements = get_article_body(code)
                    text = ""
                    for el in elements:
                        text += el.text
                    text = to_ascii_character_string(text)
                    current_size = len(text)

                file.write(to_ascii_character_string(text[:self.article_size]))
                file.close()
        self.__calculate_frequencies()

    def __calculate_frequencies(self):
        for country, ls in self.char_frequencies.items():
            for filename in os.scandir(path=self.country_dirs[country]):
                with open(filename.path, 'r') as file:
                    txt = sorted(file.read().rstrip())
                    proportions = letter_proportion(txt)
                    ls.append(proportions)
        print(self.char_frequencies)