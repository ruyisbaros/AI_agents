from langchain_core.tools import tool


@tool
def note_tool(note):
    """Saves a note to a local file.

    Args:
    note (str): The text note to save.
    """
    with open("notes.txt", 'a') as file:
        # Append the note to the file with a newline character
        file.write(note + "\n")
