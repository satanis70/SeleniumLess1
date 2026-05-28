from negative_tests.send_message_negative_tests import check_incorrect_name, check_incorrect_email
from positive_tests.send_message_positive_tests import check_correct_name, check_correct_current_address

INCORRECT_NAMES = [" ", "@", "f!#$%^&&*@$$$$", " niki "]
INCORRECT_EMAILS = [" niki ", "inbox.com", " ", "@"]
CORRECT_NAMES = ["ivan", "214214"]
CORRECT_EMAIL = "ivan@mail.com"
CORRECT_NAME = "ivan"
CORRECT_ADDRESSES = ["Novosibirsk, pl. Lenina 1", "Fasfasf"]
check_correct_name(CORRECT_NAMES, CORRECT_EMAIL)
check_incorrect_name(INCORRECT_NAMES, CORRECT_EMAIL)
check_incorrect_email(INCORRECT_EMAILS, CORRECT_NAME)
check_correct_current_address(CORRECT_ADDRESSES, CORRECT_NAMES, CORRECT_EMAIL)
