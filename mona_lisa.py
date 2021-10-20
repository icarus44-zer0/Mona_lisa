import typing
import requests
import shutil
import os
from typing import List, Dict, Any


def example():
    example_parts: List[Dict] = [
        {'dir': '', 'name': '', 'presentation': '', 'playbackTicket': ''},
        {'dir': '', 'name': '', 'presentation': '', 'playbackTicket': ''},
        {'dir': '', 'name': '', 'presentation': '', 'playbackTicket': ''},
    ]


def make_dir(parentdir, dirname):
    try:
        path = os.path.join(parentdir, dirname)
        os.mkdir(path)
    except:
        return


def make_parts(parts: List[Dict], dir: str, name: str) -> List[Dict]:

    p_offset: int = 96  # presentation/
    p_offset2: int = 130  # id len
    t_offset: int = 169  # playbackTicket/
    t_offset2: int = 201  # id len (EOL would be simpler)
    count = 0

    with open('urls.txt') as f:
        lines = f.readlines()

    for line in range(len(lines)):
        count += 1
        string = lines[line]

        pres = string[p_offset: p_offset2]
        ticket = string[t_offset: t_offset2]

        temp: dict = {'dir': dir, 'name': name + str(count),
                      'presentation': pres, 'playbackTicket': ticket}
        parts.append(temp)

    return parts


def get_slides(parts: List[Dict]):
    inc: int = 0

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
                    "https://csus.mediasite.com/Mediasite/FileServer/f91cef6bec4e43d297b3859d0d54b19d29/Presentation/%(presentation)s/%(slide)s_819_512.jpg?playbackTicket=%(playbackTicket)s"
                    % locals())

                print(image_url)
                route = image_url.split("/")[-1]
                params = route.split("?", 1)
                slide_name = params[0]

                # Open the url image, set stream to True, this will return the stream content.
                try:
                    r = requests.get(image_url, stream=True)
                    if r.status_code != 200:
                        raise Exception('End of slides')
                    else:
                        r.raw.decode_content = True
                        with open('./' + dir_name + '/' + dir_name + seperator + part_name + seperator + slide_name, "wb") as f:
                            shutil.copyfileobj(r.raw, f)
                except Exception as er:
                    r.close()
                    print(er)
                    break


def main():
    parts: List[Dict] = []
    parentdir = '.'
    dirname = 'Chapter6'
    filename = 'part'
    make_dir(parentdir=parentdir, dirname=dirname)
    parts = make_parts(parts=parts, dir=dirname, name=filename)
    get_slides(parts)


if __name__ == "__main__":
    main()
