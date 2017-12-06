import mysql.connector as ms
import redis

print('enter % to execute all records into redis')
inp = str(input())

def createtokenized(r, hotel_id, review):
    words = set(filter(lambda word: len(word) > 3, review.split(' ')))
    for word in words:
        r.sadd(word, hotel_id)

rds = redis.StrictRedis()
pipe = rds.pipeline()

cnn = ms.connect(user='root', database='Hotels')
cursor = cnn.cursor()

if inp == '%':
   # print('right')
    query = ('SELECT hid_id, Positive_Review, Review_Total_Positive_Word_Counts'
         ' FROM reviews_review_entity WHERE hid_id LIKE {}'.format(inp))
else:
    raise ValueError('Input in wrong format.')

cursor.execute(query)
cnt = 0

for h_id, review, count in cursor:
    cnt += 1
    if count==0:
        continue
    # print('hotel:{} {}'.format(h_id, review[:20]))
    review = review.strip().lower()
    createtokenized(pipe, h_id, review)

    if cnt % 10000 == 0:
        print('Done %d' % cnt)
        pipe.execute()

pipe.execute()

