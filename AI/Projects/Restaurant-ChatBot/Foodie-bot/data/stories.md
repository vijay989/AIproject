## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "no"}
	- slot{"email_address": "no"}
    - action_email_restaurants
* affirm
    - utter_goodbye
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "goa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "akhileshdumca@gmail.com"}
    - slot{"email_address": "akhileshdumca@gmail.com"}
    - action_email_restaurants
* affirm
	- utter_goodbye
## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "goa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "akhileshdumca@gmail.com"}
    - slot{"email_address": "akhileshdumca@gmail.com"}
    - action_email_restaurants
* affirm
	- utter_goodbye
	
## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer{"email_address": "abc@gmail.com"}
    - slot{"email_address": "abc@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer{"email_address": "abc@def.com"}
    - slot{"email_address": "abc@def.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye
	
## complete_path_wo_initial_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye
## complete_path_wo_last_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
	
## mexican_delhi_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
	- utter_goodbye
## location_cuisine_combine_story
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## agra_italian_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Agra"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Agra"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## goa_chinese_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
* emailer{"email_address": "no"}
	- slot{"email_address": "no"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## american_delhi_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye
## interactive_story_1_wo_greets
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants

## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye
## happy_path_wo_initial_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye
## happy_path_wo_last_greet
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
## happy_path_wo_greets
* restaurant_search{"location": "Delhi","cuisine": "South Indian"}
    - slot{"location": "Delhi"}
	- slot{"cuisine": "South Indian"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
## delhi_italian_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## price_interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "location": "delhi"}
    - slot{"cuisine": "American"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer{"email_address": "abc.def@gmail.com"}
    - slot{"email_address": "abc.def@gmail.com"}
    - action_email_restaurants
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "delhi"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer{"email_address": "abc@gmail.com"}
    - slot{"email_address": "abc@gmail.com"}
    - action_email_restaurants
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "goa"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_ask_email
* emailer_deny
    - utter_goodbye

## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "goa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
## interactive_story_1
* restaurant_search{"cuisine": "Mexican", "location": "goa"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
	
## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer_deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer_deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer_deny
    - utter_goodbye

## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
	
## complete_path_wo_initial_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
## complete_path_wo_last_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
	
## mexican_delhi_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
## location_cuisine_combine_story
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye

## agra_italian_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Agra"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Agra"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye

## goa_chinese_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye

## american_delhi_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
## interactive_story_1_wo_greets
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye

## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
## happy_path_wo_initial_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
## happy_path_wo_last_greet
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
## happy_path_wo_greets
* restaurant_search{"location": "Delhi","cuisine": "South Indian"}
    - slot{"location": "Delhi"}
	- slot{"cuisine": "South Indian"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
## delhi_italian_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}	
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye

## price_interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
	- utter_ask_email
* emailer_deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer_deny
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* emailer{"email_address": "akhileshdumca@gmail.com"}
    - slot{"email_address": "akhileshdumca@gmail.com"}
    - utter_ask_location
* restaurant_search{"location": "nanded"}
    - slot{"location": "nanded"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer{"email_address": "akhilesh.dualumni@gmail.com"}
    - slot{"email_address": "akhilesh.dualumni@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* emailer{"email_address": "akhilesh.dualumni@gmail.com"}
    - slot{"email_address": "akhilesh.dualumni@gmail.com"}
    - action_email_restaurants
* affirm
    - utter_goodbye