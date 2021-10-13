import requests 
import shutil

# master: list(dict) = [
#         {'dir': '', 'name': 'Part1_', 'presentation': '','playbackTicket': ''},
#         {'dir': '', 'name': 'Part2_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part3_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part4_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part5_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part6_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part7_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part8_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part9_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part10_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part11_', 'presentation': '','playbackTicket': ''},    
#         {'dir': '', 'name': 'Part12_', 'presentation': '','playbackTicket': ''},  
# ]

# example: list(dict) = [
#         {'dir': 'Chapter5', 'name': 'Part1_', 'presentation': 'c9f9449a4bf84bb2a2cd851faf2c4be21d','playbackTicket': 'a22f44e76b7f48f0932db6dc9e6d308c'},
#         {'dir': 'Chapter5', 'name': 'Part2_', 'presentation': '21948968bf82494295feebe348ebd5ca1d','playbackTicket': 'a154c87fce984790b3efca3abca65e61'},
#         {'dir': 'Chapter5', 'name': 'Part3_', 'presentation': '9bc999c6be8c43a68687097e9eb33bb81d','playbackTicket': '7892e1eb72f142898aa521899275022c'},
#         {'dir': 'Chapter5', 'name': 'Part4_', 'presentation': 'd41a276acc67498dbd99511c2cca77cf1d','playbackTicket': '8191a85ef5a34e71bb0ac8b26a3209a3'},
#         {'dir': 'Chapter5', 'name': 'Part5_', 'presentation': 'b937d69512764ba99889218f883458a21d','playbackTicket': ''},
#         {'dir': 'Chapter5', 'name': 'Part6_', 'presentation': '2c4c848deac44e17a83403e09d1c63f71d','playbackTicket': '8979f35f48ec440c80876a1c9e21a09b'},
#         {'dir': 'Chapter5', 'name': 'Part7_', 'presentation': '542dd51577be4ca49850b8580c9ce4761d','playbackTicket': '6a8a2a367f0947a8b687a8bb8eac546f'},
#         {'dir': 'Chapter5', 'name': 'Part8_', 'presentation': 'c7bad6d601774bf3b01ed7a9e0c310571d','playbackTicket': 'caa0465f05e74752af79c29b6d266ea3'},
#         {'dir': 'Chapter5', 'name': 'Part9_', 'presentation': '28cae310818f468fa0ac30ac608a59b21d','playbackTicket': 'acde275a5e784bb6b2effb0ba7578a2b'},
#         {'dir': 'Chapter5', 'name': 'Part10_', 'presentation': '01a7b46b716c45d6b70f7215398cd0791d','playbackTicket': '8a17f3708aa745629a1ecb01cb59c738'},
#         {'dir': 'Chapter5', 'name': 'Part11_', 'presentation': '624c07dbe19f4283914f17b064cedba01d','playbackTicket': 'c362844c23b2431eaa29d8367f5a2c5e'},
# ]

def main():

    inc: int = 0
    parts: list(dict) = [
        {'dir': 'Chapter4', 'name': 'Part1_', 'presentation': '8dc11eb93e5b46e09fed6b3788b3b5fd1d','playbackTicket': '0465ca62f5804b84ab25766f830a6182'},
        {'dir': 'Chapter4', 'name': 'Part2_', 'presentation': 'c740905ba81c488d90cf610fccebce041d','playbackTicket': '79562ca6ef684b6f80596d14b4c9c55c'},    
        {'dir': 'Chapter4', 'name': 'Part3_', 'presentation': '4ccf4f7690aa49dd8dfd7f3f0626d9511d','playbackTicket': 'e68b61ffd49a4e17a458b594f1cd3a1e'},    
        {'dir': 'Chapter4', 'name': 'Part4_', 'presentation': 'e3807f4c7e6849288157b76c3afd9ea01d','playbackTicket': '8aa69840c86b4883864bcc82c8e08467'},    
        {'dir': 'Chapter4', 'name': 'Part5_', 'presentation': '2fff5bac17464c8fb35a9237c5fb4c4b1d','playbackTicket': 'd0e758e37bfc4f4aba563b3024514837'},    
        {'dir': 'Chapter4', 'name': 'Part6_', 'presentation': 'fee19ce0fc1b4cd19f112bf05c52b8781d','playbackTicket': '0edfddbd9cf94c4aacd28208b4fba46a'},    
        {'dir': 'Chapter4', 'name': 'Part7_', 'presentation': '3486c2b7f27e4b18b0602b8b6c7908881d','playbackTicket': 'b444ae84f35b4302bf07a7de914a6e1f'},    
        {'dir': 'Chapter4', 'name': 'Part8_', 'presentation': 'ee4d41504c8c4750874256e9bc1d48631d','playbackTicket': '49369beb96914414acf4ad439ca8abc8'},    
        {'dir': 'Chapter4', 'name': 'Part9_', 'presentation': 'e9fe79193ec140bfb4d5b7457f0b0f861d','playbackTicket': 'a91fd8c656e0476dbc7987489723b8e1'},    
        {'dir': 'Chapter4', 'name': 'Part10_', 'presentation': 'eb823cc16ab54c59bb83e58eaa96c7d71d','playbackTicket': '152d7c9f33ca4c46b707ab2f8a88ba59'},    
    ]

    for i in range(len(parts)):
        for key, value in parts[i].items():
            dir_name = parts[i].get('dir')
            part_name = parts[i].get('name')
            presentation = parts[i].get('presentation')
            playbackTicket = parts[i].get('playbackTicket')
            inc = 0
            while True:
                inc += 1
                slide = str(inc)
                slide = slide.zfill(4)
                slide = 'slide_' + slide

                image_url = (
                    "https://csus.mediasite.com/Mediasite/FileServer/f91cef6bec4e43d297b3859d0d54b19d29/Presentation/%(presentation)s/%(slide)s.jpg?playbackTicket=%(playbackTicket)s"
                    % locals())

                route = image_url.split("/")[-1]
                params = route.split("?", 1)
                slide_name = params[0]

                # Open the url image, set stream to True, this will return the stream content.
                r = requests.get(image_url, stream=True)
                if r.status_code != 200:
                    print("Image Couldn't be retreived\n")
                    print(image_url)
                    break
                elif r.status_code == 200:
                    r.raw.decode_content = True
                    with open('./'+ dir_name + '/' + part_name + slide_name, "wb") as f:
                        shutil.copyfileobj(r.raw, f)
                else:
                    print("Error: " + str(r.status_code))
                    break

if __name__ == "__main__":
    main()