#!/usr/bin/env python
# coding: latin-1
import sys
import random
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature

archivo_gbk = sys.argv[1]
lista_file = sys.argv[2]
gbk = SeqIO.read(archivo_gbk, "genbank")

#funcion para leer el archivo 'lista_file' a una lista
def listar_tabla(arch):
    lista=[]
    tabla= open(arch)
    for line in tabla.xreadlines():
        col = line.split()
        lista.append(col)
    tabla.close()
    return lista
    
#acá se crea la lista:
lista_interes=listar_tabla(lista_file)

#generar colores para poner en las features
ro=[(a,0,0) for a in xrange(200,255)]
na=[(255,a,0) for a in xrange(100,255)]
am=[(255,a,0) for a in xrange(200,255)]
ve=[(0,255,a) for a in xrange(200,255)]
az=[(0,125,a) for a in xrange(150,255)]
vi=[(a,0,255) for a in xrange(100,255)]
random.shuffle(ro)
random.shuffle(na)
random.shuffle(am)
random.shuffle(ve)
random.shuffle(az)
random.shuffle(vi)
colores1=()
for i in range(len(ro)):
   A=tuple(map(str,ro.pop(0))),tuple(map(str,ve.pop(0))),tuple(map(str,am.pop(0))),tuple(map(str,vi.pop(0))),tuple(map(str,az.pop(0))),tuple(map(str,na.pop(0)))
    colores1=colores1+A
colores=list(colores1)

for feature in gbk.features:
    if feature.type=="CDS":
        if feature.qualifiers.get('locus_tag') in lista_interes:
            feature.qualifiers['colour']=' '.join(map(str,colores.pop(0)))

#imprime el gbk modificad
print gbk.format("gb")

