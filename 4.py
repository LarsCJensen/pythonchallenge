import urllib.request


def _get_next_id(resp: str) -> str:
    temp_list = resp.split(" ")
    return temp_list[len(temp_list) - 1]


url_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
id = "12345"
while True:
    resp = urllib.request.urlopen(url_base + id).read().decode("utf-8")
    if resp == "Yes. Divide by two and keep going.":
        id = str(int(id) / 2)
    elif (
        "There maybe misleading numbers in the text." in resp
        or "Your hands are getting tired" in resp
    ):
        id = _get_next_id(resp)
    else:
        if "the next nothing" not in resp:
            break
        id = _get_next_id(resp)

print(resp)
