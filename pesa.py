
import urllib.request as urllib2
import pesapal


pesapal.consumer_key = 'F+tkb4PGqyDzcX62uzQxEKSKetHcNFUk'
pesapal.consumer_secret = '70QDOJKe6tqKoVcHxy/Nnz5l9yw='
pesapal.testing = False


### post a direct order

post_params = {
  'oauth_callback': 'https://791a-102-69-228-142.ngrok.io/api/v1/testing/'
}
request_data = {
  'Amount': '100',
  'Description': 'E-book purchase',
  'Type': 'MERCHANT',
  'Reference': 'williamotieno',
  'PhoneNumber': '0719383956'
}
# build url to redirect user to confirm payment
url = pesapal.postDirectOrder(post_params, request_data)


### get order status

post_params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': '000'
}
url = pesapal.queryPaymentStatus(post_params)
response = urllib2.urlopen(url)
print(response.read())


### get order status by ref

post_params = {
  'pesapal_merchant_reference': '000'
}
url = pesapal.queryPaymentStatusByMerchantRef(post_params)
response = urllib2.urlopen(url)
print(response.read())


### get detailed order status

post_params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': '000'
}
url = pesapal.queryPaymentDetails(post_params)
response = urllib2.urlopen(url)
print(response.read())

