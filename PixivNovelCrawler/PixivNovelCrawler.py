from time import sleep
from pixivpy3 import *
from utils import *

def crawl_user_novels(user_id, output_folder):
    
    novels_info_dict_list=[]
    offset=0
    while True:
        print("Fetching user novel %s"%offset)
        novels=api.user_novels(user_id,offset=offset)
        novels_info_dict_list.extend(novels["novels"])
        if not novels["next_url"]:
            break
        else:
            offset=int(novels["next_url"].split("=")[-1])
    
    user=api.user_detail(user_id)["user"]
    author=user["name"]
    title=author+"の小説"
    user_description=user["comment"]
    
    output_folder=os.path.join(output_folder,title)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cover_link=user["profile_image_urls"]["medium"]
    cover_file=os.path.join(output_folder,"cover.jpg")
    print("Fetching Novel Cover: %s"%cover_link)
    api.download(cover_link,name=cover_file)

    book=MarkdownBook(title, author, user_description, "cover.jpg")
    novels_info_dict_list.reverse()
    for novel_info_dict in novels_info_dict_list:
        sleep(1)
        novel_id, novel_title, novel_description, novel_text, _ = getNovel(api, novel_info_dict)
        print("Fetched Text %s"%novel_id)
        book.appendChapter(novel_title, novel_description, novel_text)
    
    book.saveEPUB(output_folder)

def crawl_novel_serie(series_id:int, output_folder):
    
    print("Fetching Novel Serie: %s"%series_id)
    json_result = api.novel_series(series_id=series_id)
    serie_name=json_result["novel_series_detail"]["title"]
    serie_author=json_result["novel_series_detail"]["user"]["name"]
    serie_description=json_result["novel_series_detail"]["caption"]

    output_folder=os.path.join(output_folder,serie_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cover_link=json_result["novel_series_first_novel"]["image_urls"]["large"]
    cover_file=os.path.join(output_folder,"cover.jpg")
    print("Fetching Novel Cover: %s"%cover_link)
    api.download(cover_link,name=cover_file)

    book=MarkdownBook(serie_name, serie_author, serie_description, "cover.jpg")
    
    next_novel_info_dict=json_result["novel_series_first_novel"]
    while next_novel_info_dict!={}:
        sleep(1)
        novel_id, novel_title, novel_description, novel_text, next_novel_info_dict = getNovel(api, next_novel_info_dict)
        print("Fetched Text %s"%novel_id)
        book.appendChapter(novel_title, novel_description, novel_text)
    
    book.saveEPUB(output_folder)

def crawl_novels(things, output_folder):
    novel_id_list, book_name, book_author, book_description = things

    output_folder=os.path.join(output_folder,book_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    book=MarkdownBook(book_name, book_author, book_description, os.path.join(os.getcwd(),"cover.jpg"))

    for novel_id in novel_id_list:
        novel_id, novel_title, novel_description, novel_text, _ =getNovel(api, api.novel_detail(novel_id)["novel"])
        print("Fetched Text %s"%novel_id)
        book.appendChapter(novel_title, novel_description, novel_text)
    
    book.saveEPUB(output_folder)

if __name__=="__main__":

    root=os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    output_folder=os.path.join(root,"output")

    print("Logging")
    api = AppPixivAPI()
    # api.login("", "")   # login不能用了
    api.auth(refresh_token="REFRESH_TOKEN") # 现在只能用refresh_token

    # 爬取小说系列
    serie_list=[
        # 123456
    ]
    for i in serie_list:
        sleep(1)
        crawl_novel_serie(i, output_folder)
    
    # 爬取用户全部小说
    user_list=[
        # 123456
    ]
    for i in user_list:
        sleep(1)
        crawl_user_novels(i, output_folder)
    
    # 爬取指定小说
    novels_list=[
        ( [123456,123457,123458 ], "Book", "Author", "Description" )
    ]
    for i in novels_list:
        sleep(1)
        crawl_novels(i, output_folder)