# -*- coding: utf-8 -*-
import scrapy
import datetime
import re

class BaijiaSpider(scrapy.Spider):
    name = "baijia"
    allowed_domains = ["baijia.baidu.com"]
    start_urls = ['http://baijia.baidu.com/']

    def parse(self, response):
        feeds = response.xpath('//div[@class="feeds-item hasImg"]')
        for feed in feeds:
            # print(feed)
            article_text = feed.xpath('./h3/a/text()').extract()
            article_url = feed.xpath('./h3/a/@href').extract()
            feed_author = feed.xpath('./div[@class="feeds-item-info"]/a[@ class="feeds-item-author"]/text()').extract()
            author_homepage = feed.xpath('./div[@class="feeds-item-info"]/a[@ class="feeds-item-author"]/@href').extract()
            datet = feed.xpath('./div[@class="feeds-item-info"]//span[@class="tm"]/text()').extract()
            if '1' in str(datet):
                datet = datetime.date.today().strftime('%m-%d')
            count = feed.xpath('./div[@class="feeds-item-info"]//span[@class="count"]/text()').extract()
            datetimes =  datetime.datetime.now() .strftime('%Y-%m-%d %H:%M')
            # if '万' in count:
            #     g = re.search(r'\d+', count)
            #
            #     count=int(g.group(1)) *10000
            # else:
            #     g = re.search(r'\d+',str(count))
            #     count = g.group(1)
            yield {'article_text': article_text,
                   'article_url': article_url,
                   'feed_author': feed_author,
                   'author_homepage': author_homepage,
                   'datet': datet,
                   'count': count,
                   'datetimes': datetimes
                }
        #
        # article_text = response.xpath('//div[@class="feeds-item hasImg"]/h3/a/text()').extract()
        # article_url = response.xpath('//div[@class="feeds-item hasImg"]/h3/a/@href').extract()
        # feed_author = response.xpath('//div[@class="feeds-item hasImg"]/div[@class="feeds-item-info"]/a[@ class="feeds-item-author"]/text()').extract()
        # author_homepage = response.xpath('//div[@class="feeds-item hasImg"]/div[@class="feeds-item-info"]/a[@ class="feeds-item-author"]/@href').extract()
        # datet = response.xpath('//div[@class="feeds-item hasImg"]/div[@class="feeds-item-info"]//span[@class="tm"]/text()').extract()
        # if '1' in str(datet):
        #     datet = datetime.date.today().strftime('%m-%d')
        # count = response.xpath('//div[@class="feeds-item hasImg"]/div[@class="feeds-item-info"]//span[@class="count"]/text()').extract()
        # datetimes =  datetime.datetime.now() .strftime('%Y-%m-%d %H:%M')
        #
        # yield {'article_text': article_text,
        #        'article_url': article_url,
        #        'feed_author': feed_author,
        #        'author_homepage': author_homepage,
        #        'datet': datet,
        #        'count': count,
        #        'datetimes': datetimes
        #     }
