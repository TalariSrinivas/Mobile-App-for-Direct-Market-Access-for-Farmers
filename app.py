from flask import Flask,render_template

app = Flask(__name__)

Products=[
    {
        'Pid':1,
        'Farmer Name':'T Srinivas',
        'Fid':1,
        'Product Name':'Rice',
        'Quantity':100,
        'Price':100, 
        'Date':'25-09-2025',
        'Img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9cRTv_WmJZCBkCpPRim6aDvXFMNi3_O1EhQ&s'
        
    },
    {
        'Pid':2,
        'Farmer Name':'Md Azeez',
        'Fid':2,
        'Product Name':'Wheat',
        'Quantity':150,
        'Price':100, 
        'Date':'25-07-2025'
    },
    {
        'Pid':3,
        'Farmer Name':'T Srinivas',
        'Fid':1,
        'Product Name':'ground nuts',
        'Quantity':200,
        'Price':50, 
        'Date':'01-10-2025'
    },
    {
        'Pid':4,
        'Farmer Name':'Sk Saboor',
        'Fid':3,
        'Product Name':'millets',
        'Quantity':500,
        'Price':150, 
        'Date':'05-10-2025'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',products=Products)
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)