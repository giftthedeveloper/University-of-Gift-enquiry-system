import random

def random_bot_unknown_response():
    random_list = ["I dont understand what you're tryna say.\nplease can you rephrase that statement ?",
                   "please can you rephrase that statement ?",
                   "oops! It appears you wrote something i don't understand"]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
#print(random_bot_unknown_response())

