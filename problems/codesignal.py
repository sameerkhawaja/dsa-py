def count_matching_substrings(pattern, source):
    vowels = set("aeiouy")

    def is_matching(substring):
        for i in range(len(pattern)):
            if pattern[i] == "0" and substring[i] not in vowels:
                return False
            elif pattern[i] == "1" and substring[i] in vowels:
                return False
        return True

    count = 0
    l = 0

    # Initialize the sliding window
    window = source[: len(pattern)]

    for r in range(len(pattern) - 1, len(source)):
        window = window[1:] + source[r]

        if is_matching(window):
            count += 1

        l += 1

    return count


# Example usage:
pattern = "010"
source = "amazing"
result = count_matching_substrings(pattern, source)
print("Number of matching substrings:", result)
