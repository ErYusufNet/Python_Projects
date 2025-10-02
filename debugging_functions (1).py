



def sum_of_squares(number1, number2):
    square = number1 ** 2
    square2 = number2 ** 2
    sum_of_squares = square + square2
    return sum_of_squares






def caps_lock(input_string):
    block_letter_string = ''
    for char in input_string:
        if char.isalpha():
            block_letter_string += char.upper()
        else:
            block_letter_string += char
    return block_letter_string



def rock_paper_scissors_helper(opposition_choice):

    if opposition_choice == "rock":
        return "paper"
    elif opposition_choice == "paper":
        return 'scissors'
    elif opposition_choice == "scissors":
        return 'rock'
    else:
            return 'Invalid choice'



def save_list_of_strings_as_txt(list, filename):
   with open(filename, 'w') as file:
       for string in list:
           file.write(string + '\n')





def price_calculator(price, base_currency, target_currency):
    import requests
    currency_url =  'https://www.frankfurter.app'
    response = requests.get(f'{currency_url}/latest',
                            params={"from": base_currency, "to": target_currency})
    rates = response.json()['rates']
    exchange_rate = rates.get(target_currency)
    if exchange_rate is None:
        return None
    return price * exchange_rate


