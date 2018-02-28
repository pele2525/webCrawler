import requests
from bs4 import BeautifulSoup


class Film:
    tittle = ''
    rate = 0


def film_web_spider(year):
    url = 'http://www.filmweb.pl/ranking/film/' + str(year)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    title_list = []
    rate_list = []
    for link in soup.findAll('a', {'class': 'film__link'}):
        tittle = link.string
        title_list.append(tittle)
    for rate in soup.findAll(attrs={'class': 'rate__value'}):
        rate_value = rate.string
        rate_list.append(rate_value)
    film_list = [Film() for i in range(len(title_list))]
    for i in range(len(title_list)):
        film_list[i].tittle = title_list[i]
        film_list[i].rate = rate_list[i]
    return film_list


def print_film_list(film_list):
    for i in range(len(film_list)):
        print(film_list[i].tittle + film_list[i].rate)


def main():
    film_web_list = film_web_spider(2017)
    #losmovies_list = losmovies_spider() # TODO
    print_film_list(film_web_list)
    #compared_list = compare_titles(filmweb_list, losmovies_list) # TODO
    #print_film_list(compared_list) # TODO


if __name__ == "__main__":
    main()



