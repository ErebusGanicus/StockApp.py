# This is a test
# first we print out a greeting and tell the user what
print('BALANCE SHEET DATA')
print("please enter numbers for the Balance Sheet.\n")

# organizing each item into simple letters to be used in a function with the last elements to be updated
ce = ['ce - cash and equivalents----------------------', 0, 0, 0]
sti = ['sti - short term investments-------------------', 0, 0, 0]
nr = ['nr - net receivables---------------------------', 0, 0, 0]
oca = ['oca - other current assets---------------------', 0, 0, 0]
tca = ['tca - total current assets---------------------', 0, 0, 0]
lti = ['lti - long term investments--------------------', 0, 0, 0]
pre = ['pre - property plant equip---------------------', 0, 0, 0]
gw = ['gw - goodwill----------------------------------', 0, 0, 0]
ia = ['ia - intangible assets-------------------------', 0, 0, 0]
aa = ['aa - accumulated amortization------------------', 0, 0, 0]
oa = ['oa - other assets------------------------------', 0, 0, 0]
dlta = ['dlta - deferred long term assets charges-------', 0, 0, 0]
ta = ['ta - total assets------------------------------', 0, 0, 0]
ap = ['ap - accounts payable--------------------------', 0, 0, 0]
scl = ['scl - short current long term debt-------------', 0, 0, 0]
ocl = ['ocl - other_current_liabilities----------------', 0, 0, 0]
tcl = ['tcl - total_current_liabilities----------------', 0, 0, 0]
ltd = ['ltd - long_term_debt---------------------------', 0, 0, 0]
ol = ['ol - other_liabilities-------------------------', 0, 0, 0]
dltl = ['dltl - deferred_long_term_liabilities_charges--', 0, 0, 0]
mi = ['mi - minority_interest-------------------------', 0, 0, 0]
ngw = ['ngw - negative_goodwill------------------------', 0, 0, 0]
tl = ['tl - total_liabilities-------------------------', 0, 0, 0]
mso = ['mso - mis_stocks_options_warrents--------------', 0, 0, 0]
rps = ['rps - redeemable_preferred_stock---------------', 0, 0, 0]
ps = ['ps - preferred_stock---------------------------', 0, 0, 0]
cos = ['cos - common_stock---------w--------------------', 0, 0, 0]
re = ['re - retained_earnings-------------------------', 0, 0, 0]
ts = ['ts - treasury_stock----------------------------', 0, 0, 0]
cas = ['cas - capital_surplus--------------------------', 0, 0, 0]
ose = ['ose - other_stockholder_equity-----------------', 0, 0, 0]
tse = ['tse - total_stockholder_equity-----------------', 0, 0, 0]
nta = ['nta - net_tangible_assets----------------------', 0, 0, 0]

# to group them even further to allow me to print them all out at once
all_stok_data = [ce, sti, nr, oca, tca, lti, pre, gw, ia, aa, oa, dlta, ta, ap, scl, ocl, tcl, ltd, ol, dltl, mi, ngw,
                 tl, mso, rps, ps, cos, re, ts, cas, ose, tse, nta]

# now i need to gather user inputs, that will organize the data, divide them and place them in the right locations
shares_out = int(input("enter total shares outstanding, leave off the last 6 zeros"))
shares_out = int(str(shares_out) + '000000')
print(shares_out)
first_date = int(input("enter the oldest year"))
second_date = int(input("enter the middle year"))
third_date = int(input("enter the newest year"))
print('')


def dat_order(lis, first, second, third):
    """prints out the dates over the list each time it is called"""
    print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
    for i in lis:
        print(i)


def stock_times(mul, work_on):
    """this takes in a number and times it by a multiple, 3 numbers. work on must be a 4 item list"""
    for i in work_on:
        pink = i[1] / mul
        blue = i[2] / mul
        red = i[3] / mul
        i[1] = float("{0:.2f}".format(pink))
        i[2] = float("{0:.2f}".format(blue))
        i[3] = float("{0:.2f}".format(red))
        print(i)


dat_order(all_stok_data, first_date, second_date, third_date)


def stock_nums(year1, year2, year3):
    first = first_date
    second = second_date
    third = third_date

    stock_cata = input('for what category is this number for?')
    stock_year = int(input('for what year?'))
    stock_num = int(input("enter total amount for that category and year, leave off last 3 zeros"))

    if stock_cata == 'ce':
        if stock_year == year1:
            ce[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ce)
        elif stock_year == year2:
            ce[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ce)
        elif stock_year == year3:
            ce[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ce)
        else:
            print("only enter ")
    elif stock_cata == 'sti':
        if stock_year == year1:
            sti[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(sti)
        elif stock_year == year2:
            sti[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(sti)
        elif stock_year == year3:
            sti[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(sti)
        else:
            print(sti, nr)
    elif stock_cata == 'nr':
        if stock_year == year1:
            nr[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(nr)
        elif stock_year == year2:
            nr[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(nr)
        elif stock_year == year3:
            nr[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(nr)
        else:
            print(nr, oca)
    elif stock_cata == 'oca':
        if stock_year == year1:
            oca[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(oca)
        elif stock_year == year2:
            oca[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(oca)
        elif stock_year == year3:
            oca[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(oca)
        else:
            print(oca, tca)
    elif stock_cata == 'tca':
        if stock_year == year1:
            tca[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tca)
        elif stock_year == year2:
            tca[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tca)
        elif stock_year == year3:
            tca[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tca)
        else:
            print(tca, lti)
    elif stock_cata == 'lti':
        if stock_year == year1:
            lti[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(lti)
        elif stock_year == year2:
            lti[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(lti)
        elif stock_year == year3:
            lti[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(lti)
        else:
            print(lti, pre)
    elif stock_cata == 'pre':
        if stock_year == year1:
            pre[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(pre)
        elif stock_year == year2:
            pre[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(pre)
        elif stock_year == year3:
            pre[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(pre)
        else:
            print(pre, gw)
    elif stock_cata == 'gw':
        if stock_year == year1:
            gw[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(gw)
        elif stock_year == year2:
            gw[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(gw)
        elif stock_year == year3:
            gw[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(gw)
        else:
            print(gw, ia)
    elif stock_cata == 'ia':
        if stock_year == year1:
            ia[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ia)
        elif stock_year == year2:
            ia[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ia)
        elif stock_year == year3:
            ia[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ia)
        else:
            print(ia, aa)
    elif stock_cata == 'aa':
        if stock_year == year1:
            aa[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(aa)
        elif stock_year == year2:
            aa[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(aa)
        elif stock_year == year3:
            aa[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(aa)
        else:
            print(aa, oa)
    elif stock_cata == 'oa':
        if stock_year == year1:
            oa[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(oa)
        elif stock_year == year2:
            oa[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(oa)
        elif stock_year == year3:
            oa[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(oa)
        else:
            print(oa, dlta)
    elif stock_cata == 'dlta':
        if stock_year == year1:
            dlta[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(dlta)
        elif stock_year == year2:
            dlta[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(dlta)
        elif stock_year == year3:
            dlta[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(dlta)
        else:
            print(dlta, ta)
    elif stock_cata == 'ta':
        if stock_year == year1:
            ta[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ta)
        elif stock_year == year2:
            ta[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ta)
        elif stock_year == year3:
            ta[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ta)
        else:
            print(ta, ap)
    elif stock_cata == 'ap':
        if stock_year == year1:
            ap[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ap)
        elif stock_year == year2:
            ap[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ap)
        elif stock_year == year3:
            ap[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ap)
        else:
            print(ap, scl)
    elif stock_cata == 'scl':
        if stock_year == year1:
            scl[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(scl)
        elif stock_year == year2:
            scl[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(scl)
        elif stock_year == year3:
            scl[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(scl)
        else:
            print(scl, ocl)
    elif stock_cata == 'ocl':
        if stock_year == year1:
            ocl[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ocl)
        elif stock_year == year2:
            ocl[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ocl)
        elif stock_year == year3:
            ocl[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ocl)
        else:
            print(ocl, tcl)
    elif stock_cata == 'tcl':
        if stock_year == year1:
            tcl[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tcl)
        elif stock_year == year2:
            tcl[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tcl)
        elif stock_year == year3:
            tcl[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tcl)
        else:
            print(tcl, ltd)
    elif stock_cata == 'ltd':
        if stock_year == year1:
            ltd[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ltd)
        elif stock_year == year2:
            ltd[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ltd)
        elif stock_year == year3:
            ltd[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ltd)
        else:
            print(ltd, ol)
    elif stock_cata == 'ol':
        if stock_year == year1:
            ol[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ol)
        elif stock_year == year2:
            ol[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ol)
        elif stock_year == year3:
            ol[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ol)
        else:
            print(ol, dltl)
    elif stock_cata == 'dltl':
        if stock_year == year1:
            dltl[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(dltl)
        elif stock_year == year2:
            dltl[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(dltl)
        elif stock_year == year3:
            dltl[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(dltl)
        else:
            print(dltl, mi)
    elif stock_cata == 'mi':
        if stock_year == year1:
            mi[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(mi)
        elif stock_year == year2:
            mi[2] = int(str(stock_num) + '000')

            print(mi)
        elif stock_year == year3:
            mi[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(mi)
        else:
            print(mi, ngw)
    elif stock_cata == 'ngw':
        if stock_year == year1:
            ngw[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ngw)
        elif stock_year == year2:
            ngw[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ngw)
        elif stock_year == year3:
            ngw[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ngw)
        else:
            print(ngw, tl)
    elif stock_cata == 'tl':
        if stock_year == year1:
            tl[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tl)
        elif stock_year == year2:
            tl[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tl)
        elif stock_year == year3:
            tl[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tl)
        else:
            print(tl, mso)
    elif stock_cata == 'mso':
        if stock_year == year1:
            mso[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(mso)
        elif stock_year == year2:
            mso[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(mso)
        elif stock_year == year3:
            mso[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(mso)
        else:
            print(mso, rps)
    elif stock_cata == 'rps':
        if stock_year == year1:
            rps[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(rps)
        elif stock_year == year2:
            rps[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(rps)
        elif stock_year == year3:
            rps[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(rps)
        else:
            print(rps, ps)
    elif stock_cata == 'ps':
        if stock_year == year1:
            ps[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ps)
        elif stock_year == year2:
            ps[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ps)
        elif stock_year == year3:
            ps[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ps)
        else:
            print(ps, cos)
    elif stock_cata == 'cos':
        if stock_year == year1:
            cos[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(cos)
        elif stock_year == year2:
            cos[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(cos)
        elif stock_year == year3:
            cos[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(cos)
        else:
            print(cos, re)
    elif stock_cata == 're':
        if stock_year == year1:
            re[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(re)
        elif stock_year == year2:
            re[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(re)
        elif stock_year == year3:
            re[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(re)
        else:
            print(re, ts)
    elif stock_cata == 'ts':
        if stock_year == year1:
            ts[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ts)
        elif stock_year == year2:
            ts[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ts)
        elif stock_year == year3:
            ts[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ts)
        else:
            print(ts)
    elif stock_cata == 'cas':
        if stock_year == year1:
            cas[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(cas)
        elif stock_year == year2:
            cas[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(cas)
        elif stock_year == year3:
            cas[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(cas)
        else:
            print(cas, ose)
    elif stock_cata == 'ose':
        if stock_year == year1:
            ose[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ose)
        elif stock_year == year2:
            ose[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ose)
        elif stock_year == year3:
            ose[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(ose)
        else:
            print(ose, tse)
    elif stock_cata == 'tse':
        if stock_year == year1:
            tse[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tse)
        elif stock_year == year2:
            tse[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tse)
        elif stock_year == year3:
            tse[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(tse)
        else:
            print(tse, nta)
    elif stock_cata == 'nta':
        if stock_year == year1:
            nta[1] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(nta)
        elif stock_year == year2:
            nta[2] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(nta)
        elif stock_year == year3:
            nta[3] = int(str(stock_num) + '000')
            print("dates---------------------------------------------%d, %d, %d" % (first, second, third))
            print(nta)
        else:
            print(nta, '\n', 'that was the last entry, check to make sure you have not missed anything.')
    else:
        print('done')


stock_state = True
while stock_state:
    more_info = input('need to enter data? "y" if yes, "c" to check list, "p" to print out per share '
                      'data and you\'re done.')
    if more_info == 'y':
        stock_nums(first_date, second_date, third_date)
    elif more_info == 'c':
        print(dat_order(all_stok_data, first_date, second_date, third_date))
    elif more_info == 'p':
        print('thank you that\'s it! see the results below')
        stock_times(shares_out, all_stok_data)
        stock_state = False
        pass
    else:
        print("please enter y, c, or p")
