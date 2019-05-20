# def vat(x):
#     stawka = int(input('podaj stawke : '))
#     return x*(1+stawka)
# dana = [100,200,300,400]
# nowa = []
#
# for i in dana:
#      nowa.append(vat(i))
# print(nowa)

# def brutto():
#     brutto = float(input('podaj stawke brutto '))
#     def vat(x):
#         return x*(brutto+1)
#
#
#     for i in dana:
#         nowa.append(vat(i))
#     return nowa


dana = [100,200,300,400]
def vat(x,a = float(input('podaj vat'))):
    return x*(a+1)
a = list(map(vat, dana))
print(a)
