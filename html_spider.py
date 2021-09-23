import os
import urllib.request
import patoolib

ARCHIVES_PATH   = 'E:\\stud\\spark\\archives'
BOOKS_PATH      = 'E:\\stud\\spark\\books'
BOOK_NAMES_FILE = 'E:\\stud\\spark\\author_book\\book_names.txt'
URLS            = 'E:\\stud\\spark\\urls.txt'

def book_pages_fetcher(links):
    book_page_urls = []

    for link in links:

        fp = urllib.request.urlopen(link)
        bytes = fp.read()
        html = bytes.decode("utf8")
        author_name = link[link.rfind('/') + 1: link.rfind('html') - 1]
        book_page_url = '//royallib.com/book/' + author_name
        start = 0

        while html.find(book_page_url, start):
            start = html.find(book_page_url, start)
            end = html.find('\"', start)
            book_url = html[start:end]

            book_name = book_url[book_url.rfind('/') + 1 : book_url.rfind('html') - 1]
            with open(BOOK_NAMES_FILE, 'w') as file:
                    file.write(author_name + ' ' + book_name + '\n')

            if book_url in book_page_urls:
                break
            book_page_urls.append(book_url)
            start = end + 1
        fp.close()

    return book_page_urls
#
def book_loader(url, target_path):
    path = os.path.join(ARCHIVES_PATH, url[url.rfind('/') + 1 : url.rfind('.')] + '.zip')
    book_name = path[path.rfind('\\') + 1 : path.rfind('.')]
    urllib.request.urlretrieve('https:' + url, path)
    patoolib.extract_archive(path, outdir=target_path)
    folder_cleaner(BOOKS_PATH)
    a = os.listdir(BOOKS_PATH)[-1]
    os.rename(BOOKS_PATH + '\\' + os.listdir(BOOKS_PATH)[-1], BOOKS_PATH + '\\' + book_name + '.txt')

def txt_archive_url(book_page_url):
    zip_arch_url = ''
    zip_arch_url += book_page_url[:book_page_url.find('book')]
    zip_arch_url += 'get/txt'
    zip_arch_url += book_page_url[book_page_url[:book_page_url.rfind('/')].rfind('/') : book_page_url.rfind('.')]
    zip_arch_url += '.zip'
    return zip_arch_url

def folder_cleaner(path):
    for filename in os.listdir(path):
        if not filename.endswith('.txt'):
            os.remove(path + '\\' + filename)

def urls_getter(path):
    with open(path, 'r') as file:
        urls = file.readlines()
    urls = [line.rstrip() for line in urls]
    return urls

# book_loader()

author_urls = urls_getter(URLS)
books_urls = book_pages_fetcher(author_urls)
for book_url in books_urls:
    if len(book_url) != 0:
        zip_url = txt_archive_url(book_url)
        book_loader(zip_url, BOOKS_PATH)

