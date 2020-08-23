def yoda(update, context):
    """Convert a sentence from English to YodaSpeak"""
    message = update.message
    if not context.args:
        try:
            text = message.reply_to_message.text or message.reply_to_message.caption
            message.reply_text(text=translator(text))
        except AttributeError:
            message.reply_text(
                text="*Usage:* `/yoda {SENTENCE}`\n"
                     "*Example:* `/yoda It was good`\n"
                     "Reply with `/yoda` to a message to speak it in Yoddish.",
            )
            return
    else:
        sentence = ' '.join(context.args)
        if not sentence:
            message.reply_text(text=translator(sentence))
        else:
            message.reply_text(text="Invalid input, provided you have.")


def translator(text: str):
    if text[:3] == "The" or text[:1] == "A" or text[:2] == "An":
        space = 0
        place = 0
        userInputM = text
        for dummy in userInputM:
            if dummy == " ":
                space += 1
                userInputM = text[place:]
                continue
            elif space == 3:
                break
            else:
                place += 1
        if text[len(text) - 1] == "." or text[len(text) - 1] == "!" or text[
            len(text) - 1] == "?":
            text = text[:len(text) - 1]
        subject = text[:place + 2]
        rest = text[place + 2:]
        rest1 = rest[1]
        rest2 = rest1.upper()
        rest = rest2 + rest[2:]
    else:
        space = 0
        place = 0
        userInputM = text
        for dummy in userInputM:
            if dummy == " ":
                space += 1
                userInputM = text[place:]
                continue
            elif space == 2:
                break
            else:
                place += 1
        if text[len(text) - 1] == "." or text[len(text) - 1] == "!" or text[
            len(text) - 1] == "?":
            text = text[:len(text) - 1]
        subject = text[:place + 1]
        rest = text[place + 2:]
        rest1 = rest[0]
        rest2 = rest1.upper()
        rest = rest2 + rest[1:]
    return rest + ", " + subject.lower()
