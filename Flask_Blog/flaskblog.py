# save this as app.py
from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

schueKollektion = [
    {
        'productName': 'Product 1',
        'imageLink': '//cdn.shoepassion.de/catalog/product/3/5/3503_0645_cognac_br-br_milano-05.jpg',
        'price': '250€'
    },
    {
        'productName': 'Product 2',
        'imageLink': '//cdn.shoepassion.de/color_swatches/hd/swatch/hd_4331-0616_1052.jpg',
        'price': '300€'
    }
]
guertelKollektion = [
    {
        'productName': 'Product 1',
        'imageLink': '//cdn.shoepassion.de/catalog/product/g/7/g735_06_sm_cognac_br-105-03.jpg',
        'price': '50€'
    },
    {
        'productName': 'Product 2',
        'imageLink': '//cdn.shoepassion.de/catalog/product/g/_/g_735_00_sm_100_bordo_br-dro-03.jpg',
        'price': '80€'
    }
]
schuhPflegeKollektion = [
    {
        'productName': 'Product 1',
        'imageLink': '//cdn.shoepassion.de/catalog/product/h/d/hd-shoepassion_z13-1.jpg',
        'price': '20€'
    },
    {
        'productName': 'Product 2',
        'imageLink': '//cdn.shoepassion.de/catalog/product/h/d/hd-burgolbuersten_ross1_1_1.jpg',
        'price': '30€'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/schuhe')
def schuhe():
    return render_template('schuhe.html', schueKollektion = schueKollektion)

@app.route('/guertel')
def guertel():
    return render_template('guertel.html', guertelKollektion = guertelKollektion)

@app.route('/schuhpflege')
def schuhpflege():
    return render_template('schuhpflege.html', schuhPflegeKollektion = schuhPflegeKollektion)

@app.route('/stores')
def stores():
    return render_template('stores.html')

@app.route('/werkstatt')
def werkstatt():
    return render_template('werkstatt.html')

@app.route('/ueberuns')
def ueberuns():
    return render_template('ueberuns.html')