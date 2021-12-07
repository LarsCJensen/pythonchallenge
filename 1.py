import string


def translate(str_to_translate: str) -> str:
    alphabet = list(string.ascii_lowercase)
    translated = ""
    for letter in str_to_translate:
        if letter not in alphabet:
            translated = translated + letter
        else:
            letter_index = alphabet.index(letter) + 2
            print(letter_index)
            if letter_index >= len(alphabet):
                letter_index = letter_index - len(alphabet)
            translated = translated + alphabet[letter_index]
    return translated


to_translate = list(
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
)

print(translate(to_translate))

to_translate_url = "map"
print(translate(to_translate_url))
