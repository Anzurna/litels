from flask import Flask, render_template, url_for

app = Flask(__name__)


articles = [
    {
        "url": "https://meduza.io/feature/2021/05/11/nekonfliktnyy-student-kotoryy-osoznal-sebya-bogom-i-legalno-kupil-drobovik-chto-izvestno-o-napadenii-na-shkolu-v-kazani-i-o-samom-napadavshem",
        "title": "«Неконфликтный» студент, который осознал себя «богом» и легально купил дробовик. Что известно о нападении на школу в Казани — и о самом нападавшем"
    }, 
     {
        "url": "https://dtf.ru/life/681118-drevneyshie-zhiteli-rossii-kto-takie-finno-ugry-i-pochemu-vse-ih-zabyli",
        "title": "Древнейшие жители России: кто такие финно-угры и почему все их забыли"
    }, 
]


@app.route("/")
def main():
    return render_template('main.html', articles=articles)

if __name__ == "__main__":
    app.run(debug=True)