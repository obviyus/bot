def text(update, context):
    """Generate text based on prompt"""
    message = update.message
    if not context.args:
        try:
            args = message.reply_to_message.text or message.reply_to_message.caption
            message.reply_text(text=context.bot_data["textgen_obj"].generate(prefix=args))
        except AttributeError:
            message.reply_text(
                text="*Usage:* `/text {PROMPT}`\n"
                     "*Example:* `/text how are you?`\n"
            )
            return
    else:
        sentence = ' '.join(context.args)
        if not sentence:
            message.reply_text(text=context.bot_data["textgen_obj"].generate())
        else:
            message.reply_text(text=context.bot_data["textgen_obj"].generate(prefix=sentence))