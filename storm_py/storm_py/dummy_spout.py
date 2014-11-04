import random
from pyleus.storm import Spout


class DummySpout(Spout):

    OUTPUT_FIELDS = ['user', 'article']

    def next_tuple(self):
        actions = (
            ('Mike', 'Wild life'),
            ('Boby', 'Wild life'),
            ('Jay', 'Another NGM article'),
            ('John', '42, the number'),
        )
        self.emit(random.choice(actions))

if __name__ == '__main__':
    DummySpout().run()
