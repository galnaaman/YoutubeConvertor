from django.shortcuts import render, redirect
from pytube import YouTube


def homepage(request):
    if request.method == "GET":
        return render(request, "homepage.html")
    else:
        if request.method == "POST":
            link = request.POST["link"]
            isVaild = True
            if "https://www.youtube.com/watch" in link:

                yt = YouTube(link)
                ys = yt.streams.get_highest_resolution()
                print(ys)
                x = ys.download()
                # Title of video
                print("Title:", yt.title)
                title = yt.title
                # Number of views of video
                print('Number of views:', yt.views)
                views = yt.views
                # Length of the video
                print("Length of video:", yt.length, " seconds")
                length = yt.length
                rating = yt.rating
                print(rating)
                if length >= 60:
                    length_minutes = length // 60
                    length_seconds = length % 60
                    description = yt.description
                    thumbnail = yt.thumbnail_url
                    context = {"isVaild": isVaild, "title": title, "views": views, "minutes": length_minutes,
                               "seconds": length_seconds,
                               "description": description, "thumbnail": thumbnail, "rating": rating, "link":link, "x": x}
                    return render(request, "homepage.html", context,)
                else:
                    description = yt.description
                    thumbnail = yt.thumbnail_url
                    context = {"isVaild": isVaild, "title": title, "views": views, "description": description,
                               "thumbnail": thumbnail, "length": length, "rating": rating}
                    return render(request, "homepage.html", context)
            else:
                isVaild = False
                error = "In Vaild Youtube link"
                context = {"error": error, "isVaild": isVaild}
                return render(request, "homepage.html", context)


def download_vid(request):
    link = request.POST["link"]
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    return redirect("homepage")

# from pytube import YouTube
#
# link = input("Enter the link : \n >> ")
# yt = YouTube(link)
# # Title of video
# print("Title:", yt.title)
# # Number of views of video
# print('Number of views:', yt.views)
# # Length of the video
# print("Length of video:", yt.length, " seconds")
#
# # Rating
# print("Ratings: ", yt.rating)
#
# ys = yt.streams.get_highest_resolution()
#
# print("Downloading...")
# ys.download('location')
# print("Download completed!!")
