from operator import itemgetter

list = []

def productRegistration(newProdutc: dict):
    list.append(newProduct)
    return

initProgram = int(input('Register product? 0 - No  |  1 - Yes '))
while initProgram == 1:
    newProduct = {}
    newProduct['code'] = int(input('Enter the product code: '))
    
    if newProduct['code'] == 0:
        print('Code 0, registration closed!')
        break
    
    newProduct['stock'] = int(input('Enter quantity in stock: '))
    newProduct['minimun'] = int(input('Enter a minimum required stock: '))
    
    productRegistration(newProduct)
    initProgram = int(input('Register product? 0 - No  |  1 - Yes '))

print (f'List of registered products: {list}\n')

orderedList = sorted(list, key=itemgetter('code'))
print (f'List sorted by code {orderedList}\n')

print('List table sorted by code:')
print("Code".center(10), end='')
print("Stock".center(10), end='')
print("Minimun".center(10))

for product in orderedList:
        print(str(product['code']).center(10), end='')
        print(str(product['stock']).center(10), end='')
        print(str(product['minimun']).center(10))