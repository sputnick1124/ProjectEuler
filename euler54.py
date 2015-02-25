from time import time
def scorer(hand):
    suits={'h','d','s','c'}
    values=['','','2','3','4','5','6','7','8','9','t','j','q','k','a']
    hand.sort(key=lambda x: values.index(x[0]))
    handsuit=[card[1] for card in hand]
    handvalue=[values.index(card[0]) for card in hand]
    if any(all(suit in card for card in handsuit) for suit in suits):
        if handvalue[0]==10 and handvalue[-1]==14:
            return 100000
        if handvalue==list(range(handvalue[0],handvalue[-1]+1)):
            return 90000+handvalue[-1]
        return 60000+handvalue[-1]*100+handvalue[-2]
    if handvalue==list(range(handvalue[0],handvalue[-1]+1)) or handvalue==[2,3,4,5,14]:
        return 50000+handvalue[-1]*100+handvalue[-2]
    hvs=set(handvalue)
    if len(hvs)<5:
        score=[handvalue.count(v) for v in hvs]
        if score.count(2)==1:
            if score.count(3):
                trip=[v for v in hvs if handvalue.count(v)==3][0]
                hvs.remove(trip)
                return 70000+trip*100+hvs.pop()
            pair=[v for v in hvs if handvalue.count(v)==2][0]
            hvs.remove(pair)
            return 20000+pair*100+max(hvs)
        elif score.count(2)==2:
            pairs=[v for v in hvs if handvalue.count(v)==2]
            return 30000+max(pairs)*100+min(pairs)
        elif score.count(3):
            trip=[v for v in hvs if handvalue.count(v)==3][0]
            hvs.remove(trip)
            return 40000+trip*100+max(hvs)
        else:
            quad=[v for v in hvs if handvalue.count(v)==4][0]
            hvs.remove(quad)
            return 80000+quad*100+hvs.pop
    return 10000+handvalue[-1]*10+handvalue[-2]

t1=time()
f=open('poker.txt')
pokerhands=f.read().lower().strip().split('\n')
f.close
deal=0
wins=0
for hand in pokerhands:
     pokerhands[deal]=hand.split()
     if scorer(pokerhands[deal][:5])>scorer(pokerhands[deal][5:]):
         wins+=1
     deal+=1
print(wins)
print(time()-t1)
