# -*- coding: utf-8 -*-
"""'Food, meals' part of product categories dictionary.

Must hold subcategories of 'Food, meals'
category in the form of python dictionary data type.

"""
food_drinks = {
}
meals = {
    ('Europe', 'Европа'): {
        ('Central Europe', 'Центральная Европа'): {
            ('Austria', 'Австрия'): {},
            ('Bulgaria', 'Болгария'): {},
            ('Czech Republic', 'Чехия'): {},
            ('Germany', 'Германия'): {},
            ('Hungary', 'Венгрия'): {},
            ('Liechtenstein', 'Лихтенштейн'): {},
            ('Romania', 'Румыния'): {},
            ('Serbia', 'Сербия'): {},
            ('Slovakia', 'Словакия'): {},
            ('Slovenia', 'Словения'): {},
            ('Poland', 'Польша'): {},
            ('Moldova', 'Молдoвa'): {},

        },
        ('Eastern Europe', 'Восточная Европа'): {
            ('Belarus', 'Беларусь'): {},
            ('Russia', 'Россия'): {},
            ('Ukraine', 'Украина'): {},
            ('Caucasus', 'Кавказ'): {
                ('Armenia', 'Армения'): {},
                ('Azerbaijan', 'Азербайджан'): {},
                ('Georgia', 'Грузия'): {},
            },

        },
        ('Northern Europe', 'Северная Европа'): {

            ('Baltic states', 'Балтийские государства'): {
                ('Estonia', 'Эстония'): {},
                ('Latvia', 'Латвия'): {},
                ('Lithuania', 'Литва'): {},
            },

            ('British Isles', 'Британские острова'): {
                ('Ireland', 'Ирландия'): {},
                ('Great Britain', 'Великобритания'): {
                    ('England', 'Англия'): {},
                    ('Scotland', 'Шотландия'): {},
                    ('Wales', 'Уэльс'): {},
                },
            },


            ('Scandinavia', 'Скандинавия'): {
                ('Denmark', 'Дания'): {},
                ('Greenland', 'Гренландия'): {},
                ('Finland', 'Финляндия'): {},
                ('Iceland', 'Исландия'): {},
                ('Norway', 'Норвегия'): {},
                ('Sweden', 'Швеция'): {},
            },
        },
        ('Southern Europe', 'Южная Европа'): {
            ('Cyprus', 'Кипр'): {},
            ('Albania', 'Албания'): {},
            ('Bosnia and Herzegovina', 'Босния и Герцеговина', ): {},
            ('Croatia', 'Хорватия'): {},
            ('Greece', 'Греция'): {},
            ('Macedonia', 'Македония'): {},
            ('Montenegro', 'Черногория'): {},
            ('Italy', 'Италия'): {},
            ('Malta', 'Мальта'): {},
            ('Portugal', 'Португалия'): {},
            ('Spain', 'Испания'): {},
        },
        ('Western Europe', 'Западная Европа'): {
            ('France', 'Франция'): {},
            ('Belgium', 'Бельгия'): {},
            ('Netherlands', 'Нидерланды'): {},
            ('Luxembourg', 'Люксембург'): {},
            ('Switzerland', 'Швейцария'): {},
        },

    },
    ('Asia', 'Азия'): {
        ('Central Asia', 'Центральная Азия'): {
            ('Turkmenistan', 'Туркменистан'): {},
            ('Tajikistan', 'Таджикистан'): {},
            ('Kyrgyzstan', 'Кыргызтан'): {},
            ('Kazakhstan', 'Казахстан'): {},
            ('Uzbekistan', 'Узбекистан'): {},
            ('Afghanistan', 'Афганистан'): {},
        },
        ('East Asia', 'Восточная Азия'): {
            ('Japan', 'Япония'): {},
            ('Korea', 'Корея'): {},
            ('China', 'Китай'): {
                ('Anhui', 'Anhui'): {},
                ('Cantonese', 'Cantonese'): {},
                ('Fujian', 'Fujian'): {},
                ('Hunan', 'Hunan'): {},
                ('Jiangsu', 'Jiangsu'): {},
                ('Shandong', 'Shandong'): {},
                ('Sichuan', 'Sichuan'): {},
                ('Zhejiang', 'Zhejiang'): {},
            },
        },
        ('Southeast Asia', 'Юго-Восточная Азия'): {
            ('Brunei', 'Бруней'): {},
            ('Myanmar', 'Мьянма'): {},
            ('Cambodia', 'Камбоджа'): {},
            ('Indonesia', 'Индонезия'): {},
            ('Laos', 'Лаос'): {},
            ('Malaysia', 'Малайзия'): {},
            ('Philippines', 'Филиппины'): {},
            ('Singapore', 'Сингапур'): {},
            ('Thailand', 'Тайланд'): {},
            ('Vietnam', 'Вьетнам'): {},
        },
        ('South Asia', 'Южная Азия'): {
            ('Bangladesh', 'Бангладеш'): {},
            ('Bhutan', 'Бутан'): {},
            ('India', 'Индия'): {
                ('North', 'Север'): {
                    ('Awadh', 'Awadh'): {},
                    ('Punjab', 'Punjab'): {},
                    ('Uttar Pradesh', 'Uttar Pradesh'): {},
                    ('Rajasthan', 'Rajasthan'): {},
                    ('Mughlai cuisine', 'Mughlai cuisine'): {},
                    ('Bhojpur', 'Bhojpur'): {},
                    ('Bihar', 'Bihar'): {},
                    ('Kashmir', 'Kashmir'): {},
                },
                ('South', 'Юг'): {
                    ('Kerala', 'Kerala'): {},
                    ('Tamil', 'Tamil'): {},
                    ('Andhra', 'Andhra'): {},
                    ('Karnataka', 'Karnataka'): {},
                    ('Hyderabad', 'Hyderabad'): {},
                },

                ('East', 'Восток'): {
                    ('Bengal', 'Bengal'): {},
                    ('Jharkhand', 'Jharkhand'): {},
                    ('Odia', 'Odia'): {},
                },

                ('North East', 'Северо-восток'): {
                    ('Sikkim', 'Sikkim'): {},
                    ('Assam', 'Assam'): {},
                    ('Thal', 'Thal'): {},
                    ('Tripur', 'Tripur'): {},
                    ('Naga', 'Naga'): {},
                },
                ('West', 'Запад'): {
                    ('Goa', 'Goa'): {},
                    ('Gujarat', 'Gujarat'): {},
                    ('Maharashtra', 'Maharashtra'): {},
                    ('Malvan', 'Malvan'): {},
                    ('Parsi', 'Parsi'): {},
                    ('Rajasthan', 'Rajasthan'): {},
                },
            },
            ('Maldives', 'Малдивы'): {},
            ('Nepal', 'Непал'): {},
            ('Pakistan', ): {
                ('Baloch', 'Baloch'): {},
                ('Kashmir', 'Kashmir'): {},
                ('Pashtun', 'Pashtun'): {},
                ('Muhajir', 'Muhajir'): {},
                ('Punjab', 'Punjab'): {},
                ('Lahor', 'Lahor'): {},
                ('Mughlai', 'Mughlai'): {},
                ('Sindh', 'Sindh'): {},
            },
            ('Sri Lanka', ): {},
        },
    },
    ('Middle East', 'Средний Восток'): {
        ('Bahrain', 'Бахрейн'): {},
        ('Iran', 'Иран'): {},
        ('Iraq', 'Ирак'): {},
        ('Israel', 'Израиль'): {},
        ('Jordan', 'Иордания'): {},
        ('Lebanon', 'Ливан'): {},
        ('Syria', 'Сирия'): {},
        ('Kuwait', 'Кувейт'): {},
        ('Oman', 'Оман'): {},
        ('Qatar', 'Катар'): {},
        ('Saudi Arabia', 'Саудовская Аравия'): {},
        ('United Arab Emirates', 'Объединённые Арабские Эмираты'): {},
        ('Turkey', 'Турция'): {},
        ('Yemen', 'Йемен'): {},
    },
    ('Africa', 'Африка'): {
        ('Central Africa', 'Центральная Африка'): {
            ('Cameroon', 'Камерун'): {},
            ('Congo', 'Конго'): {},
            ('Central African Republic', 'Центральноафриканская Республика'): {},
        },
        ('East Africa', 'Восточная Африка'): {
            ('Burundi', 'Бурунди'): {},
            ('Kenya', 'Кения'): {},
            ('Tanzania', 'Танзания'): {},
            ('Uganda', 'Уганда'): {},
            ('Eritrea', 'Эритрея'): {},
            ('Ethiopia', 'Эфиопия'): {},
            ('Somali', 'Сомали'): {},
        },
        ('North Africa', 'Северная Африка'): {
            ('Algeria', 'Алжир'): {},
            ('Egypt', 'Египет'): {},
            ('Libya', 'Ливия'): {},
            ('Morocca', 'Марокко'): {},
            ('Sudan', 'Судан'): {},
            ('Tunisia', 'Тунис'): {},
        },
        ('South Africa', 'Южная Африка'): {
            ('Botswana', 'Ботсвана'): {},
            ('Madagascar', 'Мадагаскар'): {},
            ('Namibia', 'Намибия'): {},
            ('South Africa', 'ЮАР'): {},
            ('Zimbabwe', 'Зимбабвe'): {},
        },
        ('West Africa', 'Западная Африка'): {
            ('Burkina Faso', 'Буркина Фасо'): {},
            ('Ghana', 'Гана'): {},
            ("Côte d'Ivoire", 'Берег Слоновой Кости'): {},
            ('Nigeria', 'Нигерия'): {},
            ('Sierra Leone', 'Сьерра-Леоне'): {},
            ('Senegal', 'Синегал'): {},
        },
    },
    ('Americas', 'Американский континент'): {
        ('North America', 'Северная Америка'): {
            ('Canada', 'Канада'): {},
            ('USA', 'США'): {},
            ('Mexico', 'Мексика'): {},
        },
        ('South America', 'Южная Америка'): {
            ('Argentina', 'Аргентина'): {},
            ('Brazil', 'Бразилия'): {},
            ('Chile', 'Чили'): {},
            ('Colombia', 'Колумбия'): {},
            ('Ecuador', 'Эквадор'): {},
            ('Paraguay', 'Парагвай'): {},
            ('Peru', 'Перу'): {},
            ('Uruguay', 'Уругвай'): {},
            ('Venezuela', 'Венесуэла'): {},
        },
        ('Central America', 'Центральная Америка'): {
            ('Belize', 'Белиз'): {},
            ('Costa Rica', 'Коста-Рика'): {},
            ('El Salvador', 'Эль-Сальвадор'): {},
            ('Guatemala', 'Гватемала'): {},
            ('Honduras', 'Гондурас'): {},
            ('Nicaragua', 'Никарагуа'): {},
            ('Panama', 'Панама'): {},
        },
        ('Caribbean', 'Карибы'): {},
    },
    ('Australia, Oceania', 'Австралия, Океания'): {
        ('Australia', 'Австралия'): {},
        ('Cook Islands', 'Острова Кука'): {},
        ('Easter Island', 'Остров Пасхи'): {},
        ('Fiji', 'Фиджи'): {},
        ('Hawaii', 'Гавайи'): {},
        ('Mariana Islands', 'Марианские Острова'): {},
        ('New Zealand', 'Новая Зеландия'): {},
        ('Niue', 'Ниуэ'): {},
        ('Palau', 'Палау'): {},
        ('Samoa', 'Самоа'): {},
        ('Solomon Islands', 'Соломоновы Острова'): {},
        ('Tonga', 'Тонга'): {},
        ('Tuvalu', 'Острова Тувалу'): {},
        ('Vanuatu', 'Вануату'): {},
    },
    ('Local cuisine', 'Местная кухня'): {},
}
food_meals = {('food, meals', 'продукты, блюда'): {
    ('food, drinks', 'продукты, напитки'): food_drinks,
    ('meals', 'блюда'): meals,
}
}
