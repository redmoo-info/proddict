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
from prodsupport.proddict.antiques import antiques_collectibles
from prodsupport.proddict.art import art
from prodsupport.proddict.baby_kids import baby_kids
from prodsupport.proddict.clothing_accessories import clothing_accessories
from prodsupport.proddict.home_garden import home_garden
from prodsupport.proddict.sport import sport
from prodsupport.proddict.mobile_phones_devs import mobile_phones_devices
from prodsupport.proddict.books import books
from prodsupport.proddict.building_renovation import building_renovation
from prodsupport.proddict.business_industry import business_industry
from prodsupport.proddict.computers import computers
from prodsupport.proddict.craft import craft
from prodsupport.proddict.electronics import electronics
from prodsupport.proddict.video_games import video_games
from prodsupport.proddict.health_beauty import health_beauty
from prodsupport.proddict.musical_instruments import musical_instruments
from prodsupport.proddict.toys_models import toys_models
from prodsupport.proddict.pets import pets
from prodsupport.proddict.movies_music import movies_music
from prodsupport.proddict.watches import watches
from prodsupport.proddict.food_meals import food_meals
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
