import pyodbc
import decimal
import time

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Hammaad\Documents\Hammaads stuff\CODE\Python\Files\Tyres.accdb;')
cursor = conn.cursor()
cursor.execute('select * from TYRES STOCK')

pr = True   
while pr == True:
    q1 = input('\n\nWhat would you like to do? (Add/Search) ')
    if q1.lower() == 'add':
        cd = 'false'
        while cd != 'true':
            size = input('\nTire size= ')
            pricex = input('Price Ex VAT= £')
            brand = input('Tyre brand= ')
            f = input('Fuel rating= ')
            w = input('Wet grip= ')
            n = input('Noise rating= ')
            quantity = input('Quantity= ')
            supplier = input('Supplier= ')
            sn = input('Any special note?= ')
            confirm = input('All details correct? (y/n)')
            if confirm.lower() == 'y' and pricex.upper().isupper() == False and quantity.upper().isupper() == False and pricex != '' and quantity != '':
                cd = 'true'
                pricex = float(pricex)
                quantity = int(quantity)
                priceinc=pricex*1.2
                priceinc = float(round(priceinc, 2))
                tf = False
                tnf = True
                for row in cursor.fetchall():
                    if tf == True:
                        break
                    row[0].split(',')
                    oldsize=row[0]
                    oldprice=row[1]
                    oldbrand=row[2]
                    oldfuelrate=row[3]
                    oldwindrate=row[4]
                    oldnoiserate=row[5]
                    oldsupplier=row[6]
                    oldnational=row[7]
                    oldbrittania=row[8]
                    newnote=row[9]
                    oldquantity=row[10]
                    oldnote=row[11]
                    oldneedorder=row[12]
                    oldkeep=row[13]
                    b = 0.02
                    bd = decimal.Decimal(float(b))
                    if str(oldprice)!='None':
                        oldprice = float(oldprice)
                        oldprice = round(decimal.Decimal(float(oldprice)),2)
                        oldpricep = round(oldprice+bd,2)
                        #print(oldpricep)
                        oldpricem = round(oldprice-bd,2)
                        #print(oldpricem)
                    if oldsize.lower() == size.lower():
                        print('\nSize Found!')
                        time.sleep(0.5)
                        if oldbrand.lower() == brand.lower():
                            print('Brand Found!')
                            time.sleep(0.5)
                            priceinc = round(decimal.Decimal(float(priceinc)),2)
                            if oldpricem <= priceinc <= oldpricep:
                                print('Same price!')
                                time.sleep(0.5)
                                tf = True
                                tnf = False
                                print('\nUpdating quantity')
                                pr = True

            
                            else:
                                tf = True
                                tnf = False
                                print('Price is different')
                                mn = input('\nOld price for: (' + str(oldsize) + ', ' + str(oldbrand) + ') was: £' + str(oldprice) + '\nNew price is: £' + str(priceinc) + '\n\n(Old stock remaining: ' + str(oldquantity) + ')\n\nWould you like to add the note: (' + str(oldquantity) + ' at £' + str(oldprice) + ')? (y/n): ')
                                if mn.lower() == 'y':
                                    time.sleep(0.5)
                                    print('\nUpdating quantity, price and adding the note (' + str(oldquantity) + ' at £' + str(oldprice) + ')' )
                                    pr = True
                                else:
                                    print('\nOk! Updating quantity')
                                    pr = True

                        else:
                            tnf = 'nb'
                            tf = True
                            
                            

                    else:
                        tnf = 'ns'
                        tf = True
                        


                if tnf == 'ns':
                    at = input('\nSize not found! Would you like to add the tire: (' +str(size) + ', ' + str(brand) + ', Quantity: ' + str(quantity) + ')? (y/n): ')
                    if at.lower() == 'y':
                        time.sleep(0.5)
                        print('\nAdding tire: (' +str(size) + ', ' + str(brand) + ', Quantity: ' + str(quantity) + ')')
                    else:
                        pr = True


                elif tnf == 'nb':
                    ab = input('\nBrand not found! Would you like to add the tire: (' +str(size) + ', ' + str(brand) + ', Quantity: ' + str(quantity) + ')? (y/n): ')
                    if ab.lower() == 'y':
                        time.sleep(0.5)
                        print('\nAdding tire: (' +str(size) + ', ' + str(brand) + ', Quantity: ' + str(quantity) + ')')
                        pr = True
                    else:
                        pr = True
                    
                    
                

                
                


                                
            else:
                print('\nPlease check details, and try again! ')

    elif q1.lower() == 'search':
        size = input('\nTire size= ')
        brand = input('Tyre brand= ')
        tf = False
        for row in cursor.fetchall():
            row[0].split(',')
            oldsize=row[0]
            oldbrand=row[2]
            if size.lower() == oldsize.lower() and brand.lower() == oldbrand.lower():
                print('\nTyres found!!\n')
                print(row)
                tf = True
                break

        if tf == False:
            print('\nTyre not found!')

    #cursor.execute(f"INSERT INTO TYRES STOCK (Size, Price Ex VAT, Brand, Fuel rating, Wet grip, Noise rating, Quantity, Supplier, Special notes) VALUES (?,?,?,?,?,?,?,?,?)", (size,pricex,brand,f,w,n,quantity,supplier,sn))
#conn.commit()
