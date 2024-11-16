import requests, xlrd
import urllib

import sch_parc, configg
import ahdsjashdhas


import datetime



def convert_tod(today):
    today = str(today).split('-')
    

    if today[2] == '01':
        day = '1'
    elif today[2] == '02':
        day = '2'
    elif today[2] == '03':
        day = '3'
    elif today[2] == '04':
        day = '4'
    elif today[2] == '05':
        day = '5'
    elif today[2] == '06':
        day = '6'
    elif today[2] == '07':
        day = '7'
    elif today[2] == '08':
        day = '8'
    elif today[2] == '09':
        day = '9'
    else:
        day = today[2]
    
    
    if today[1] == '01':
        month = 'yanvarya'
    elif today[1] == '02':
        month = 'fevralya'
    elif today[1] == '03':
        month = 'marta'
    elif today[1] == '04':
        month = 'aprelya'
    elif today[1] == '05':
        month = 'maya'
    elif today[1] == '06':
        month = 'iyunya'
    elif today[1] == '07':
        month = 'iyulya'
    elif today[1] == '08':
        month = 'avgusta'
    elif today[1] == '09':
        month = 'sentyabrya'
    elif today[1] == '10':
        month = 'oktyabrya'
    elif today[1] == '11':
        month = 'noyabrya'
    elif today[1] == '12':
        month = 'dekabrya'


    today = str(day) + '_' + str(month)
    return today




def excel_parcer_tod(files_data, today, form):
    shift1 = '1_smena'
    shift2 = '2_smena'

    today = convert_tod(today)

    day_id1 = f"{today}_{shift1}"
    day_id2 = f"{today}_{shift2}"






    #Для первой смены
    for files in files_data:

        #поиск расписания на сегодня
        if files['name'] == day_id1:
            file = files_data.index({'name': day_id1, 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id1 + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)
            time = datetime.date.today()

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break

        elif files['name'] == day_id1 + '_izmeneniya':
            file = files_data.index({'name': day_id1 + '_izmeneniya', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id1 + '_izmeneniya' + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)
            time = datetime.date.today()

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break

        elif files['name'] == day_id1 + '_':
            file = files_data.index({'name': day_id1 + '_', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id1 + "_.xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)
            time = datetime.date.today()

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break
    
        else:
            smena1 = 'Расписания на сегодня уже нет'





    #Для второй смены
    for files in files_data:

        #поиск расписания на сегодня
        if files['name'] == day_id2:
            file = files_data.index({'name': day_id2, 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id2 + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            smena2 = ahdsjashdhas.sm2(form, sheet)

            break

        elif files['name'] == day_id2 + '_izmeneniya':
            file = files_data.index({'name': day_id2 + '_izmeneniya', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id2 + '_izmeneniya' + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            smena2 = ahdsjashdhas.sm2(form, sheet)

            break

        elif files['name'] == day_id2 + '_':
            file = files_data.index({'name': day_id2 + '_', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id2 + "_.xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)
            time = datetime.date.today()

            smena2 = ahdsjashdhas.sm2(form, sheet)
            break
        else:
            smena2 = ''





    lessons = f'{smena1}\n\n{smena2}'

    return lessons

    




    # Производит загрузку расписания в удобном формате
def loader_tod(today, form):

        files_data = sch_parc.get_suitable_files_url(configg.WEBSITE)
          # print(files_data)
        
        if files_data:
                # Загрузка
           
                    
            lessons = excel_parcer_tod(files_data, today, form)
    
        return lessons