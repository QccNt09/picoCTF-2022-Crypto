
from math import gcd
def pollar(n):
    a = 2
    j = 2
    while True:
        a = pow(a,j,n)
        d = gcd(a-1,n)
        if(d >1 and d<n):
            return d
        j = j+1
    return "none"

n =  13650983611329317589670370711391090694988201856296599880208159117154408484599601119275200617504974660817990662085164938209259740775996848463625575460317369836570289350110414167693412626787114572940738151534118072470019665357384016080593442175672674154611465692091576036447518453344821913797013097147285378753985313689153698044127055266365830527635182496802920380995365517711850622104248221297463922263804348589147691653687864200705227703937425511610912536071237392847317477870016104413756526582622276157411098563739267289126907818832105343995216627391637251157402591147707075267660870304584210801395434086232401877249
print(pollar(n))
