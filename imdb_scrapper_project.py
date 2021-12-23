import requests
from bs4 import BeautifulSoup

userMovieName = input("Enter movie: ")
res = requests.get("https://www.imdb.com/chart/top/")
html = res.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class':'lister-list'})
trs = tbody.findAll('tr')
for tr in trs:
    td = tr.find('td', {'class':'titleColumn'})
    movieName = td.a.string.strip()
    if movieName == userMovieName:
        movieId = td.a['href']
        movieUrl = f"https://www.imdb.com{movieId}"
        print(movieUrl)
        res2 = requests.get(movieUrl)
        html = res2.text
        soup2 = BeautifulSoup(html, 'html.parser')
        li = soup2.find('li', {'data-testid':'title-pc-principal-credit'})

        directorName = li.div.ul.li.a.text
        directorId = li.div.ul.li.a['href']
        directorUrl = f"https://www.imdb.com/{directorId}"
        print(directorName, directorUrl)

        res3 = requests.get(directorUrl)
        html = res3.text
        soup3 = BeautifulSoup(html, 'html.parser')
        knownFor = soup3.find('div', {'id':'knownfor'})
        movieDivs = knownFor.findAll('div', {'class':'knownfor-title'})
        recommendedMovies = []
        for div in movieDivs:
            movieNamediv = div.find('div', {'class':'knownfor-title-role'})
            print(movieNamediv.a.string)
            recommendedMovies.append(movieNamediv.a.string)
        recommendedMovies = ','.join(recommendedMovies)
        print(recommendedMovies)


