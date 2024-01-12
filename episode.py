import requests
from lxml import etree

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def get_episode_content(url):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("status_code error")
        return None
    html = response.text
    tree = etree.HTML(html)

    title = tree.xpath('//p[@class="epi_t"]/text()')[0].strip()
    article = tree.xpath('//article[@class="clear epi_c"]/p')
    fp.write(title+'\n')
    for p in article:
        text = p.xpath('./text()')[0]
        fp.write(text+'\n')
    

def get_episode_content_url(main_url):
    response = requests.get(main_url, headers=headers)
    if response.status_code != 200:
        print("status_code error")
        return None
    html = response.text
    tree = etree.HTML(html)

    ul = tree.xpath('//div[@class="epipage clear"]/ul/li/a/@href')
    url_list = []
    for url in ul:
        url_list.append("https://www.tvmao.com"+url)
    return url_list



if __name__ == "__main__":
    main_url = "https://www.tvmao.com/drama/aGslXGFh/episode"
    url_list = get_episode_content_url(main_url)

    fp = open("zhi_fou.txt", "w")
    for url in url_list:
        get_episode_content(url)
    fp.close()