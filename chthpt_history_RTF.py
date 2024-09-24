def save_history_to_rtf(history, filename):
    # Start the RTF document
    rtf_content = r"{\rtf1\ansi\deff0"

    for entry in history:
        # Add user text (bold)
        rtf_content += r"\b " + entry["user"] + r"\b0\line\line"

        # Add assistant text (normal)
        rtf_content += entry["assistant"] + r"\line\line"

    # End the RTF document
    rtf_content += r"}"

    # Write the content to the file
    with open(filename, "w") as rtf_file:
        rtf_file.write(rtf_content)


# Example chat history
chat_history = [
    {"user": "User: What is AI?", "assistant": "Assistant: AI stands for Artificial Intelligence."},
    {"user": "User: How does it work?",
     "assistant": "Assistant: AI works by using algorithms and models to make decisions."},
    # Add more conversation pairs as needed
]

# Save the chat history to an RTF file
save_history_to_rtf(chat_history, "/home/jasvir/PycharmProjects/Imagemagic/chat_history.rtf")
