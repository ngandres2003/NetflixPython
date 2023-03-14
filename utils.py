def most_genre(data):
    genre = list(map(lambda genre : genre['Genre'],data)) #Lista de genero de cada pelicula
    genre_count = set(genre) #Set donde de la lista pasada eliminanos duplicados
    dict_genre = {key:0 for key in genre_count} #Diccionario que tiene como llave cada genero
    for x in genre: #Ciclo que contara cuantas veces se repite cada genero
        if x in genre_count:
            dict_genre[x] += 1 #Se le va sumando en el valor del diccionario creado
    keys = []
    for x,y in dict_genre.items(): #Aqui vamos a dejar en blanco los generos que se repitan menos de 3 veces,evitando saturacion en la grafica
        if y > 5:
            keys.append(x)
        else:
            keys.append('')
    values = dict_genre.values() 
    return keys,values

def top_10(data): #Funcion para encontrar top 10 con mejor puntuacion
    imdb = list(map(lambda score : float(score['IMDB Score']),data)) #lista con los puntajes de imdb
    movies = list(map(lambda movie : movie['Title'],data)) #Lista de las peliculas
    dict_top10 = dict(zip(movies[-10:],imdb[-10:])) #Diccionario con las top 10 peliculas
    return dict_top10.keys(),dict_top10.values()
        
    

    

    