import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    print(id)
    return f"{base_url}/items/{id}"


def MakeNewList():
    NewList = []
    newinfo = requests.get(new).json()
    for hits in newinfo['hits']:
        NewList.append({'Title': hits['title'], 'URL': hits['url'], 'Point': hits['points'],
                        'Author': hits['author'], 'Num_Comment': hits['num_comments'], 'ObjectID': hits['objectID']})
    return NewList


def MakePopList():
    PopList = []
    popinfo = requests.get(popular).json()
    for hits in popinfo['hits']:
        PopList.append({'Title': hits['title'], 'URL': hits['url'], 'Point': hits['points'],
                        'Author': hits['author'], 'Num_Comment': hits['num_comments'], 'ObjectID': hits['objectID']})
    return PopList


def MakeDetail(id):

    detail_info = requests.get(make_detail_url(id)).json()

    DetailList = {'Title': detail_info['title'], 'URL': detail_info['url'], 'Point': detail_info['points'],
                  'Author': detail_info['author'], 'Children': detail_info['children']}
    return DetailList


db = {}
app = Flask("DayNine")


@app.route('/')
def home():
    order_by = request.args.get('order_by', 'popular')
    if order_by not in db:
        if order_by == 'popular':
            ResultList = MakePopList()
        elif order_by == 'new':
            ResultList = MakeNewList()

        db[order_by] = ResultList
    ResultList = db[order_by]
    return render_template("index.html", order_by=order_by, ResultList=ResultList)


@app.route('/<id>')
def gotodetail(id):
    result = MakeDetail(id)
    return render_template("detail.html", result=result)


app.run(host="0.0.0.0", port='5000', debug=True)
