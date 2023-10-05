import pyttsx3
from pydub import AudioSegment
import objc
from pypdf import PdfReader
from pydub.generators import say

text = "Hello, how are you?"
audio = say(text)
audio.export("output.mp3", format="mp3")

pdfreader = PdfReader("flask-intro.pdf")
#speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
  text = pdfreader.pages[page_num].extract_text()
  clean_text = text.strip().replace('\n', '')
  print(clean_text)

# speaker.save_to_file(clean_text, 'story.mp3')
# speaker.runAndWait()

# speaker.stop()
