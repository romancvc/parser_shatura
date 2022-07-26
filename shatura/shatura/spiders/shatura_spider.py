#python 3
from shatura.items import ShaturaItem

import scrapy
from urllib.parse import urljoin


class PycoderSpider(scrapy.Spider):
    name = "shatura"
    start_urls = [
        'https://www.shatura.com/goods/groups/krovati/?PAGEN_1',
        'https://www.shatura.com/goods/groups/shkafy_stellazhi_polki/?PAGEN_1',
        'https://www.shatura.com/goods/groups/matrasy_odeyala_podushki/?PAGEN_1',
        'https://www.shatura.com/goods/groups/tumby/?PAGEN_1',
        'https://www.shatura.com/goods/groups/komody/?PAGEN_1',
        'https://www.shatura.com/goods/groups/gotovye_nabory/?PAGEN_1',
        'https://www.shatura.com/goods/groups/stoly_i_stulya/?PAGEN_1',
        'https://www.shatura.com/goods/groups/veshalki/?PAGEN_1',
        'https://www.shatura.com/goods/groups/zerkala/?PAGEN_1',
        'https://www.shatura.com/goods/groups/myagkaya_mebel/?PAGEN_1',
        'https://www.shatura.com/goods/groups/predmety_interera/?PAGEN_1',
        'https://www.shatura.com/sale/?PAGEN_1'

    ]
    cookies = {'BITRIX_SM_CITY_ID': 25257}

    visited_urls = []

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
            for post_link in response.xpath(
                    '//div[@class="product-tile__picture"]/a/@href').extract():
                url = urljoin(response.url, post_link)
                yield response.follow(url, cookies={'BITRIX_SM_CITY_ID': 25257}, callback=self.parse_post)
                # print(url)

            next_pages = response.xpath(
                '//li[contains(@class, "page-item") and'
                ' not(contains(@class, "active"))]/a/@href').extract()
            next_page = next_pages[-1]

            next_page_url = urljoin(response.url + '/', next_page)
            yield response.follow(next_page_url, cookies={'BITRIX_SM_CITY_ID': 25257}, callback=self.parse)

    def parse_post(self, response):
        item = ShaturaItem()

        url = response.url
        item['url'] = url

        title = response.xpath('//div[@class="card-single__description"]/h2/text()').extract()
        item['title'] = title

        code = response.xpath('//div[@class="card-single__merch-info"]/div/text()').get().replace('Код товара ', '').strip()
        item['code'] = code

        category = response.xpath('//li[@class="breadcrumb__item breadcrumb-item"]//span/text()').extract()
        item['category'] = category

        item['old_price']  = response.xpath('//div[@class="price-block__old"]/text()').get()

        item['price'] = response.xpath('//div[@class="price-block__current"]/text()').get()

        item['params'] = {}
        item['collections'] = {}
        item['style'] = {}
        item['sleep_size'] = {}
        item['color'] = {}
        item['view'] = {}
        item['up_color'] = {}
        item['fabric_type'] = {}
        item['lift'] = {}
        item['headboard'] = {}
        item['back_wall'] = {}
        item['decor'] = {}

        item['width'] = {}
        item['length'] = {}
        item['height'] = {}
        item['manufacturer'] = {}
        item['manuf_code'] = {}
        item['vlago_covers'] = {}
        item['filling'] = {}
        item['mechanism'] = {}
        item['type_polok'] = {}
        item['num_boxes'] = {}
        item['type_fasade'] = {}

        item['carcas'] = {}
        item['num_doors'] = {}
        item['coll_matrases'] = {}
        item['type_matrases'] = {}
        item['weight_matrases'] = {}
        item['sliding_table'] = {}
        item['guides'] = {}
        item['load_sleep'] = {}
        item['brand'] = {}
        item['rigidity'] = {}



        param_list = response.xpath('//div[contains(@class, "chars-table__row")]')
        for params in param_list:
            key = params.xpath('./div[1]/span/text()').get().replace('', '')
            value = "".join([p.get() for p in params.xpath('./div[2]//text()')])
            value = value.strip() if value else ""
            if key == 'Коллекция':
                item['collections'][key] = value
            if 'Стиль' in key:
                item['style'][key] = value
            if key == 'Цвет':
                item['color'][key] = value
            if 'Вид' in key:
                item['view'][key] = value
            if 'Размер спального места' in key:
                item['sleep_size'][key] = value
            if 'Цвет обивки' in key:
                item['up_color'][key] = value
            if 'Тип ткани' in key:
                item['fabric_type'][key] = value
            if 'Подъемный механизм' in key:
                item['lift'][key] = value
            if 'Мягкое изголовье' in key:
                item['headboard'][key] = value
            if 'Обивка задней стенки' in key:
                item['back_wall'][key] = value
            if 'Тип декора для мягких кроватей' in key:
                item['decor'][key] = value
            if 'Глубина (Ширина)' in key:
                item['width'][key] = value
            if 'Длина' in key:
                item['length'][key] = value
            if 'Высота' in key:
                item['height'][key] = value
            if 'Производитель' in key:
                item['manufacturer'][key] = value
            if 'Производственный код' in key:
                item['manuf_code'][key] = value
            if 'Влагостойкость чехла' in key:
                item['vlago_covers'][key] = value
            if 'Наполнение' in key:
                item['filling'][key] = value
            if 'Механизм трансформации' in key:
                item['mechanism'][key] = value
            if 'Тип полок' in key:
                item['type_polok'][key] = value
            if 'Количество ящиков' in key:
                item['num_boxes'][key] = value
            if 'Тип фасада' in key:
                item['type_fasade'][key] = value
            if 'Каркас' in key:
                item['carcas'][key] = value
            if 'Количество дверей' in key:
                item['num_doors'][key] = value
            if 'Коллекция матрасов' in key:
                item['coll_matrases'][key] = value
            if 'Тип матраса' in key:
                item['type_matrases'][key] = value
            if 'Вес матраса' in key:
                item['weight_matrases'][key] = value
            if 'Жесткость матрасов' in key:
                item['rigidity'][key] = value
            if 'Стол раздвижной' in key:
                item['sliding_table'][key] = value
            if 'Направляющие' in key:
                item['guides'][key] = value
            if 'Нагрузка' in key:
                item['load_sleep'][key] = value
            if 'Бренд' in key:
                item['brand'][key] = value

            item['params'][key] = value

        description = response.xpath('//div[@class="block-content coupleСolumns"]').get().replace('', '').strip()
        item['description'] = description

        #item['images'] = response.xpath('//img[@class="gallery__big-img"]/@src').extract()

        main_image_urls = response.xpath('//img[@class="gallery__big-img"]/@src').extract()
        item['image_urls'] = [main_image_urls, ]


        yield item

        #for post_link in response.xpath(
        #       '//div[@class="product-tile__picture"]/a/@href').extract():
        #   url = urljoin(response.url, post_link)
        #   print(url)