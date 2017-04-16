# -*- coding: utf-8 -*-
"""'Building, renovation' part of product categories dictionary.

Must hold subcategories of 'Building, renovation'
category in the form of python dictionary data type.

"""
building_renovation = {('building, renovation', 'строительство, ремонт'): {
    ('bathroom', 'ванная, туалет'): {
        ('basins, vanities', 'раковины, мебель'): {},
        ('baths', 'ванны'): {},
        ('mirrors', 'зеркала'): {},
        ('showers', 'душевые кабины'): {},
        ('taps', 'краны, смесители'): {},
        ('toilets', 'унитазы'): {},
        ('other', 'другое'): {},
    },
    ('building supplies', 'стройматериалы'): {
        ('fixing, fastening', 'крепежи'): {},
        ('panels, boards', 'панели, доски'): {},
        ('insulation', 'теплоизоляция'): {},
        ('roofing', 'кровля'): {},
        ('sealant, adhesives', 'герметики, клеи'): {},
        ('scaffolding, ladders', 'лестницы, подмостки'): {},
        ('timber', 'строительный лес'): {},
        ('other', 'другое'): {},
    },
    ('tiles, flooring', 'плитка, полы'): {
        ('carpet', 'ковролин'): {
        },
        ('floorboards', 'половые доски, панели'): {
            ('wood', 'дерево'): {},
            ('laminate', 'ламинат'): {},
        },
        ('vinyl', 'линолеум'): {},
        ('tiles, stone', 'плитка, камень'): {
            ('ceramic', 'керамика'): {},
            ('limestone', 'известняк'): {},
            ('marble', 'мрамор'): {},
            ('stone', 'камень'): {},
            ('travertine', 'травертин'): {},
            ('porcelain', 'фарфор, фаянс'): {},
            ('vinyl tiles', 'виниловая плитка'): {},
            ('other', 'другое'): {},
        },
        ('other', 'другое'): {},
    },
    ('doors, windows', 'двери, окна'): {
        ('doors', 'двери'): {},
        ('windows', 'окна'): {},
        ('other', 'другое'): {},
    },
    ('electrical, lighting', 'электричество, свет'): {
        ('cabling', 'кабели'): {},
        ('lights', 'освещение'): {
            ('exterior', 'наружное'): {},
            ('hanging', 'подвесное'): {},
            ('inset', 'встраиваемое'): {},
            ('wall', 'настенное'): {},
            ('other', 'другое'): {},
        },
        ('switches, sockets', 'выключатели, розетки'): {
            ('sockets, oultets', 'розетки'): {},
            ('switchboards', 'электрощиты'): {},
            ('switches', 'выключатели'): {},
            ('other', 'другое'): {},
        },
    },
    ('fixtures, fittings', 'отделочная арматура'): {
        ('handles, knobs', 'ручки'): {},
        ('locks, latches', 'замки, щеколды'): {},
        ('rails, railings', 'перила, поручни'): {},
        ('other', 'другое'): {},
    },
    ('heating, cooling', 'обогрев, охлаждение'): {
        ('air conditioning', 'кондиционеры'): {},
        ('fireplaces, stoves', 'камины, печи'): {},
        ('heating systems', 'отопительные системы'): {},
        ('other', 'другое'): {},
    },
    ('kitchen', 'кухни'): {
        ('complete kitchens', 'готовые кухни'): {},
        ('countertops, benches', 'столешницы'): {},
        ('cupboards, cabinets', 'буфеты, шкафы'): {},
        ('rangehoods', 'вытяжки'): {},
        ('sinks', 'мойки'): {},
        ('other', 'другое'): {},
    },
    ('painting, wallpaper', 'покраска, обои'): {
        ('brushes, rollers', 'кисти, валики'): {},
        ('paint', 'краски'): {
            ('exterior', 'наружное'): {},
            ('interior', 'внутреннее'): {},
            ('roof', 'крыша'): {},
            ('other', 'другое'): {},
        },
        ('wallpaper', 'обои'): {},
        ('other', 'другое'): {},
    },
    ('plumbing', 'водопровод'): {
        ('faucets, taps', 'краны, смесители'): {},
        ('pipe', 'трубы'): {},
        ('pipe fittings', 'фитинги'): {},
        ('tubing', 'трубопровод'): {},
        ('valves', 'вентили, клапаны'): {},
        ('pumps', 'насосы'): {},
        ('water cylinders, heaters', 'нагреватели воды, цилидры'): {},
        ('sewer plumbing, drainage', 'канализация, сток'): {},
        ('other', 'другое'): {},
    },
    ('tools', 'инструмент'): {
        ('air compressors', 'компрессоры'): {
        },
        ('air tools', 'пневмоинструмент'): {
            ('air nailers', 'гвоздолет'): {},
            ('impact wrenches', 'гайковерт'): {},
            ('staplers', 'степлер'): {},
            ('sanders', 'пескоструйка'): {},
            ('spray guns', 'пульверизаторы'): {},
            ('bulk lots', 'оптом'): {},
            ('other', 'другое'): {},
        },
        ('hand tools', 'ручной инструмент'): {
            ('drills', 'дрели'): {},
            ('files, chisels', 'напильники, стамески'): {},
            ('hammers', 'молотки'): {},
            ('knives, cutters', 'ножи, резаки'): {},
            ('levelling', 'выравнивание'): {},
            ('measuring', 'измерение'): {},
            ('planes', 'рубанки'): {},
            ('pliers', 'плоскогубцы'): {},
            ('saws', 'пилы'): {},
            ('screwdrivers', 'отвертки'): {},
            ('spanners, wrenches', 'гаечные ключи'): {},
            ('vices, clamps, presses', 'тиски, зажимы'): {},
            ('bulk lots', 'оптом'): {},
            ('other', 'другое'): {},
        },
        ('power tools', 'электроинструмент'): {
            ('drills, rotary hammer', 'дрели, перфораторы'): {},
            ('grinders', 'шлифмашины'): {},
            ('nail guns, staple guns', 'гвоздолеты, степлеры'): {},
            ('planers', 'рубанки'): {},
            ('routers', 'фрезы'): {},
            ('sanders', 'полировка'): {},
            ('saw blades', 'лезвия пил'): {},
            ('saws', 'пилы'): {},
            ('bulk lots', 'оптом'): {},
            ('other', 'другое'): {},
        },
        ('parts, accessories', 'запчасти, аксессуары'): {},
        ('supplies', 'расходные материалы'): {},
        ('tool sets', 'наборы инструментов'): {},
        ('other', 'другое'): {},
    },
    ('gas', 'газовое оборудование'): {},
    ('other', 'другое'): {},
}
}
