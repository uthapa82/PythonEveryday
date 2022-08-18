import re

# extract the URL from some HTML text 
def image_extractor(str_url):
    pass

# w/o using regex
def normal_link_extractor(str_url):
    keyword = "src='"
    before_url, keyword, after  = str_url.partition(keyword)
    print(after.replace("'</body></html>", ""))
    
def main():
    sample_url = "<html><head></head><body><img src='www.geeksforgeeks.org/sample/62.jpg'</body></html>"
    sample_url_2 = "<html><head></head><body><img src='www.geeksforgeeks.org/sample/99.jpg'</body></html>"
    image_extractor(sample_url)
    normal_link_extractor(sample_url_2)
    
if __name__ == "__main__":
    main()