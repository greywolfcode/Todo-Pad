import base64
def get_base_64_string(path):
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')
print(get_base_64_string(r"C:\Users\zrobi\Documents\Todo Pad\layout_editor\images/icon.png"))