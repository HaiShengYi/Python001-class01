import pandas

class SpidersPipeline:
    def process_item(self, item, spider):
        movies = pandas.DataFrame(item.values())
        movies.to_csv('./movie.csv', mode='a', encoding='utf-8', index=False, header=False)
        return item
