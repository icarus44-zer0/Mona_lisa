# Importing Necessary Modules
import requests  # to get image from the web
import shutil  # to save it locally
import os


def main():

    inc: int = 0
    parts: list(dict) = [
        {'name': 'Chapter5_Part1_', 'presentation': 'c9f9449a4bf84bb2a2cd851faf2c4be21d',
            'playbackTicket': 'a22f44e76b7f48f0932db6dc9e6d308c'},
        {'name': 'Chapter5_Part2_', 'presentation': '21948968bf82494295feebe348ebd5ca1d',
            'playbackTicket': 'a154c87fce984790b3efca3abca65e61'},
        {'name': 'Chapter5_Part3_', 'presentation': '9bc999c6be8c43a68687097e9eb33bb81d',
            'playbackTicket': '7892e1eb72f142898aa521899275022c'},
        {'name': 'Chapter5_Part4_', 'presentation': 'd41a276acc67498dbd99511c2cca77cf1d',
            'playbackTicket': '8191a85ef5a34e71bb0ac8b26a3209a3'},
    ]
    for i in range(len(parts)):
        for key, value in parts[i].items():
            name = parts[i].get('name')
            presentation = parts[i].get('presentation')
            playbackTicket = parts[i].get('playbackTicket')

            while True:
                inc = inc + 1
                slide = str(inc)
                slide = slide.zfill(4)
                slide = 'slide_' + slide

                image_url = (
                    "https://csus.mediasite.com/Mediasite/FileServer/f91cef6bec4e43d297b3859d0d54b19d29/Presentation/%(presentation)s/%(slide)s.jpg?playbackTicket=%(playbackTicket)s"
                    % locals())

                route = image_url.split("/")[-1]
                params = route.split("?", 1)
                filename = params[0]

                # Open the url image, set stream to True, this will return the stream content.
                r = requests.get(image_url, stream=True)
                if r.status_code != 200:
                    print("Image Couldn't be retreived\n")
                    print(image_url)
                    break
                elif r.status_code == 200:
                    r.raw.decode_content = True
                    with open('./Chapter5/' + name+filename, "wb") as f:
                        shutil.copyfileobj(r.raw, f)
                else:
                    print("Error: " + str(r.status_code))
                    break


if __name__ == "__main__":
    main()