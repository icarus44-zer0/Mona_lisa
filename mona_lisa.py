import requests 
import shutil

def main():

    inc: int = 0

    parts: list(dict) = [
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},    
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},    
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},    
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},    
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},    
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},    
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},    
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},    
        {'dir': '', 'name': '', 'presentation': '','playbackTicket': ''},
    ]

    for i in range(len(parts)):
        seperator = '_'

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
                    r.close()
                    break
                elif r.status_code == 200:
                    r.raw.decode_content = True
                    with open('./'+ dir_name + '/' + dir_name + seperator + part_name + seperator + slide_name, "wb") as f:
                        shutil.copyfileobj(r.raw, f)
                else:
                    print("Error: " + str(r.status_code))
                    r.close()
                    break

if __name__ == "__main__":
    main()