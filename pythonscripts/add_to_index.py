index = []

def add_to_index(index,keyword,url):
    if not index:
        index.append([keyword])
        index[0].append([url])
    else:
        for sublist in index:
            if sublist[0] == keyword:
                i = index.index(sublist)
                index[i][1].append(url)
                return index
        i = len(index)
        index.append([keyword])
        index[i].append([url])
    return index


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print(index)
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]