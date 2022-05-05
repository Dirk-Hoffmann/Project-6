from ast import Break
from audioop import reverse
import sys



def odds(hp_string):
    index = 0
    S_odd_indexes = []
    S_even_indexes = []
    for i in hp_string:
        if i == "h" or i == "H":
            if index%2 == 0:
                S_even_indexes.append(index)
            else: 
                S_odd_indexes.append(index)
        elif i == "p" or i == "P":
            None
        else:
            raise NameError("string does not consist  of only H and P")
        index+=1
    
    return S_odd_indexes

def evens(hp_string):
    index = 0
    S_odd_indexes = []
    S_even_indexes = []
    for i in hp_string:
        if i == "h" or i == "H":
            if index%2 == 0:
                S_even_indexes.append(index)
            else: 
                S_odd_indexes.append(index)
        elif i == "p" or i == "P":
            None
        else:
            raise NameError("string does not consist  of only H and P")
        index+=1
    
    return S_even_indexes

def matchings(hp_string):
    odd_indexes = odds(hp_string)
    rev_odd_indexes = odd_indexes[::-1]
    even_indexes = evens(hp_string)
    rev_even_indexes = even_indexes[::-1]
    it = 0
    even_odds = []
    odd_evens = []
    break_point = len(hp_string)/2
    for i in odd_indexes:
        if odd_indexes[it] < rev_even_indexes[it]:
            odd_evens.append((odd_indexes[it],rev_even_indexes[it]))
        it+=1
        if i >= break_point:
            break        
#    while odd_indexes[it] < break_point or it <= (len(odd_indexes)-1):
#        if odd_indexes[it] < rev_even_indexes[it]:
#            odd_evens.append((odd_indexes[it],rev_even_indexes[it]))
#        it+=1
        #print(odd_indexes, it, break_point, len(odd_indexes))
    it = 0
    while even_indexes[it] <= break_point:
        if even_indexes[it] < rev_odd_indexes[it]:
            even_odds.append((even_indexes[it],rev_odd_indexes[it]))
        it+=1
    if len(even_odds) > len(odd_evens):
        return even_odds
    else:
        return odd_evens

def makefold(hp_string):
    matches = matchings(hp_string)[::-1]
    left = len(hp_string)/2
    right = left+1
    it = 0
    out = ""
    #print(matches)
   # while left > 0 and right < len(hp_string):
    while len(out)+1 < len(hp_string):
        #print(out,len(out)+1, hp_string, len(hp_string))
        if it == 0:
            out = "s"+out
            left-=1
            while left - matches[it][0]>=0:
                out = "e"+out
                left -=1
            while matches[it][1] - right>=0:
                out = out+"w"
                right += 1
        elif it <= len(matches)-1:
            #these next two lines might be bugged idk
            ll = matches[it-1][0]-matches[it][0]-1
            rl = matches[it][1]-matches[it-1][1]-1
            if ll == 1:
                out = "ee"+out
                left -= 2
            else:
                temp_it = 0
                while ll - temp_it > ll/2+1:
                    out = "s" + out
                    left-=1
                    temp_it+=1
                out = "e"+out
                left-=1
                temp_it+=1
                while ll-temp_it > 0:
                    out = "n"+ out
                    left -=1 
                    temp_it += 1
            if rl == 1:
                out = out + "ww"
                right += 2
            else:
                temp_it = 0
                while (rl - temp_it) >  (rl)/2+1:
                    out = out+ "s"
                    right+=1
                    temp_it+=1
                out = out+"w"
                right+=1
                temp_it += 1
                while rl-temp_it > 0:
                    out =out+"n"
                    right +=1 
                    temp_it += 1
        else:
            if left > 0:
                out = "e"+out
                left -= 1
            if right < len(hp_string):     
                right += 1
                out = out + "w"
        it+=1
    #out = out[1::]
    return out

test= sys.argv[1]

print(test, makefold(test))



