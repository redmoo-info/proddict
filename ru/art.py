# -*- coding: utf-8 -*-
"""'Art' part of product categories dictionary.

Must hold subcategories of 'Art'
category in the form of python dictionary data type.

"""

medium = {
    ('acrilic', 'акрил'): {},
    ('oil', 'масло'): {},
    ('pastels', 'пастель'): {},
    ('pencil', 'карандаш'): {},
    ('watercolor', 'акварель'): {},
    ('other', 'другое'): {},
}
art_themes = {
    ('abstract', 'абстракция'): {},
    ('animals', 'животные'): {},
    ('cityscape', 'городской мотив'): {},
    ('fantasy, mistic', 'фантастика, мистика'): {},
    ('floral', 'цветочный, растительный'): {},
    ('landscape', 'пейзаж'): {},
    ('nudes', 'обнаженные'): {},
    ('people', 'люди'): {},
    ('portrait, figures', 'портреты, фигуры'): {},
    ('religious', 'религиозный мотив'): {},
    ('seascape', 'морской пейзаж'): {},
    ('still life', 'натюрморт'): {},
    ('other', 'другое'): {},
}
art = {('art', 'живопись, искусство'): {
    ('art supplies, equipment', 'принадлежности, расходные'): {
        ('brushes', 'кисти'): {},
        ('easels, drawing boards', 'мольберты, доски'): {},
        ('paints, varnishes', 'краски, лаки'): {},
        ('paper, canvas', 'бумага, холст'): {},
        ('other', 'другое'): {},
    },
    ('drawings', 'рисунок'): art_themes,
    ('paintings', 'картины'): art_themes,
    ('photographs', 'фотографии'): art_themes,
    ('prints', 'печатные картины'): art_themes,
    ('sculpture', 'скульптура'): {
    },
    ('other', 'другое'): {},
}
}
