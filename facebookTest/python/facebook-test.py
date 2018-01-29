import facebook
import requests

# graph = facebook.GraphAPI(access_token="EAACEdEose0cBAI5RXZBztzlcHvHDQx6WqbwkDFqbCxEGg17lUYN0ZA27FFKM3ult7Qz1HkUExYLJc4ZAZAsfKoc8JNExF79zVBKfnGqS1hQQXVm89fnUM40FAZByBYlnBjMaWzY6Mfe1SmXf042o9pdoFyH7EgkV12Kpa5jwdXtexjVxOhJTQTj6gZCButkH0ZD", version="2.11")
#
# graph.
a = []
def  getPostLike(id):
        #print(id)
        postUrl =  "https://graph.facebook.com/v2.11/" + id +"/likes?summary=true&access_token=EAACEdEose0cBAGEXlnR0Pi6PAaOefNM8epxM5weGNd3MP1IlLZC10Os53moAV3Xb46L6hMH8hcyN5atgsgjnpHvS8lPIEnrr8ZAqFplatHc9px4euq3E3JhS7OjtYhH9dJEZCgBZBP0AiEpKA0NYcm0qBswP9tfAaXcqnMCtaJbFCdiqNSBQjyy4EL07P3QAJYlPcYVJGAZDZD"
        # print(postUrl)
        postLike = requests.get(postUrl).json().get("summary", { "total_count" : 0})['total_count']
        print(str(postLike))
        # print(str(postLike) + " : " + text)
        getStatsandCounts(postLike)

def getAllIds(response):
    idData = response.get("data", {})
    getIdsFromData(idData)
    idPaging = response.get("paging",{})
    #print(idPaging)
    if( idPaging != {}):

        pagingUrl = idPaging.get("next",{})
        if(pagingUrl != {}):
        # print(pagingUrl)
            urlHandler(pagingUrl)

def getIdsFromData(array):
    for a in array:
        # if 'message' in a:
        #     print('yes')
        #     print(a)
        # else:
        #     print('no')
        id = a.get("id",{})
        # text =  a.get("message","")
        # print(id)
        if(id!={}):
            getPostLike(id)
        # if(id != ""):
        #     getPostLike(id,text)
        # else:
        #     break

def getStatsandCounts(value):
    a.append(value)
    #a.append(5)

def urlHandler(url):
    fb_response = requests.get(url).json()
    #print(fb_response)
    getAllIds(fb_response)

# data = fb_response.get("data", "")
# paging = fb_response.get("paging", "")

# for datum in data:
#     print(datum)
#     print(datum['id'])
#     print(datum['paging'])
#     getPostLike(datum['id'])

# getPostLike('10201934648744209_10210756746171131')

def main():
    url = "https://graph.facebook.com/v2.11/me/posts?access_token=EAACEdEose0cBAGEXlnR0Pi6PAaOefNM8epxM5weGNd3MP1IlLZC10Os53moAV3Xb46L6hMH8hcyN5atgsgjnpHvS8lPIEnrr8ZAqFplatHc9px4euq3E3JhS7OjtYhH9dJEZCgBZBP0AiEpKA0NYcm0qBswP9tfAaXcqnMCtaJbFCdiqNSBQjyy4EL07P3QAJYlPcYVJGAZDZD"
    #urlHandler('https://graph.facebook.com/v2.11/10201934648744209/posts?limit=25&__paging_token=enc_AdCTILxphyoNFKyvEhbY43ZBPzz37kgTNzo3ETPf0TZCie3VrmzRfV7ZCFdV3CQZAjzA3OKuQepBCKgfJRzKS0bloaiQ&access_token=EAACEdEose0cBAGEXlnR0Pi6PAaOefNM8epxM5weGNd3MP1IlLZC10Os53moAV3Xb46L6hMH8hcyN5atgsgjnpHvS8lPIEnrr8ZAqFplatHc9px4euq3E3JhS7OjtYhH9dJEZCgBZBP0AiEpKA0NYcm0qBswP9tfAaXcqnMCtaJbFCdiqNSBQjyy4EL07P3QAJYlPcYVJGAZDZD&until=1261977401')
    urlHandler(url)
    total_likes = sum(a)
    print("total like is: " + str(total_likes))
    total_posts = len(a)
    print("total posts is: " + str(total_posts))
    average_like = total_likes/total_posts
    print("average like is: " + str(average_like))


if __name__ == '__main__':
    main()