import logging
import requests
def add(str):
    if( len(str) == 0) : return 0
    else:
        if str[:2] == '//':
            # On Delimiter change detection
            numbers_str = []
            delimiter = str[2]
            numbers_str = str[4:].split(delimiter)

        else:
            numbers_str = []
            # Split string by comma
            numbers_comma_split = str.split(',')
            # SPlit string elements again by newline
            for number in numbers_comma_split:
                numbers_str = numbers_str + number.split('\n')
        # Check for negatives
        negatives = []
        for number_str in numbers_str:
            if int(number_str) < 0:
                negatives.append(number_str)
        # If negatives exist, throw NegativesUnsupported exception
        if len(negatives) > 0 : raise NegativesUnsupported("negatives ".join(negatives) + " unsupported")
        numbers_int = [int(i) for i in numbers_str]
        sum_result = 0
        for i in range(len(numbers_int)):
            sum_result = sum_result + numbers_int[i]

        # When logging throws an exception, the exception message is sent to a web server
        try:
            logging.info(sum_result)
        except Exception as err:
            exception_type = type(err).__name__
            requests.get('http://some.web.server/' + exception_type)
        
        return sum_result

class NegativesUnsupported(Exception):
    "Raised when at least an input is negative"
    pass