from collections import Counter

def analyze_hashtags(publicaciones):

    todos_hashtags = []
    
    for post in publicaciones:
        palabras = post.split()
        
        for palabra in palabras:
            if palabra.startswith('#'):
                todos_hashtags.append(palabra)
                
    contador = Counter(todos_hashtags)
    
    trending = []
    for tag, freq in contador.most_common():
        if freq > 1:
            trending.append((tag, freq))
            

    total_unicos = len(contador)
    
    return {
        "trending_tags": trending,
        "total_unicos": total_unicos
    }