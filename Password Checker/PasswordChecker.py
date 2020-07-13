import requests
import hashlib
import sys


def request_api_data(query_char):  # query_char is hashed version of the password.

    # Part of Hash output and we need not give the entire hash output for searching
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}, check the api and try again')
    return res


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_five)  # returns https response code
    #print(first_five, tail, response)
    return get_password_leak_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password')
        else:
            print(f'{password} wad NOT found. Please carry on.')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
