from pyleus.storm import SimpleBolt
from neo4j_py.models import Article, Actor


class DummyBolt(SimpleBolt):

    OUTPUT_FIELDS = ['sentence']

    def process_tuple(self, tup):
        actor_name, article_name = tup.values

        try:
            actor = Actor.nodes.get(name=actor_name)
        except Actor.DoesNotExist:
            actor = Actor(name=actor_name).save()

        try:
            article = Article.nodes.get(name=article_name)
        except Article.DoesNotExist:
            article = Article(name=article_name).save()
        actor.favorites.connect(article)

        new_sentence = "{0} likes \"{1}\"".format(actor.name, article.name)
        self.emit((new_sentence,), anchors=[tup])

if __name__ == '__main__':
    DummyBolt().run()
