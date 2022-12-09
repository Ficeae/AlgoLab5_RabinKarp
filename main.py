def read_input_file():
    input_data = open('input.txt')
    pattern_in = input_data.readline()[:-1]
    text_in = input_data.readline()[:-1]
    prime_num = int(input_data.readline())
    alphabet_character_num = int(input_data.readline())
    return pattern_in, text_in, prime_num, alphabet_character_num


def rabin_karp(pattern, txt, prime_n, a_size):
    pattern_length = len(pattern)
    txt_length = len(txt)
    pattern_hash = 0
    txt_hash = 0
    pat_pos = 0
    q_hash = pow(a_size, pattern_length - 1) % prime_n

    for i in range(pattern_length):
        pattern_hash = (a_size * pattern_hash + ord(pattern[i])) % prime_n
        txt_hash = (a_size * txt_hash + ord(txt[i])) % prime_n

    for i in range(txt_length - pattern_length + 1):
        if pattern_hash == txt_hash:
            for pat_pos in range(pattern_length):
                if txt[i + pat_pos] != pattern[pat_pos]:
                    break
                else:
                    pat_pos += 1

            if pat_pos == pattern_length:
                print("Found at position: " + str(i + 1))

        if i < txt_length - pattern_length:
            txt_hash = (txt_hash - ord(txt[i]) * q_hash) % prime_n
            txt_hash = (txt_hash * a_size + ord(txt[i + pattern_length])) % prime_n


if __name__ == '__main__':
    searched_pattern, targeted_text, prime_number, alphabet = read_input_file()
    rabin_karp(searched_pattern, targeted_text, prime_number, alphabet)
