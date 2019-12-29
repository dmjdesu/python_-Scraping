import MeCab

tagger = MeCab.Tagger()
tagger.parse('')

node = tagger.parseToNode('ぼくがもし、人生に絶望することがあったら父親を殺そうと思う。')

while node:
	print(node.surface, node.feature)
	node = node.next