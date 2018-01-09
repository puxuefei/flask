from flask import Flask,request,render_template
from sklearn.externals import joblib


clf = joblib.load('d:/model.pkl')
d = {0:'setosa',1:'versiclor',2:'virginica'}

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('text.html')

@app.route('/result', methods=['POST'])
def signin():
    '1111'
    # sepal_length = request.form['sepal_length']
    # sepal_width = request.form['sepal_width']
    # petal_length = request.form['petal_length']
    # petal_width = request.form['petal_width']
    keys = list(request.form.keys())
    x = [request.form[i] for i in keys]
    print(x)
    pre = clf.predict([x])
    result = d[pre[0]]
    return  render_template('result.html',result = result)

if __name__ == '__main__':
    app.run(debug=True)
