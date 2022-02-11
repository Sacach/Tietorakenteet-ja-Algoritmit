# Python code to perform Dijkstra's algorithm
# in a non-directed graph
import time
import math
from collections import deque

INF = float('inf')

# We assume that nodes numbered from 1 to n

# class for edges in adjacency list
class WeightedEdgeNode:
    def __init__(self,nde,wght=0):
        self.node = nde
        self.weight = wght

# graph class for breadth-forst search 
class WeightedGraph:
    
    def __init__(self,nVerts):
        self.nVertices = nVerts
        self.adj_list = {}
        self.vertices = []
        
        for x in range(1,nVerts+1):
            self.adj_list[x] = []
            self.vertices.append(x)
            
        self.dist = {}
        for x in range(1,nVerts+1):
            self.dist[x] = INF
            
        self.pred = {}
        for x in range(1,nVerts+1):
            self.pred[x] = None

        
# adds edge (x,y)       
def add_edge(g,x,y,wght):   
    g.adj_list[x].append(WeightedEdgeNode(y,wght))
    g.adj_list[y].append(WeightedEdgeNode(x,wght))  

    
'''
   Dijkstra's algorithm:
   DIJKSTRA(G,w,s)
   for each vertex v in V
      d[v] = INF
      p[v] = NIL
   d[s] = 0
   S = EMPTY
   Q = V[G]
   while Q != EMPTY
         u =  EXTRACT-MIN(Q)
         S = S UNION {u}
         for each vertex v in Adj[u] do
            if d[v] > d[u] + w(u,v) then
               d[v] = d[u] + w(u,v)
               p[v] = u
'''

#yllä oleva koodi kopioitu kurssin koodimateriaaleista import time:a lukuun ottamatta

def dijkstra(g,s,k):
    #funktion runko kopioitu kurssin koodimateriaaleista
    for i in g.vertices:
        g.dist[i] = INF
        g.pred[i] = 0
    
    g.dist[s] = 0
    
    queue = [i for i in g.vertices]
    
    while len(queue) > 0:
        minval = INF
        u = 0
        for vert in queue:
            if g.dist[vert] < minval:
                minval = g.dist[vert]
                u = vert
        #algoritmiin muokattu try except rakenne, jotta 
        #voidaan käsitellä tilanteet, joissa reittiä ei ole
        try:
            #jos päätepiste ei ole viimeinen solmu, niin pysäytetään
            if u == k:
                return 1
            else:
                queue.remove(u)

        except ValueError:
            print("Reittiä ei ole")
            return -1

        for edge in g.adj_list[u]:
            v = edge.node
            #if lauseen sisältö muutettu kasaantuvan painon
            #sijaan säilyttämään keveimmän polun suurin paino
            if g.dist[v] > max(g.dist[u], edge.weight):
                g.dist[v] = max(g.dist[u], edge.weight)
                g.pred[v] = u

        # DEBUG INFO:
        # print(u, " processed, dist =  ",g.dist[u])
        
def print_path(g,u):
    #funktio kopioitu kurssin koodimateriaaleista
    if g.pred[u] != 0:
        print_path(g,g.pred[u])
    #tulostusta muokattu siten, että :-merkit tulostuvat
    #samalle pystyriville, jolloin tuloste on siistimpi
    if u < 10:
        print('  ', u,'   :  ',g.dist[u])
    elif u < 100:
        print('  ', u,'  :  ',g.dist[u])
    elif u < 1000:
        print('  ', u,' :  ',g.dist[u])
    else:
        print('  ', u,':  ',g.dist[u])
    

def avaa_tiedosto():
    #ikuisella silmukalla tehdään mahdolliseksi antaa syöte uudelleen,
    #jos käyttäjä syöttää tiedoston nimen, jota ei ole olemassa.
    while True:
        try:
            #kysytään syöte
            tiedosto = input("Anna tiedoston nimi: ")
            #yritetään avata tiedosto
            polku = open("graph_testdata\\{}.txt".format(tiedosto))
            #palautetaan avattu tiedosto funktiosta
            return polku
        #jos tiedostoa ei löydy, ilmoitetaan siitä
        #ja koodi palautuu silmukan alkuun
        except FileNotFoundError:
            print("Tiedostoa ei löydy")
            print("Yritä uudelleen")
    
def luo_graafi(data):
    #luodaan väliaikainen muuttuja, joka sisältää kaupunkien sekä yhteyksien määrän
    temp = data.readline().rstrip("\n").split(" ")
    #graafin alustus
    g = WeightedGraph(int(temp[0]))
    #otetaan muistiin kaupunkien välillä olevien yhteyksien määrä
    i = int(temp[1])
    #luodaan silmukka, joka loppuu, kun kaikki yhteydet on käyty läpi
    while i > 0:
        #luetaan tiedostoa rivi kerrallaan
        reitti = data.readline().rstrip("\n")
        #asetetaan rivillä olevat tiedot muuttujiin
        alku, loppu, paino = reitti.split(" ")
        #lisätään graafiin yhteys muuttujien tietojen mukaisesti 
        add_edge(g,int(alku), int(loppu), int(paino))
        #ei lisättyjen yhteyksien määrä vähenee yhdellä
        i = i - 1
    #luetaan tekstitiedoston viimeinen rivi,
    #joka on sen kaupungin numero, johon halutaan päästä
    kohde = int(data.readline().rstrip("\n"))
    #palautetaan funktiosta graafi sekä päätöskaupungin numero
    return g, kohde

def main():
    #avataan tiedosto
    Data = avaa_tiedosto()
    #start = time.time(), käytettiin aikakompleksisuuden selvittämiseen
    #luodaan graafi
    graafi, Kohde = luo_graafi(Data)
    #etsitään polku djikstran algoritmilla
    reitti = dijkstra(graafi,1,Kohde)
    #tulostus
    if reitti > 0:
        print("Reitti  :  Korkein ylitetty kohta kyseisen kaupungin kohdalla")
        #tulostetaan polku
        print_path(graafi,Kohde)
    #end = time.time(), käytettiin aikakompleksisuuden selvittämiseen
    #print(end - start), käytettiin aikakompleksisuuden selvittämiseen
    
if __name__ == "__main__":
    main()