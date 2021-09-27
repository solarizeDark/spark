import os
import urllib.request
import patoolib

ARCHIVES_PATH   = 'E:\\stud\\spark\\archives'
BOOKS_PATH      = 'E:\\stud\\spark\\books'
BOOK_NAMES_FILE = 'E:\\stud\\spark\\author_book\\book_names.txt'
URLS            = 'E:\\stud\\spark\\urls.txt'
URLS_ERROR      = 'E:\\stud\\spark\\errors.txt'

def book_pages_fetcher(html, author_page_url):
    start = 0
    book_page_urls = []
    while html.find(author_page_url, start):
        start = html.find(author_page_url, start)
        end = html.find('\"', start)
        book_url = html[start:end]

        if book_url in book_page_urls:
            break
        book_page_urls.append(book_url)
        start = end + 1
    return book_page_urls

def info_fetcher(links):
    book_page_urls = []

    for link in links:
        fp = urllib.request.urlopen(link)
        bytes = fp.read()
        html = bytes.decode("utf8")
        author_name = link[link.rfind('/') + 1: link.rfind('html') - 1]
        author_page_url = '//royallib.com/book/' + author_name
        book_page_urls.extend(book_pages_fetcher(html, author_page_url))
        fp.close()
    return book_page_urls
#
def book_loader(url, target_path):

    path = os.path.join(ARCHIVES_PATH, url[url.rfind('/') + 1 : url.rfind('.')] + '.zip')
    book_name = path[path.rfind('\\') + 1 : path.rfind('.')]
    urllib.request.urlretrieve('https:' + url, path)

    # book couldnt been get for free
    # or file already exists
    try:
        patoolib.extract_archive(path, outdir=target_path)
    except (patoolib.util.PatoolError, FileExistsError):
        with open(URLS_ERROR, 'a') as file:
            file.write(book_name + '\n')
        return

    folder_cleaner(BOOKS_PATH)

    try:
        os.rename(BOOKS_PATH + '\\' + os.listdir(BOOKS_PATH)[-1], BOOKS_PATH + '\\' + book_name + '.txt')
    except FileExistsError:
        with open(URLS_ERROR, 'a') as file:
            file.write(book_name + '\n')
        return

    author_name = url[:url.rfind('/')]
    author_name = author_name[author_name.rfind('/') + 1:]
    with open(BOOK_NAMES_FILE, 'a') as file:
        file.write(author_name + ' ' + book_name + '\n')


def txt_archive_url(book_page_url):
    zip_arch_url = ''
    zip_arch_url += book_page_url[:book_page_url.find('book')]
    zip_arch_url += 'get/txt'
    zip_arch_url += book_page_url[book_page_url[:book_page_url.rfind('/')].rfind('/') : book_page_url.rfind('.')]
    zip_arch_url += '.zip'
    return zip_arch_url

def folder_cleaner(path):
    for filename in os.listdir(path):
        if os.path.isdir(path + "\\" + filename):
            folder_cleaner(path + "\\" + filename)
        elif not filename.endswith('.txt'):
            os.remove(path + '\\' + filename)

def urls_getter(path):
    with open(path, 'r') as file:
        urls = file.readlines()
    urls = [line.rstrip() for line in urls]
    return urls

author_urls = urls_getter(URLS)
books_urls = info_fetcher(author_urls)
for book_url in books_urls:
    if len(book_url) != 0:
        zip_url = txt_archive_url(book_url)
        book_loader(zip_url, BOOKS_PATH)

