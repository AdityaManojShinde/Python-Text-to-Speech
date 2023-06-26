import pyttsx3

def text_to_speech(file_path):
    # Initialize pyttsx3
    engine = pyttsx3.init()

    # Load the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Set the properties for audio output
    engine.setProperty('rate', 120)  # Speed of speech
    engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)

    # Save audio to a file
    output_path = 'output.mp3'
    engine.save_to_file(text, output_path)

    # Play the audio
    engine.runAndWait()

    print(f"Audio saved to: {output_path}")


# Usage
text_file_path = 'text.txt'
text_to_speech(text_file_path)
