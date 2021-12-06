"""Web crawling and scraping.
BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import requests
from bs4 import BeautifulSoup

from util import utility

BASE_URL = 'https://www.imdb.com/'


def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed (allow_redirects=False)
    response = requests.get(url, allow_redirects=False)

    # Get text from the Response object, using <response>.text
    response_text = response.text

    # Create and return the corresponding BeautifulSoup object from the response text; use 'html.parser'
    return BeautifulSoup(response_text, features='html.parser')


def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """

    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key' \
    #             '&sort=moviemeter,asc&mode=detail&page=1'     # '&page=' in the end of the URL string, SPECIFIC case
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key' \
    #             '&page=1&sort=moviemeter,asc&mode=detail'     # '&page=' in the middle of the URL string, GENERAL case
    if '&page=' in start_url:
        url_chunks = start_url.split('&page=')
        return url_chunks[0] + '&page=' + str(page) + '&' + url_chunks[1].split('&', maxsplit=1)[1]
    return start_url


def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    Essentially, get_next_soup() just returns get_soup(get_specific_page(start_url, page)),
    i.e. converts the result of the call to get_specific_page(start_url, page), which is a string,
    into a BeautifulSoup object.
    """

    return get_soup(get_specific_page(start_url, page))


def crawl(url: str, max_pages=1):
    """Web crawler that collects info about movies from IMDb,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup()) from multi-page movie lists.
    Parameters: the url of the starting IMDb page and the max number of pages to crawl in case of multi-page lists.
    """

    for page in range(max_pages):
        yield get_next_soup(url, page + 1)
        page += 1


def get_4_digit_substring(a_string):
    """Returns the first 4-digit substring from a_string.
    It assumes that a_string contains a 4-digit substring representing a year.
    Useful when the year of a movie release on IMDb is represented like '(1988, part 2)', or '(video, 2002)'."""

    if len(a_string) >= 4:
        all_4_digit_substrings = [a_string[i:(i+4)] for i in range(len(a_string) - 3)]
        for substring in all_4_digit_substrings:
            if substring.isdigit():
                return substring
    return None


def get_m_info(start_url: str, max_pages=1):
    """
    Returns structured information about movies from a multi-page IMDb movie list.
    :param start_url: the url of the starting page of a multi-page IMDb movie list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the movies from a multi-page IMDb movie list
    Creates and uses the following data:
    - h3_list - a list of all 'h3' tags from multiple IMDb pages
                (each 'h3' tag contains: movie title, year of release, and (relative) link to the movie's IMDb page)
    - poster_list - a list of all relevant 'div' tags from multiple IMDb pages
                    (each such a 'div' tag contains the link to the poster of the corresponding movie)
    - info_list - a list of 3-tuples of information about each movie from h3_list ((title, year, link) tuples)
    - poster_link_list - a list of links to the posters of the movies from poster_list
    - complete_list - a list of 4-tuples of information about each movie from info_list and poster_list
    """

    # Initialize h3_list and poster_list as empty lists, as well as the generator object (crawl(start_url, max_pages))
    h3_list = []
    poster_list = []
    crawler = crawl(start_url, max_pages)

    # In a while True loop, get the next soup from the generator and use it to populate h3_list and poster_list
    # by EXTENDing them with the relevant tags from the soup
    # (find all 'h3' tags and 'div' tags that contain class="lister-item-image ribbonize" attribute);
    # make sure to exclude the last h3 from each soup, because it does not refer to a movie
    while True:
        try:
            next_soup = next(crawler)
            h3_list.extend(next_soup.find_all('h3')[:-1])
            poster_list.extend(next_soup.find_all('div', {'class': "lister-item-image ribbonize"}))
        except StopIteration:
            break

    # Initialize info_list as an empty list.
    # Repeat the following steps for each h3 in a for loop over h3_list:
    # Extract title from h3.a.text (strip() it in order to eliminate leading/trailing whitespace).
    # Extract year from <span class="lister-item-year text-muted unbold"> using h3.find(...).text,
    # and filter it by get_4_digit_substring(year); set year to 'unknown' if get_4_digit_substring(year) returns None.
    # Extract relative link from h3.a['href'] (make sure to lstrip('/') from it as well) and append it to BASE_URL.
    # Append (title, year, link) to info_list.
    info_list = []
    for h3 in h3_list:
        title = h3.a.text.strip()
        year = h3.find('span', {'class': "lister-item-year text-muted unbold"}).text
        year = get_4_digit_substring(year)
        year = year if year else 'unknown'
        link = BASE_URL + h3.a['href'].lstrip('/')
        info_list.append((title, link, year))

    # Initialize poster_link_list as an empty list.
    # In a for loop over all posters in poster_list, extract the poster link from poster.a.img['loadlate']
    # and append it to poster_link_list.
    # Note that extraction from poster.a.img['src'] does not work. Check the saved HTML code (soup) of the entire page.
    poster_link_list = []
    for poster in poster_list:
        poster_link = poster.a.img['loadlate']
        poster_link_list.append(poster_link)

    # Initialize complete_list as an empty list.
    # In a for loop over zip(info_list, poster_link_list) extract (title, year, link, poster_link) tuples and
    # append them to complete_list.
    # Return complete_list.
    complete_list = []
    for info, poster_link in zip(info_list, poster_link_list):
        title, year, link = info
        complete_list.append((title, year, link, poster_link))

    return complete_list


if __name__ == "__main__":
    # # Getting started
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key' \
    #             '&sort=moviemeter,asc&mode=detail&page=1'

    # # Create Response object from GET request, using requests.get(<url>, allow_redirects=False)
    # response = requests.get(start_url, allow_redirects=False)
    # print(type(response))
    # print()
    # print(response)
    # print()

    # # Get response text from Response object, using <response>.text
    # print(response.text[0:1000])
    # print()
    # print()

    # # Get BeautifulSoup object from response text, using BeautifulSoup(<response text>, features='html.parser')
    # soup = get_soup(start_url)
    # # soup = BeautifulSoup(response.text, features='html.parser')
    # print(type(soup))
    # print()
    # print(str(soup)[0:500])
    # print()

    # # Save BeautifulSoup object to an HTML file,
    # # using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace')
    # soup_file = utility.get_data_dir() / 'soup.html'
    # soup_file.write_text(str(soup), encoding='utf-8', errors='replace')
    # print()

    # # Demonstrate <BeautifulSoup object>.find('<tag>'), <BeautifulSoup object>.find_all(<tag>),
    # # <BeautifulSoup object>.find_all(<tag>, {'<tag_attr_name>': "<tag_attr_value>"});
    # # use, e.g., 'h3' or 'div' as the tags in the examples (e.g., <div class="lister-item-image ribbonize">)
    #
    # h3_first = soup.find('h3')
    # print(type(h3_first))
    # print()
    # print(h3_first)
    # # movie_items = soup.find_all('div', {'class': "lister-item-image ribbonize"})
    # # print(type(movie_items))
    # # print(len(movie_items))
    # # print('\n\n'.join([str(item) for item in movie_items[:3]]))
    # print()

    # # Demonstrate getting a 'subtag' for a tag (a bs4.element.Tag object), e.g. h3.find('<subtag>')
    # print(h3_first.find('span', {'class': "lister-item-index unbold text-primary"}))
    # print()

    # # Demonstrate getting an attribute value for a tag (a bs4.element.Tag object),
    # # e.g. h3.find('<subtag>'), filtered with <{'class': "<class name>"}>;
    # # alternatively: h3.find('<tag>')['<attr>'], h3.find('<subtag>').get('<attribute>'),
    # # h3.find('<subtag>').<attribute>,... (<attribute>: e.g. text)
    # print(h3_first.find('span', {'class': "lister-item-index unbold text-primary"}).name)
    # print(h3_first.find('span', {'class': "lister-item-index unbold text-primary"}).text)
    # print()

    # # Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
    # # <tag>.find_next_sibling() (returns just the first one)
    # print(h3_first.find('span', {'class': "lister-item-index unbold text-primary"}).string, '\n')
    # print(h3_first.find('span', {'class': "lister-item-index unbold text-primary"}).find_next_sibling(), '\n')
    # print(h3_first.find('span', {'class': "lister-item-index unbold text-primary"}).find_next_sibling().string, '\n')
    # print(h3_first.find('span', {'class': "lister-item-index unbold text-primary"}).find_next_siblings(), '\n')
    # # print(h3_first.find_next_sibling())
    # print()

    # # Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
    # # using BeautifulSoup(str(<bs4.element object>), 'html.parser')
    # movie_items = soup.find_all('div', {'class': "lister-item-image ribbonize"})
    # print(len(movie_items))
    # soup_first = BeautifulSoup(str(movie_items[0]), features='html.parser')
    # print(type(soup_first))
    # print()

    # # Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last)
    # movie = movie_items.pop(0)
    # print(movie)
    # print(len(movie_items))
    # print()

    # # Example: get all movie titles from an IMDb page
    # titles = []
    # # h3_set = soup.find_all('h3')
    # # print(len(h3_set))
    # # print(h3_set[50])
    # for h3 in soup.find_all('h3')[:-1]:
    #     print(h3.a.text)
    #     # titles.append(h3.a['href'])
    # print()

    # Test get_soup()
    start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
                'mode=detail&page=1&sort=moviemeter,asc'
    # print(get_soup(start_url))
    # print()

    # # Test get_specific_page()
    # print(get_specific_page(start_url, 3))
    # print()

    # # Test get_next_soup()
    # print(get_next_soup(start_url, page=3))
    # print()

    # # Test crawl()
    # crawler = crawl(start_url, 3)
    # while True:
    #     try:
    #         next_soup = next(crawler)
    #         for h3 in next_soup.find_all('h3')[:-1]:
    #             print(h3.a.text)
    #         print('\n')
    #     except StopIteration:
    #         break
    # print()

    # # Test get_4_digit_substring()
    # print(get_4_digit_substring('sdfah1234rety'))
    # print(get_4_digit_substring('sdfah1234556rety'))
    # print(get_4_digit_substring('sdfah126rety'))
    # print()

    # Test get_m_info()
    for info in get_m_info(start_url, 3):
        print(info)
    print()

    """
    HTML tags with examples:
    https://www.tutorialstonight.com/html-tags-list-with-examples.php

    start_url:
    https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&mode=detail&page=1&sort=moviemeter,asc

    Finding relevant tags:
    body/wrapper/root/pagecontent/content-2-wide/main/article/lister list detail sub-list/lister-list/lister-item mode-detail/
	    lister-item-image ribbonize/removable-wrapper/a
	    lister-item-content/<h3 class="lister-item-header">/
	        <a ...>
	        <span class="lister-item-year text-muted unbold">(2000)</span>
	"""

