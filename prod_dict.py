# -*- coding: utf-8 -*-
""" Collection of supporting material for product navigation """
# Change country references: "New Zealand, Russia" might be referenced here.
# at least in 'stamps' and 'movies' section.
# Change clothing size reference to the one of your country.
# correct some brands, like ('sylvania',): {},
#('auto, moto', 'авто, мото'): {},
#('jewelry, watches', 'часы, украшения'): {},
#('jobs', 'работа'): {},
#('real estate', 'недвижимость'): {},
#('renting, letting', 'аренда жилья'): {},
#('services', 'услуги, сервис'): {},
from antiques import antiques_collectibles
from art import art
from baby_kids import baby_kids
from clothing_accessories import clothing_accessories
from home_garden import home_garden
from sport import sport
from mobile_phones_devs import mobile_phones_devices
from books import books
from building_renovation import building_renovation
from business_industry import business_industry
from computers import computers
from craft import craft
from electronics import electronics
from video_games import video_games
from health_beauty import health_beauty
from musical_instruments import musical_instruments
from toys_models import toys_models
from pets import pets
from movies_music import movies_music
from watches import watches
from food_meals import food_meals
prod_dict = {}
prod_dict.update(antiques_collectibles)
prod_dict.update(art)
prod_dict.update(baby_kids)
prod_dict.update(clothing_accessories)
prod_dict.update(home_garden)
prod_dict.update(sport)
prod_dict.update(mobile_phones_devices)
prod_dict.update(books)
prod_dict.update(building_renovation)
prod_dict.update(business_industry)
prod_dict.update(computers)
prod_dict.update(craft)
prod_dict.update(electronics)
prod_dict.update(video_games)
prod_dict.update(health_beauty)
prod_dict.update(musical_instruments)
prod_dict.update(toys_models)
prod_dict.update(pets)
prod_dict.update(movies_music)
prod_dict.update(watches)
prod_dict.update(food_meals)
