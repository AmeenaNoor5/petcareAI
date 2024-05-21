import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    # Additional pet care responses
    response(long.R_CARE_DOG, ['how', 'take', 'care', 'dog'], required_words=['care', 'dog'])
    response(long.R_CARE_CAT, ['how', 'take', 'care', 'cat'], required_words=['care', 'cat'])
    response(long.R_SICK_DOG, ['signs', 'sick', 'dog'], required_words=['sick', 'dog'])
    response(long.R_SICK_CAT, ['signs', 'sick', 'cat'], required_words=['sick', 'cat'])
    response(long.R_FEED_DOG, ['what', 'feed', 'dog'], required_words=['feed', 'dog'])
    response(long.R_FEED_CAT, ['what', 'feed', 'cat'], required_words=['feed', 'cat'])
    response(long.R_TRAIN_DOG, ['train', 'dog'], required_words=['train', 'dog'])
    response(long.R_STOP_SCRATCHING_CAT, ['stop', 'cat', 'scratching'], required_words=['cat', 'scratching'])
    response(long.R_GROOM_DOG, ['how', 'groom', 'dog'], required_words=['groom', 'dog'])
    response(long.R_GROOM_CAT, ['how', 'groom', 'cat'], required_words=['groom', 'cat'])
    response(long.R_DIARRHEA_DOG, ['dog', 'diarrhea'], required_words=['dog', 'diarrhea'])
    response(long.R_COLD_CAT, ['cat', 'cold'], required_words=['cat', 'cold'])
    response(long.R_FRUITS_DOG, ['can', 'dog', 'eat', 'fruits'], required_words=['dog', 'eat', 'fruits'])
    response(long.R_CHOCOLATE_CAT, ['cat', 'eat', 'chocolate'], required_words=['cat', 'eat', 'chocolate'])
    response(long.R_BARKING_DOG, ['stop', 'dog', 'barking'], required_words=['dog', 'barking'])
    response(long.R_AGGRESSIVE_CAT, ['cat', 'aggressive'], required_words=['cat', 'aggressive'])
    response(long.R_SHED_DOG, ['dog', 'shed', 'lot'], required_words=['dog', 'shed'])
    response(long.R_BATHE_CAT, ['bathe', 'cat'], required_words=['bathe', 'cat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))