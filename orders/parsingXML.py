from urllib.request import urlopen
from xml.etree import cElementTree as et
from orders.models import Order

url = 'http://test.lengow.io/orders-test.xml'

dom = et.parse(urlopen(url))
root = dom.getroot()

for node in root[1]:
    order = Order()
    for element in node:
        if element.tag =='marketplace' and element.tag != 'None':
            order.marketplace = element.text
        if element.tag == 'order_amount' and element.tag != 'None':
            order.amount = float(element.text)
        if element.tag == 'order_shipping' and element.tag != 'None':
            order.shipping = float(element.text)
        if element.tag == 'billing_address':
            for child in element:
                if child.tag == 'billing_address' and child.text != 'None':
                    order.address = child.text
                if child.tag == 'billing_lastname' and child.text != 'None':
                    order.last_name = child.text
                if child.tag == 'billing_city' and child.text != 'None':
                    order.city = child.text
    order.save()

