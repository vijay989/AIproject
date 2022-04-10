from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import zomatopy
import json

import smtplib,ssl
import random
import re
from email_validator import validate_email, EmailNotValidError

#Global Variables
top10_restaurants = []
sender_email = ""
sender_email_pwd = ""

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
	
	def filterByPrice(self, price_range, restaurants):
		pricedRestaurants = []
		for restaurant in restaurants:
			if restaurant['restaurant']["average_cost_for_two"] >= price_range[0] and restaurant['restaurant']["average_cost_for_two"] <= price_range[1]:
				pricedRestaurants.append(restaurant)
				
		return pricedRestaurants
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"5c566f8d381ec448fe315935ed02b2f4"}
		
		loc = tracker.get_slot('location').lower()
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		
		'''
		if cuisine.startswith("chin") or cuisine.startswith("Chin"):
			cuisine = "Chinese"
		if cuisine.startswith("mexi") or cuisine.startswith("Mexi"):
			cuisine = "Mexican"
		if cuisine.startswith("ital") or cuisine.startswith("Ital"):
			cuisine = "Italian"
		if cuisine.startswith("amer") or cuisine.startswith("Amer"):
			cuisine = "American"
		if cuisine.startswith("south") or cuisine.startswith("South"):
			cuisine = "South Indian"
		if cuisine.startswith("north") or cuisine.startswith("North") or cuisine.startswith("indian") or cuisine.startswith("Indian"):
			cuisine = "North Indian"
		'''
		
		printstmt = "$$ User input -> location is : {} , cuisine is : {} and price is : {} $$.".format(loc,cuisine,price)
		
		# print("location is : {} and cuisine is :  ".format(loc,cuisine))
		
		response="";
		responseSlotSet = [];
		
		locations = ["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra","ajmer","aligarh","amravati","amritsar","asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bilaspur","bokarosteelcity","chandigarh","coimbatore","cuttack","dehradun","dhanbad","bhilai","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gwalior","gurgaon","guwahati","hamirpur","hubli","dharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kakinada","kannur","kanpur","kochi","kolhapur","kollam","kozhikode","kurnool","ludhiana","lucknow","madurai","malappuram","mathura","goa","mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","patna","pondicherry","puruliaprayagraj","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","shimla","siliguri","solapur","srinagar","surat","thiruvananthapuram","thrissur","tiruchirappalli","tiruppur","ujjain","bijapur","vadodara","varanasi","vasai-virarcity","vijayawada","visakhapatnam","vellore","warangal"]
		
		if loc not in locations:
			response = "We do not operate in that area yet. Kindly enter Tier-1 & Tier-2 city from the link : https://en.wikipedia.org/wiki/Classification_of_Indian_cities"
			responseSlotSet = []
			#dispatcher.utter_message(response)
			dispatcher.utter_message(printstmt + "\n" + response)
		else:
		
			min = 300 #default price range.
			max = 700 #default price range.
		
			if price == 'low':
				min = 0
				max = 300
			elif price == 'mid':
				min = 300
				max = 700
			elif price == 'high':
				min = 700
				max = 10000
			else:
				'''
				regex1 = re.compile('[<]')
				regex2 = re.compile('[>]')
				if(regex1.search(price) != None):
					price = price.split('<')[1]
					if price.isdigit():
						min = 0
						max = int(price)
				elif(regex2.search(price) != None):
					price = price.split('>')[1]
					if price.isdigit():
						min = int(price)
						max = 10000
				else:
					prices = [int(s) for s in price.split() if s.isdigit()]
					min = prices[0]
					max = prices[1]
				'''
				min = 300
				max = 700
			priceRange = "Min is : {} and Max is : {}".format(min,max)
			printstmt = printstmt +"\n"+ priceRange

			price_range = [min,max]
			
			
			zomato = zomatopy.initialize_app(config)			
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			cuisines_dict = {'american': 1, 'chinese': 25, 'mexican': 73, 'italian': 55, 'north indian': 50, 'south indian': 85}
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 1000)
			d = json.loads(results)
			response=""
			if d['results_found'] == 0:
				response= "no results"
				responseSlotSet = [SlotSet('restaurants','None')]
			else:
				pricedRestaurants = self.filterByPrice(price_range, d['restaurants'])
				
				response = "Top "+str(len(pricedRestaurants[:5]))+" Restaurants picks are :\n\n"
				
				for restaurant in pricedRestaurants[:5]:
					response = response + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"
				
				global top10_restaurants
				top10_restaurants = pricedRestaurants[:10]
				
			'''
			response = "In Else block."
			buttons = []
			response = printstmt+"\n"+response + "\nDo you want to recieve email for these restaurants?"
			buttons.append({"title": "Please enter your ", "payload": "yes"})
			buttons.append({"title": "No", "payload": "no"})
			dispatcher.utter_button_message(response,buttons)
			'''
			response = response + "\n\n"
			#dispatcher.utter_message(printstmt+"\n"+response)
			dispatcher.utter_message(response)
					
			responseSlotSet = []
		#responseSlotSet = []		
			
		# responseSlotSet = [AllSlotsReset()]
			
		#dispatcher.utter_message(printstmt+"-----"+response)
		
		return responseSlotSet

# -- deprecated action		
class ActionValidateLocations(Action):
	def name(self):
		return 'action_validate_locations'
		
	def run(self, dispatcher, tracker, domain):
		locations = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune","Agra","Ajmer","Aligarh","Amravati","Amritsar","Asansol","Aurangabad","Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar","Bikaner","Bilaspur","BokaroSteelCity","Chandigarh","Coimbatore","Cuttack","Dehradun","Dhanbad","Bhilai","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad","Gorakhpur","Gulbarga","Guntur","Gwalior","Gurgaon","Guwahati","Hamirpur","Hubli–Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur","Kakinada","Kannur","Kanpur","Kochi","Kolhapur","Kollam","Kozhikode","Kurnool","Ludhiana","Lucknow","Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut","Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Patna","Pondicherry","PuruliaPrayagraj","Raipur","Rajkot","Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Shimla","Siliguri","Solapur","Srinagar","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tiruppur","Ujjain","Bijapur","Vadodara","Varanasi","Vasai-VirarCity","Vijayawada","Visakhapatnam","Vellore","Warangal"]
		loc = tracker.get_slot('location')
		response=""
		
		if loc not in locations:
			response = "We do not operate in that area yet. Kindly enter Tier-1 & Tier-2 city from the link : https://en.wikipedia.org/wiki/Classification_of_Indian_cities"
		else:
			response = "Great."
			
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]
		
class ActionEmailRestaurants(Action):
	def name(self):
		return 'action_email_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		user_email_address = tracker.get_slot('email_address')
		
		
		
		try:
			# Validate.
			valid = validate_email(user_email_address)

			# Update with the normalized form.
			user_email_address = valid.email
			global top10_restaurants
			restaurant_count = len(top10_restaurants)
			#restaurants = ', '.join(map(str, top10_restaurants))
			#response="We got response for email {} from user.{}".format(user_email_address,restaurants)
			
			if restaurant_count > 0:		
				response_messages = ['Sent','Sent. Bon Appetit!']
				
				# sender credentials.
				global sender_email
				global sender_email_pwd
				from_email =sender_email
				from_pwd =sender_email_pwd
				
				'''
				
				# email message details.
				SUBJECT = "Recommened Cusine!"
				TEXT = "This message was sent with Python's smtplib."
				msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT);
				
				# smtp server details.
				s= smtplib.SMTP("smtp.gmail.com", 587)
				s.ehlo()
				s.starttls()
				
				# smtp server Authentication 
				s.login(from_email, from_pwd);
				
				# email sending.
				s.sendmail(from_email, user_email_address, msg);
				
				# smtp connection closing.
				s.quit();
				
				'''
				
				
				# Create message container - the correct MIME type is multipart/alternative.
				msg = MIMEMultipart('alternative')
				msg['Subject'] = "Top "+str(restaurant_count)+" restaurants picks from Foodie."
				msg['From'] = from_email
				msg['To'] = user_email_address
				
				text_email_body = "Hi \nHope you are doing good.\n"+"Here are top "+str(restaurant_count)+" restaurants picks from Foodie.\n"
				html_email_body = """<p>Hi</p><p>Hope you are doing good.</p><p>Here are top """+str(restaurant_count)+""" restaurants picks from Foodie.</p><div><ol>"""
				
				for restaurant in top10_restaurants:
					text_email_body = text_email_body + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + " with average cost for two Rs. " + str(restaurant['restaurant']['average_cost_for_two']) + "\n"
					# text_email_body = text_email_body + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + " with average cost for two Rs " + str(restaurant['restaurant']["average_cost_for_two"]) + "\n"
					html_email_body = html_email_body + """<li>"""+restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + " with average cost for two Rs " + str(restaurant['restaurant']["average_cost_for_two"]) + """</li>"""
				
				text_email_body = text_email_body + "\n\nRegards\n-Restaurant Chatbot : Foodie"
				html_email_body = html_email_body+"""</ol></div><br><br><p>Regards</p><br><p>Restaurant Chatbot : <b>Foodie</b></p>"""
				
				
				# Record the MIME types of both parts - text/plain and text/html.
				part1 = MIMEText(text_email_body, 'plain')
				part2 = MIMEText(html_email_body, 'html')

				# Attach parts into message container.
				# According to RFC 2046, the last part of a multipart message, in this case
				# the HTML message, is best and preferred.
				msg.attach(part1)
				msg.attach(part2)

				# Send the message via local SMTP server.
				s= smtplib.SMTP("smtp.gmail.com", 587)
				s.ehlo()
				s.starttls()
				
				# smtp server Authentication 
				s.login(from_email, from_pwd)
				
				# sendmail function takes 3 arguments: sender's address, recipient's address
				# and message to send - here it is sent as one string.
				s.sendmail(from_email, user_email_address, msg.as_string())
				s.quit()
				
				# So that we know that there is no data for email to send.
				top10_restaurants = []				
				
				dispatcher.utter_message(random.choice(response_messages))
			else:
				dispatcher.utter_message("$$No data$$\nPlease select the cuisine and location first.")
		except Exception as e:
			# print(str(e))
			dispatcher.utter_message("Not Valid Email. Kindly Try again.")
			#dispatcher.utter_button_template("utter_greet", buttons, tracker)
		return []

class ActionDefaultAskAffirmation(Action):
   """Asks for an affirmation of the intent if NLU threshold is not met."""

   def name(self):
       return "action_default_ask_affirmation"

   def __init__(self):
       self.intent_mappings = {"greet":"greet","restaurant_search":"restaurant_search","emailer":"emailer","affirm":"affirm","goodbye":"goodbye","emailer_deny":"emailer_deny","out_of_scope":"out_of_scope","stop":"stop"}
       # read the mapping from a csv and store it in a dictionary
#        with open('intent_mapping.csv', newline='', encoding='utf-8') as file:
#            csv_reader = csv.reader(file)
#            for row in csv_reader:
       #self.intent_mappings["Chinise"] = "Chinese"

   def run(self, dispatcher, tracker, domain):
       # get the most likely intent
       last_intent_name = tracker.latest_message['intent']['name']
       #print("========"+last_intent_name)
       # get the prompt for the intent
      
        # intent_prompt = self.intent_mappings[last_intent_name]
       intent_prompt = self.intent_mappings[last_intent_name]

       # Create the affirmation message and add two buttons to it.
       # Use '/<intent_name>' as payload to directly trigger '<intent_name>'
       # when the button is clicked.
       message = "Did you mean '{}'?".format(intent_prompt)
       buttons = [{'title': 'Yes',
                   'payload': '/{}'.format(last_intent_name)},
                  {'title': 'No',
                   'payload': '/out_of_scope'}]
       dispatcher.utter_message(message, buttons=buttons)

       return []		