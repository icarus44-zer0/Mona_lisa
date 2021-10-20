import requests
import shutil
import os
from typing import List, Dict, Any
from furl import furl


def example():
    # url must be in form
    # https://csus.mediasite.com/Mediasite/FileServer/f91cef6bec4e43d297b3859d0d54b19d29/Presentation/3b45770d114040cc85754e7b357e9a6b1d/slide_0001_122_768.jpg?playbackTicket=10a1ea5238724982a180516f545e93e1
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


def make_parts_v2(parts: List[Dict], dir: str, name: str) -> List[Dict]:

    count = 0
    p_offset: int = 96  # presentation/
    p_offset2: int = 130  # id len

    with open('urls.txt') as f:
        lines = f.readlines()

    for line in range(len(lines)):
        count += 1

        url = lines[line]
        pres = url[p_offset: p_offset2]

        f = furl(url)
        ticket: str = f.args['playbackTicket']
        ticket: str = ticket.strip()

        temp: dict = {'dir': dir, 'name': name + str(count),
                      'presentation': pres, 'playbackTicket': ticket}

        parts.append(temp)
        print(temp)

    print(parts)
    return parts


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
                    "https://csus.mediasite.com/Mediasite/FileServer/f91cef6bec4e43d297b3859d0d54b19d29/Presentation/%(presentation)s/%(slide)s.jpg?playbackTicket=%(playbackTicket)s"
                    % locals())

                print(image_url)
                route = image_url.split("/")[-1]
                params = route.split("?", 1)
                slide_name = params[0]

                # Open the url image, set stream to True, this will return the stream content.
                try:
                    r = requests.get(image_url, stream=True)
                    if r.status_code != 200:
                        raise Exception('End of section ' + part_name)
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
    parts = make_parts_v2(parts=parts, dir=dirname, name=filename)
    get_slides(parts)


if __name__ == "__main__":
    main()
