

import random
import time
# Put words here (._.)
start  =  ["Indigenous ", "Sustainable "]
middle = ["wine ", "dog "]
middle2 = ["food ", "beverage " ]
end = ["startup", "influencer campaign"]
while True:
    # Sleep for 100ms before running code ('o')
    time.sleep(0.1)
    # Generate sentence (O_O)
    a = random.choice(start)
    d = random.choice(end)
    b = random.choice(middle)
    c = random.choice(middle2)
    sentence = a + b + c + d
    print(sentence)
