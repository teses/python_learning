from morphy import MultiLang
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
english_proc = MultiLang(lang='en')
doc = english_proc(text)
for token in doc.tokens:
    print('%s --> %s' % (token.text, token.lemma))