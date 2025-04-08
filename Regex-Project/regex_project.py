import re

def find_email(text):
    """
    This function finds and returns an email address from the given text.
    """
    pattern = r"[a-z0-9!#$%&'\"*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'\"*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}"
    match = re.search(pattern, text)
    if match:
        return match.group()


def extract_emails_and_phones(text):
    """
    This function finds and returns all email addresses and phone numbers from the given text.
    """
    pattern_emails = r"[a-z0-9!#$%&'\"*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'\"*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}"
    pattern_phone_numbers = r"(?=(?:\D*\d){7,15}\D*)(?:(?:\+|00)\d{1,3}[ -]?)?(?:\(\d{1,4}\)|\d{1,4})(?=[- \d])[ -]?\d{2,4}(?:[ -]?\d{2,4}){1,3}(?:[ -]?(?:ext\.?|x)[ -]?\d{1,5})?"

    match_emails = re.findall(pattern_emails, text)
    match_phone_numbers = re.findall(pattern_phone_numbers, text)

    if match_emails and match_phone_numbers:
        return (match_emails, match_phone_numbers)
    elif match_emails:
        return match_emails
    elif match_phone_numbers:
        return match_phone_numbers

def validate_email(email):
    """
    This function checks if the email is valid.
    """
    pattern = r"[a-z0-9!#$%&'\"*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'\"*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}"
    match = re.match(pattern, email)

    if match:
        return 'True'
    else:
        return 'False'


def validate_password(password):
    """
    This function checks if the password is strong.
    """
    pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\@\$\!\%\*\?\&])[\S]{8,}"
    match = re.match(pattern, password)
    if match:
        return 'True'
    else:
        return 'False'


def replace_word(text, old_word, new_word):
    """
    This function replaces all occurrences of 'old_word' with 'new_word' in the given text.
    """
    pattern = rf"\b{old_word}\b"
    result = re.sub(pattern, new_word, text)
    return result

text = "Hello! My email is student123@gmail.com and my phone number is +359 888-123-456."
print(find_email(text))  # Expected Output: student123@gmail.com
text = """
Contact us at support@company.com or sales@business.net.
For urgent inquiries, call +1-555-678-9999 or +44 123 4567 890.
"""
print(extract_emails_and_phones(text))
# Expected Output: (['support@company.com', 'sales@business.net'], ['+1-555-678-9999', '+44 123 4567 890'])
print(validate_email("user@domain.com"))  # Expected Output: True
print(validate_email("invalid-email"))    # Expected Output: False
print(validate_password("Secure123!"))    # Expected Output: True
print(validate_password("weakpass"))      # Expected Output: False
text = "I love Python! Python is amazing!"
print(replace_word(text, "Python", "Java"))
# Expected Output: "I love Java! Java is amazing!"