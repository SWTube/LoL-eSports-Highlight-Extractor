import unicodedata


def fill_str_with_space(input: str, max_size: int, fill_char: str = ' ') -> str:
    """
    - 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함.
    - 최대 길이(max_size)는 40이며, input_s의 실제 길이가 이보다 짧으면
    남은 문자를 fill_char로 채운다.
    """
    length = 0
    for character in input:
        if unicodedata.east_asian_width(character) in ['F', 'W']:
            length += 1.5
        else:
            length += 1
    return input + fill_char * (max_size - int(length + 0.5))


class Text:
    def __init__(self, ocr_list: list, event_type: str):
        assert type(ocr_list[0]) == list
        assert type(ocr_list[1]) == str
        assert type(ocr_list[2]) == float
        self.__bounding_box = ocr_list[0]
        self.__text = ocr_list[1]
        self.__confidence_level = ocr_list[2]
        self.__event_type = event_type

    def __str__(self) -> str:
        return_string = self.__event_type.ljust(8)
        return_string += fill_str_with_space(self.__text, 40) \
                         + "\t[[" + str(self.__bounding_box[0][0]).rjust(4) \
                         + ", " + str(self.__bounding_box[0][1]).rjust(4) \
                         + "], [" + str(self.__bounding_box[2][0]).rjust(4) \
                         + ", " + str(self.__bounding_box[2][1]).rjust(4) \
                         + "]]\t" + str(self.__confidence_level)

        return return_string

    @property
    def bounding_box(self) -> list:
        return self.__bounding_box

    @property
    def text(self) -> str:
        return self.__text

    @property
    def confidence_level(self) -> float:
        return self.__confidence_level

    @property
    def event_type(self) -> str:
        return self.__event_type

    def get_language(self) -> str:
        for c in self.__text:
            if ord('가') <= ord(c) <= ord('힣'):
                return "ko"
            elif ord('a') <= ord(c.lower()) <= ord('z'):
                return "en"
        return "ko"
