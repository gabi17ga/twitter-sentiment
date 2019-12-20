from get_access_token import get_access_token

import twitter

apiKey = "D5aNtWK60ldCwLTkawkkHji78"
apiSecrete = "6c0SPGKTmIaAnX0B9RuLyB9a1M214jja6GMRb6gl9iS9IYQfhz"

def citireDinFisier(fisier):
    lista = []
    with open (fisier, "r") as f:
        for line in f:
            line = line.strip()
            lista.append(line)
    return lista

neg = citireDinFisier("neg.txt")
poz = citireDinFisier("pozitive.txt")

consumer_key         = "D5aNtWK60ldCwLTkawkkHji78"
consumer_secret      = "6c0SPGKTmIaAnX0B9RuLyB9a1M214jja6GMRb6gl9iS9IYQfhz"
access_token_key     = "1264736048-uj2znkJ563pE4QTJZj9YmqndMpEqjmx1l9o5Elk"
access_token_secret  = "g2Fay7CXWcILFQEdPArLIDOGYv3qPAfl0lvh1dt9sQ5Lb"

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)
twitts = api.GetSearch("@British_Airways")

for t in twitts:
    print(t)