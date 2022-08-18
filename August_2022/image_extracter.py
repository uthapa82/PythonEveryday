import re

# extract the URL from some HTML text 
def image_extractor(str_url):
    pat = "src='(.*)"
    match = re.findall(pat, str_url)
    result = ''.join(match)
    print(result.replace("'</body></html>", ""))

def image_extractor_alternate(str_url):
    pat = r"www(\..+)+(\/.+)+\.jpg"
    match = re.search(pat, str_url)
    print(match.group(0))

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
    image_extractor_alternate(sample_url)
    
if __name__ == "__main__":
    main()