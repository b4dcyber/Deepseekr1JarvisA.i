import eel
from engine.chat import query_deepseek

eel.init("www")

@eel.expose
def get_response(prompt):
    return query_deepseek(prompt)

# Launch at localhost:8000 with UI
eel.start("index.html", mode=None, port=8000, block=True)


