from collections import defaultdict


def get_points(input_str):
    input_list = input_str.split("|")
    winners = set(" ".join(input_list[0].split()).split())
    numbers = " ".join(input_list[1].split()).split()

    result = 0
    for number in numbers:
        if number in winners:
            result = 1 if result == 0 else result * 2
    return result


def get_card_won(input_str):
    input_list = input_str.split("|")
    winners = set(" ".join(input_list[0].split()).split())
    numbers = " ".join(input_list[1].split()).split()

    result = 0
    for number in numbers:
        if number in winners:
            result += 1
    return result


def get_card_number(input_str):
    return int(input_str.split(" ")[-1])


def update_dictionary(index, counter, dictionary, copies):
    for i in range(1, counter + 1):
        dictionary[index + i] += copies
    return dictionary


def calculate_total_number_of_cards(dictionary):
    return sum(dictionary.values())


def get_cards_won(input):
    winners, card_numbers = [group.split() for group in input.split("|")]
    winners = set(winners)
    return sum(num in winners for num in card_numbers)


def main():
    card_dictionary = defaultdict(int)

    test = 0
    path = "./advent_of_code/test.txt" if test else "./advent_of_code/input.txt"

    with open(path, "r") as openfile:
        for line in openfile:
            line_split = line.split(":")
            cards_won = get_cards_won(line_split[1])

            card_number = get_card_number(line_split[0])

            # Add original card to dict
            card_dictionary[card_number] += 1

            # Process for each card in collection
            copies = card_dictionary[card_number]
            update_dictionary(card_number, cards_won, card_dictionary, copies)

    return calculate_total_number_of_cards(card_dictionary)


print(main())
