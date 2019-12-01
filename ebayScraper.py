import requests
import time
import os
import re
from bs4 import BeautifulSoup



view_item = 'https://api.ebay.com/buy/browse/v1/item/v1|333403365541|0'
# completed_items = 'http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findCompletedItems&SECURITY-APPNAME=APIKEY&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=iphone&categoryId=9355&aspectFilter(0).aspectName=Model&aspectFilter(0).aspectValueName(0)=Apple%20iPhone%20X&aspectFilter(0).aspectValueName(1)=Apple%20iPhone%20XS&aspectFilter(0).aspectValueName(2)=Apple%20iPhone%20XS%20Max&aspectFilter(0).aspectValueName(3)=Apple%20iPhone%2011&aspectFilter(0).aspectValueName(4)=Apple%20iPhone%2011%20Pro&aspectFilter(0).aspectValueName(5)=Apple%20iPhone%2011%20Pro%20Max&itemFilter(0).name=MaxPrice&itemFilter(0).value(0)=800.00&itemFilter(1).name=ListingType&itemFilter(1).value=FixedPrice&itemFilter(2).name=Condition&itemFilter(2).value(0)=1500&itemFilter(2).value(1)=2000&itemFilter(2).value(2)=2500&itemFilter(2).value(3)=3000&itemFilter(2).value(4)=4000&itemFilter(2).value(5)=6000&itemFilter(2).value(6)=7000&paginationInput.entriesPerPage=100&paginationInput.pageNumber=1&sortOrder=StartTimeNewest'
completed_items = 'http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findCompletedItems&SECURITY-APPNAME=APIKEY&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=&categoryId=%2011450&itemFilter(0).name=ListingType&itemFilter(0).value=FixedPrice&paginationInput.entriesPerPage=100&paginationInput.pageNumber=1&sortOrder=StartTimeNewest'
headers = {'Authorization':'Bearer v^1.1#i^1#p^3#I^3#f^0#r^0#t^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'}

r = requests.get(completed_items)
data = r.json()
number_of_pages = data['findCompletedItemsResponse'][0]['paginationOutput'][0]['totalPages'][0]
print('Number of Pages: '+number_of_pages)

with open('dataframe.csv','w') as dataframe:
        dataframe.write('item_number, item_title, payment_method, postal_code, shipping_method, sales_price, selling_state, best_offer, bin_available, start_time, end_time, listing_type, returns_accepted, condition, top_rated, seller, feedback_percentage, feedback_score, description\n')

count = 0

with open('dataframe.csv','a') as dataframe:
    for i in range (1,int(number_of_pages)):
        completed_items = 'http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findCompletedItems&SECURITY-APPNAME=APIKEY&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=&categoryId=%2011450&itemFilter(0).name=ListingType&itemFilter(0).value=FixedPrice&paginationInput.entriesPerPage=100&paginationInput.pageNumber='+str(i)+'&sortOrder=StartTimeNewest'
        r = requests.get(completed_items, headers=headers)
        data = r.json()

        for j in range (0,100):
            item_number = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['itemId'][0]
            item_title = str(data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['title'][0]).replace(",", "")
            item_title = item_title.replace('"', "")
            item_title = item_title.replace("'", "")
            try:
                payment_method = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['paymentMethod'][0]
            except:
                payment_method = 'NA'
            try:
                postal_code = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['postalCode'][0]
            except:
                postal_code = '00000'
            # location = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['location'][0]
            shipping_method = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['shippingInfo'][0]['shippingType'][0]
            sales_price = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['sellingStatus'][0]['convertedCurrentPrice'][0]['__value__']
            selling_state = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['sellingStatus'][0]['sellingState'][0]
            best_offer = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['listingInfo'][0]['bestOfferEnabled'][0]
            bin_available = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['listingInfo'][0]['buyItNowAvailable'][0]
            start_time = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['listingInfo'][0]['startTime'][0]
            end_time = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['listingInfo'][0]['endTime'][0]
            listing_type = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['listingInfo'][0]['listingType'][0]
            returns_accepted = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['returnsAccepted'][0]
            try:
                condition = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['condition'][0]['conditionId'][0]
            except:
                condition = 'NA'
            top_rated = data['findCompletedItemsResponse'][0]['searchResult'][0]['item'][j]['topRatedListing'][0]

            print(item_number)
            count += 1
            print('\033c')
            print(str(count) +" items | pages:  "+ str(i))

            view_item = 'https://www.ebay.com/itm/'+str(item_number)+'?_trksid=p2349526.m4383.l10137.c10&nordt=true&rt=nc&orig_cvip=true0'
            try:
                r = requests.get(view_item)
                soup = BeautifulSoup(r.text, 'html.parser')

                seller = soup.find(class_='mbg-nw').text

                feedback_percentage = soup.find(id='si-fb')
                feedback_percentage = re.sub("[^0-9.]", "", str(feedback_percentage))

                feedback_score = soup.find(class_='mbg-l')
                feedback_score = re.sub("[^0-9]", "", str(feedback_score.text))


                view_description = 'https://vi.vipr.ebaydesc.com/ws/eBayISAPI.dll?ViewItemDescV4&item='+str(item_number)
                r = requests.get(view_description)
                soup = BeautifulSoup(r.text, 'html.parser')

                print(view_description)

                description = soup.find(id='ds_div')
                description = len(description.text)

            except:
                print('excepted')
                time.sleep(1)
                seller = 'NA'
                feedback_percentage = 'NA'
                feedback_score = 'NA'
                description = 'NA'

            line = [item_number, item_title, payment_method, postal_code, shipping_method, sales_price, selling_state, best_offer, bin_available, start_time, end_time, listing_type, returns_accepted, condition, top_rated, seller, feedback_percentage, feedback_score, str(description)+'\n']
            dataframe.write(','.join(str(v) for v in line))