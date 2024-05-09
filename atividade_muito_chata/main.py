from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    x = 5
    resultado = " "
    while x != 100:
        if x < 100:
            x = x + 1
            if (x % 7 == 0):
                if (x % 5 != 0):
                    resultado += str(x)
    else:
        resultado += ", acabou"
    return render_template('index.html', resultado=resultado)


if __name__=='__main__':
    app.run(debug=True)