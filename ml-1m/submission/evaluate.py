from movies_for_user import *

rec_file = open('recommendations')
for r in rec_file.readlines():
    p,m = r.split(':')
    p = p[1:-2].split(',')
    movies_for_user(p,m)