import looter as lt

domain = 'https://xkcd.com'

def crawl(url):
    tree = lt.fetch(url)
    imgs = tree.cssselect('#comic img')
    lt.async_save_imgs(imgs)


if __name__ == '__main__':
    tasklist = [f'{domain}/{i}' for i in range(1, 1960)]
    result = [crawl(task) for task in tasklist]