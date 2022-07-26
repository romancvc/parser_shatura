import scrapy


class ShaturaItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    code = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    old_price = scrapy.Field()
    params = scrapy.Field()
    description = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()

    #Характеристики
    collections = scrapy.Field()
    style = scrapy.Field()
    sleep_size = scrapy.Field()
    color = scrapy.Field()
    view = scrapy.Field()
    up_color = scrapy.Field()
    fabric_type = scrapy.Field()
    lift = scrapy.Field()
    headboard = scrapy.Field()
    back_wall = scrapy.Field()
    decor = scrapy.Field()
    width = scrapy.Field()
    length = scrapy.Field()
    height = scrapy.Field()
    manufacturer = scrapy.Field()
    manuf_code = scrapy.Field()
    vlago_covers = scrapy.Field()
    filling = scrapy.Field()
    mechanism = scrapy.Field()
    type_polok = scrapy.Field()
    num_boxes = scrapy.Field()
    type_fasade = scrapy.Field()
    carcas = scrapy.Field()
    num_doors = scrapy.Field()
    coll_matrases = scrapy.Field()
    type_matrases = scrapy.Field()
    weight_matrases = scrapy.Field()
    sliding_table = scrapy.Field()
    guides = scrapy.Field()
    load_sleep = scrapy.Field()
    brand = scrapy.Field()
    rigidity = scrapy.Field()



    pass
