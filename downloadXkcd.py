#! python3
'''Downloads every single XKCD comic.'''

import os,  requests, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print(f'Downloading page {url}')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print(f'Downloading image {comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()
        imagefile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
print('Done')
