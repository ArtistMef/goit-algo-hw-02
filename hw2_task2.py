from collections import deque

def is_palindrome(data):
    deque_text = deque(data)
    while len(deque_text) > 1:
        if deque_text.pop() != deque_text.popleft():
            return "Sorry, not a palindrome"
    return "Is palindrome"
     
def main():   
    text = input("Your text: ")
    text_str = ''.join(ch.lower() for ch in text if ch.isalpha())
    print(is_palindrome(text_str))

if __name__ == "__main__":
    main()