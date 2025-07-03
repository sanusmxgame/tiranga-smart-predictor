import hashlib

SECRET_KEY = "tirangaSecret"  # Replace with real secret if known

def decode_hash(hash_str):
    for number in range(0, 100):
        input_str = f"{number}:{SECRET_KEY}"
        hashed = hashlib.sha256(input_str.encode()).hexdigest()
        if hashed == hash_str:
            return {
                "decoded_number": number,
                "color": get_color(number)
            }
    return {
        "decoded_number": -1,
        "color": "Unknown"
    }

def get_color(number):
    mod = number % 3
    if mod == 0:
        return "Green"
    elif mod == 1:
        return "Red"
    else:
        return "Violet"
