from main.models import * 
import pandas as pd
import requests
import os
from urllib.request import urlretrieve
import math


file = os.getcwd() + '/scrape/data_main2.xlsx'


def createAll():
    i = 0
    delall()
    # createCategory()
    # createProducts()
    data = pd.read_excel(file)
    data['price'].fillna('0', inplace = True)
    for index, item in data.iterrows():
        name = item['name']
        price = str(item['price']).replace(' ', '').replace('.', '')
        if type(price) == str:
            price = int(price)
        else:
            if math.isnan(price):
                price = None
            else:
                price = int(str(price).replace(' ', ''))
        imgsrc = item['imgurl']
        img_ext = item['imgurl'][0].split('.')[-1]
        category = str(item['category']).strip()
        # try:
        image_file = requests.get(imgsrc).content
        file_name = 'static/images/products/' + str(index)+'.png'
        output = open(file_name, "wb")
        output.write(image_file)
        # urlretrieve(imgsrc, 'static/images/products/'+str(index)+'.png')
        img = file_name
        # except:
        #     print('error trying to load image')
        #     img = None
        cat = Category.objects.get_or_create(
            name = category
        )[0]
        p = Product(
            category = cat,
            name = name,
            price = price,
            imgsrc = img,
        )
        p.save()
        i += 1
        print('created', i, 'items')
    

if __name__ == "__main__":
    createAll()