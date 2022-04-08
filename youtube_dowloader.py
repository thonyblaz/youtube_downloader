from pytube import YouTube

path="./videos"

link = input("Ingrese la URL: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("Elegir un formato")
dn_option = int(input("Enter la opcion: "))
dn_video = videos[dn_option]
dn_video.download(path)

print("Descarga exitosa!!!")