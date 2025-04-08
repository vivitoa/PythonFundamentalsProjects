# Regex Project

This repository is part of the Python Fundamentals course at SoftUni and contains a project focused on learning and applying regular expressions (regex). The project includes several Python functions that demonstrate various regex operations, such as finding, validating, and extracting email addresses and phone numbers, as well as validating passwords and replacing words in text.

## Project Structure

The project consists of the following main components:

1. `find_email(text)`: Finds and returns an email address from the given text.
2. `extract_emails_and_phones(text)`: Finds and returns all email addresses and phone numbers from the given text.
3. `validate_email(email)`: Checks if the email is valid.
4. `validate_password(password)`: Checks if the password is strong.
5. `replace_word(text, old_word, new_word)`: Replaces all occurrences of `old_word` with `new_word` in the given text.

## Example Usage

Below are some examples demonstrating the usage of each function:

### Finding an Email Address

```python
text = "Hello! My email is student123@gmail.com and my phone number is +359 888-123-456."
print(find_email(text))  # Expected Output: student123@gmail.com
```

### Extracting Emails and Phone Numbers

```python
text = """
Contact us at support@company.com or sales@business.net.
For urgent inquiries, call +1-555-678-9999 or +44 123 4567 890.
"""
print(extract_emails_and_phones(text))
# Expected Output: (['support@company.com', 'sales@business.net'], ['+1-555-678-9999', '+44 123 4567 890'])
```

### Validating an Email Address

```python
print(validate_email("user@domain.com"))  # Expected Output: True
print(validate_email("invalid-email"))    # Expected Output: False
```

### Validating a Password

```python
print(validate_password("Secure123!"))    # Expected Output: True
print(validate_password("weakpass"))      # Expected Output: False
```

### Replacing Words in Text

```python
text = "I love Python! Python is amazing!"
print(replace_word(text, "Python", "Java"))
# Expected Output: "I love Java! Java is amazing!"
```

## Requirements

- Python 3.x
- `re` module (part of the Python Standard Library)

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/vivitoa/PythonFundamentalsProjects.git
```

2. Navigate to the project directory:

```bash
cd PythonFundamentalsProjects/Regex-Project
```

3. Run the Python script:

```bash
python regex_project.py
```

## Conclusion

This project provides a practical introduction to using regular expressions in Python. The functions included demonstrate common regex tasks and can be used as a reference for more complex regex operations in future projects.

## Acknowledgments

- SoftUni for providing the Python Fundamentals course and resources.

---

Feel free to explore and modify the code to enhance your understanding of regular expressions in Python!
