import re, copy
from time import time

BAD_WORDS = ['amin','fatemeh','armin']*10000


x = {
    'text': 'amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left amin and the is a pattern that amin is istself a armin and some times fatemeh is there too look at amin amin amin and there armin armin fatemeh to right and left',
    'title': 'a simple amin one'
}
l = [copy.deepcopy(x) for i in range(200)]
l_copy = copy.deepcopy(l)

def f(x):
  for bad_word in BAD_WORDS:
    x['text'] = re.sub(rf'\b{bad_word}\b', ' ', x['text'])
    x['title'] = re.sub(rf'\b{bad_word}\b', ' ', x['title'])
  return x



def remove_words(x):
  for uncommon_word in BAD_WORDS:
    with_space = ' ' + uncommon_word + ' '
  
    x['text'] = x['text'].replace(with_space, ' ')
  
    if x['text'].startswith(uncommon_word):
      x['text'] = x['text'].replace(uncommon_word, ' ', 1)

    if x['text'].endswith(uncommon_word):
      x['text'] = ' '.join(x['text'].rsplit(uncommon_word, 1))



    x['title'] = x['title'].replace(with_space, ' ')
  
    if x['title'].startswith(uncommon_word):
      x['title'] = x['title'].replace(uncommon_word, ' ', 1)

    if x['title'].endswith(uncommon_word):
      x['title'] = ' '.join(x['title'].rsplit(uncommon_word, 1))
  
  return x

# t = time()
# for item in l:
#     y = f(copy.deepcopy(x))
# print(time()-t)



# t = time()
# for item in l:
#     z = remove_words(copy.deepcopy(x))
# print(time()-t)


# ----------------------------------------------------------------------------------------------------

size = 1000
s = x['text']*size

s_copy = copy.deepcopy(s)
t = time()
for uncommon_word in BAD_WORDS:
  s_copy = s_copy.replace(uncommon_word, ' ')
print(time()-t)



s_copy = copy.deepcopy(s)
t = time()
regex = 'keyvan'
for uncommon_word in BAD_WORDS:
  regex = regex  + '|' + uncommon_word
s_copy = re.sub(regex, ' ', s_copy)
print(time()-t)




# ----------------------------------------------------------------------------------------------------
# s = '!amin is hey. and? ?! ?d! ? there are a lot.'
# s = re.sub('\\b\W+\\b', ' ', s)
# print(s)

# s = 'امین ma!n ارمین'
# s = re.sub('\W+', ' ', s)
# # s = re.search('\w+', s)
# print(s)




