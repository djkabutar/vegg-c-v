def rabin_karp_string_matching(string, pattern):
    if len(string) < len(pattern):
        return False
    else:
        hash_pattern = hash(pattern)
        hash_string = hash(string[:len(pattern)])
        if hash_pattern == hash_string:
            return True
        else:
            return False