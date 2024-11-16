

def sm1(form, sheet):


    val1 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 1:
                value = sheet.cell_value(i, j+1)    
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val1 = sheet.cell_value(a, b)
                        if val1 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val1 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val1 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val1 = value + ''
    
    val2 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 2:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val2 = sheet.cell_value(a, b)
                        if val2 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val2 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val2 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val2 = value + ''
    
    val3 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 3:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val3 = sheet.cell_value(a, b)
                        if val3 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val3 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val3 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val3 = value + ''
    
    val4 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 4:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val4 = sheet.cell_value(a, b)
                        if val4 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val4 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val4 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val4 = value + ''
    
    val5 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 5:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val5 = sheet.cell_value(a, b)
                        if val5 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val5 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val5 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val5 = value + ''
    
    val6 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 6:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val6 = sheet.cell_value(a, b)
                        if val6 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val6 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val6 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val6 = value + ''
    
    val7 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 7:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val7 = sheet.cell_value(a, b)
                        if val7 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val7 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val7 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val7 = value + ''
    
    val8 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 8:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val8 = sheet.cell_value(a, b)
                        if val8 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val8 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val8 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val8 = value + ''
    
    val9 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 9:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val9 = sheet.cell_value(a, b)
                        if val9 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val9 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val9 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val9 = value + ''
    
    

    smena1 = f'1 смена: \n\n{val1}\n{val2}\n{val3}\n{val4}\n{val5}\n{val6}\n{val7}\n{val8}\n{val9}'

    

    return smena1


def sm2(form, sheet):


    val1 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 6:
                value = sheet.cell_value(i, j+1)    
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val1 = sheet.cell_value(a, b)
                        if val1 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val1 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val1 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val1 = value + ''
    
    val2 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 7:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val2 = sheet.cell_value(a, b)
                        if val2 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val2 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val2 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val2 = value + ''
    
    val3 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 8:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val3 = sheet.cell_value(a, b)
                        if val3 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val3 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val3 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val3 = value + ''
    
    val4 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 9:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val4 = sheet.cell_value(a, b)
                        if val4 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val4 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val4 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val4 = value + ''
    
    val5 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 10:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val5 = sheet.cell_value(a, b)
                        if val5 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val5 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val5 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val5 = value + ''
    
    val6 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 11:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val6 = sheet.cell_value(a, b)
                        if val6 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val6 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val6 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val6 = value + ''
    
    val7 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 12:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val7 = sheet.cell_value(a, b)
                        if val7 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val7 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val7 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val7 = value + ''
    
    val8 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 13:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val8 = sheet.cell_value(a, b)
                        if val8 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val8 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val8 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val8 = value + ''

    val9 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 14:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val9 = sheet.cell_value(a, b)
                        if val9 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val9 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val9 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val9 = value + ''
    
    val10 = ''
    for i in range(0, sheet.nrows):
        for j in range(1, 2):
            value = sheet.cell_value(i, j)
            if value == 15:
                value = sheet.cell_value(i, j+1)
                for a in range(i, i+1):
                    for b in range(j, sheet.ncols):
                        val10 = sheet.cell_value(a, b)
                        if val10 == form[0]:
                            if sheet.cell_value(a, b + 1) == form[1]:
                                val10 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                            elif sheet.cell_value(a, b + 3) == form[1]:
                                val10 = value + '\t' + form[0] + ' ' + sheet.cell_value(2, b)
                                break
                        else:
                            val10 = value + ''

    

    smena2 = f'2 смена: \n\n{val1}\n{val2}\n{val3}\n{val4}\n{val5}\n{val6}\n{val7}\n{val8}\n{val9}\n{val10}'


    return smena2

