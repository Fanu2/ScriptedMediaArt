def translate_to_yoda_speak(sentence):
    words = sentence.split()
    if len(words) < 3:
        return sentence  # Yoda-speak requires at least 3 words to make sense

    yoda_sentence = []

    # Split the sentence into three parts
    num_parts = 3
    parts = [words[i::num_parts] for i in range(num_parts)]

    # Rearrange the parts
    rearranged_parts = [parts[2], parts[0], parts[1]]

    for part in rearranged_parts:
        yoda_sentence.extend(part)

    # Capitalize the first word and add a period at the end
    yoda_sentence[0] = yoda_sentence[0].capitalize()
    yoda_sentence = ' '.join(yoda_sentence) + '.'

    return yoda_sentence

if __name__ == "__main__":
    sentence = input("Enter a sentence to translate to Yoda-speak: ")
    print(translate_to_yoda_speak(sentence))
