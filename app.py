from flask import Flask, request, render_template_string

app = Flask(__name__)

codebook = {
    'A': 823, 'B': 652, 'C': 309, 'D': 498, 'E': 586,
    'F': 671, 'G': 214, 'H': 345, 'I': 910, 'J': 627,
    'K': 158, 'L': 392, 'M': 874, 'N': 763, 'O': 120,
    'P': 948, 'Q': 537, 'R': 316, 'S': 204, 'T': 189,
    'U': 240, 'V': 764, 'W': 932, 'X': 295, 'Y': 681,
    'Z': 850, '0': 614, '1': 278, '2': 923, '3': 740, '4': 453,
    '5': 369, '6': 109, '7': 431, '8': 592, '9': 847
}
reverse_codebook = {v: k for k, v in codebook.items()}

def encrypt(text):
    return ' '.join(str(codebook.get(c, c)) for c in text.upper())

def decrypt(code):
    return ''.join(reverse_codebook.get(int(c), '?') if c.isdigit() else c for c in code.split())

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Bot Şifreleme Sistemi</title>
</head>
<body>
    <h2>Komut Gir (/sifreleme veya /sifreçöz)</h2>
    <form method=\"POST\">
        <input type=\"text\" name=\"command\" style=\"width:300px;\">
        <input type=\"submit\" value=\"Gönder\">
    </form>
    {% if result %}
        <h3>Bot Cevabı:</h3>
        <p>{{ result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        command = request.form.get("command", "")
        if command.startswith("/sifreleme"):
            content = command[len("/sifreleme"):].strip()
            result = encrypt(content)
        elif command.startswith("/sifreçöz"):
            content = command[len("/sifreçöz"):].strip()
            result = decrypt(content)
        else:
            result = "❗ Bilinmeyen komut. Lütfen /sifreleme veya /sifreçöz komutunu kullanın."
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run()
