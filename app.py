from textblob import TextBlob
from flask import Flask,render_template,request,jsonify

#import nltk
#import ssl

#ssl._create_default_https_context = ssl._create_unverified_context
#nltk.download('brown')
#nltk.download('punkt_tab')
#nltk.download('averaged_perceptron_tagger_eng')


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('hello.html')


@app.route("/feedback", methods=['POST'])
def feedback():
    text = request.form['text']
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(sentiment.polarity)

    return render_template('hello.html', value=sentiment.polarity)


@app.route("/rest", methods=['POST'])
def restEndPoint():
    data = request.get_json()
    print(data.get('text'))

    return jsonify({"Value ": data.get('text')})



if __name__ == '__main__':
    app.run()
