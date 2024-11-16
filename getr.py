import requests, xlrd
import urllib

import sch_parc, configg
import ahdsjashdhas


import datetime



def convert_date(tomorrow):
    tomorrow = str(tomorrow).split('-')

    if tomorrow[2] == '01':
        day = '1'
    elif tomorrow[2] == '02':
        day = '2'
    elif tomorrow[2] == '03':
        day = '3'
    elif tomorrow[2] == '04':
        day = '4'
    elif tomorrow[2] == '05':
        day = '5'
    elif tomorrow[2] == '06':
        day = '6'
    elif tomorrow[2] == '07':
        day = '7'
    elif tomorrow[2] == '08':
        day = '8'
    elif tomorrow[2] == '09':
        day = '9'
    else:
        day = tomorrow[2]
    
    
    if tomorrow[1] == '01':
        month = 'yanvarya'
    elif tomorrow[1] == '02':
        month = 'fevralya'
    elif tomorrow[1] == '03':
        month = 'marta'
    elif tomorrow[1] == '04':
        month = 'aprelya'
    elif tomorrow[1] == '05':
        month = 'maya'
    elif tomorrow[1] == '06':
        month = 'iyunya'
    elif tomorrow[1] == '07':
        month = 'iyulya'
    elif tomorrow[1] == '08':
        month = 'avgusta'
    elif tomorrow[1] == '09':
        month = 'sentyabrya'
    elif tomorrow[1] == '10':
        month = 'oktyabrya'
    elif tomorrow[1] == '11':
        month = 'noyabrya'
    elif tomorrow[1] == '12':
        month = 'dekabrya'


    tomorrow = str(day) + '_' + str(month)
    return tomorrow

def convert_date1(tomorrow1):
    tomorrow1 = str(tomorrow1).split('-')

    if tomorrow1[2] == '01':
        day = '1'
    elif tomorrow1[2] == '02':
        day = '2'
    elif tomorrow1[2] == '03':
        day = '3'
    elif tomorrow1[2] == '04':
        day = '4'
    elif tomorrow1[2] == '05':
        day = '5'
    elif tomorrow1[2] == '06':
        day = '6'
    elif tomorrow1[2] == '07':
        day = '7'
    elif tomorrow1[2] == '08':
        day = '8'
    elif tomorrow1[2] == '09':
        day = '9'
    else:
        day = tomorrow1[2]
    
    if tomorrow1[1] == '01':
        month = 'yanvarya'
    elif tomorrow1[1] == '02':
        month = 'fevralya'
    elif tomorrow1[1] == '03':
        month = 'marta'
    elif tomorrow1[1] == '04':
        month = 'aprelya'
    elif tomorrow1[1] == '05':
        month = 'maya'
    elif tomorrow1[1] == '06':
        month = 'iyunya'
    elif tomorrow1[1] == '07':
        month = 'iyulya'
    elif tomorrow1[1] == '08':
        month = 'avgusta'
    elif tomorrow1[1] == '09':
        month = 'sentyabrya'
    elif tomorrow1[1] == '10':
        month = 'oktyabrya'
    elif tomorrow1[1] == '11':
        month = 'noyabrya'
    elif tomorrow1[1] == '12':
        month = 'dekabrya'


    tomorrow1 = str(day) + '_' + str(month)
    return tomorrow1

def convert_date2(tomorrow2):
    tomorrow2 = str(tomorrow2).split('-')

    if tomorrow2[2] == '01':
        day = '1'
    elif tomorrow2[2] == '02':
        day = '2'
    elif tomorrow2[2] == '03':
        day = '3'
    elif tomorrow2[2] == '04':
        day = '4'
    elif tomorrow2[2] == '05':
        day = '5'
    elif tomorrow2[2] == '06':
        day = '6'
    elif tomorrow2[2] == '07':
        day = '7'
    elif tomorrow2[2] == '08':
        day = '8'
    elif tomorrow2[2] == '09':
        day = '9'
    else:
        day = tomorrow2[2]

    if tomorrow2[1] == '01':
        month = 'yanvarya'
    elif tomorrow2[1] == '02':
        month = 'fevralya'
    elif tomorrow2[1] == '03':
        month = 'marta'
    elif tomorrow2[1] == '04':
        month = 'aprelya'
    elif tomorrow2[1] == '05':
        month = 'maya'
    elif tomorrow2[1] == '06':
        month = 'iyunya'
    elif tomorrow2[1] == '07':
        month = 'iyulya'
    elif tomorrow2[1] == '08':
        month = 'avgusta'
    elif tomorrow2[1] == '09':
        month = 'sentyabrya'
    elif tomorrow2[1] == '10':
        month = 'oktyabrya'
    elif tomorrow2[1] == '11':
        month = 'noyabrya'
    elif tomorrow2[1] == '12':
        month = 'dekabrya'


    tomorrow2 = str(day) + '_' + str(month)
    return tomorrow2




def excel_parcer(files_data, tomorrow, tomorrow1, tomorrow2, form):
    shift1 = '1_smena'
    shift2 = '2_smena'

    tomorrow = convert_date(tomorrow)
    tomorrow1 = convert_date1(tomorrow1)
    tomorrow2 = convert_date2(tomorrow2)
    

    day_id1 = f"{tomorrow}_{shift1}"
    day_id2 = f"{tomorrow1}_{shift1}"
    day_id3 = f"{tomorrow2}_{shift1}"
    day_id4 = f"{tomorrow}_{shift2}"
    day_id5 = f"{tomorrow1}_{shift2}"
    day_id6 = f"{tomorrow2}_{shift2}"

    print(day_id3)






    for files in files_data:

        #поиск расписания на завтра
        if files['name'] == day_id1:
            file = files_data.index({'name': day_id1, 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id1 + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)
            
            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=1)
            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break

        elif files['name'] == day_id1 + '_izmeneniya':
            file = files_data.index({'name': day_id1 + '_izmeneniya', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id1 + '_izmeneniya' + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)
            
            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=1)
            
            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break

        elif files['name'] == day_id1 + '_':
            file = files_data.index({'name': day_id1 + '_', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id1 + "_.xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=1)

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break



        #На послезавтра
        elif files['name'] == day_id2:
            file = files_data.index({'name': day_id2, 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id2 + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=2)

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break
            
        elif files['name'] == day_id2 + '_izmeneniya':
            file = files_data.index({'name': day_id2 + '_izmeneniya', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id2 + '_izmeneniya' + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=2)

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break

        elif files['name'] == day_id2 + '_':
            file = files_data.index({'name': day_id2 + '_', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id2 + "_.xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=2)

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break



        #На после после завтра
        elif files['name'] == day_id3:
            file = files_data.index({'name': day_id3, 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id3 + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=3)

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break           

        elif files['name'] == day_id3 + '_izmeneniya':
            file = files_data.index({'name': day_id3 + '_izmeneniya', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id3 + '_izmeneniya' + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=3)

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break

        elif files['name'] == day_id3 + '_':
            file = files_data.index({'name': day_id3 + '_', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id3 + "_.xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            tod = datetime.date.today()
            time = tod + datetime.timedelta(days=3)

            smena1 = f'Расписание - {form[0]}\n{form[1]}\n{time}\n\n' + ahdsjashdhas.sm1(form, sheet)
            break

        else:
            smena1 = 'Расписания не нашлось'



    #Для второй смены
    for files in files_data:

        #поиск расписания на завтра
        if files['name'] == day_id4:
            file = files_data.index({'name': day_id4, 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id4 + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            smena2 = ahdsjashdhas.sm2(form, sheet)

            
            break

        elif files['name'] == day_id4 + '_izmeneniya':
            file = files_data.index({'name': day_id4 + '_izmeneniya', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id4 + '_izmeneniya' + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            smena2 = ahdsjashdhas.sm2(form, sheet)

            
            break

        elif files['name'] == day_id4 + '_':
            file = files_data.index({'name': day_id4 + '_', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id4 + "_.xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            

            smena2 = ahdsjashdhas.sm2(form, sheet)
            break



        #На послезавтра
        elif files['name'] == day_id5:
            file = files_data.index({'name': day_id5, 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id5 + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            smena2 = ahdsjashdhas.sm2(form, sheet)

            break

        elif files['name'] == day_id5 + '_izmeneniya':
            file = files_data.index({'name': day_id5 + '_izmeneniya', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id5 + '_izmeneniya' + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            smena2 = ahdsjashdhas.sm2(form, sheet)

            break

        elif files['name'] == day_id5 + '_':
            file = files_data.index({'name': day_id5 + '_', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id5 + "_.xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            

            smena2 = ahdsjashdhas.sm2(form, sheet)
            break



        #На после после завтра
        elif files['name'] == day_id6:
            file = files_data.index({'name': day_id6, 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id6 + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            smena2 = ahdsjashdhas.sm2(form, sheet)

            
            break

        elif files['name'] == day_id6 + '_izmeneniya':
            file = files_data.index({'name': day_id6 + '_izmeneniya', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id6 + '_izmeneniya' + ".xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            smena2 = ahdsjashdhas.sm2(form, sheet)

            
            break

        elif files['name'] == day_id6 + '_':
            file = files_data.index({'name': day_id6 + '_', 'url': "https://sh40-cherepovec-r19.gosweb.gosuslugi.ru/netcat_files/184/2973/" + day_id6 + "_.xls"})
            link = files_data[file]['url']
            
            data, headers = urllib.request.urlretrieve(link)


            workbook = xlrd.open_workbook(data)

            sheet = workbook.sheet_by_index(0)

            

            smena2 = ahdsjashdhas.sm2(form, sheet)
            break

        else:
            smena2 = ''



    lessons = f'{smena1}\n\n{smena2}'

    return lessons

    




    # Производит загрузку расписания в удобном формате
def loader(tomorrow, tomorrow1, tomorrow2, form):

        files_data = sch_parc.get_suitable_files_url(configg.WEBSITE)
        
        
        if files_data:
                # Загрузка
            # temp_file = open('temp_file.txt', 'wb+')
                    
            lessons = excel_parcer(files_data, tomorrow, tomorrow1, tomorrow2, form)
    
        return lessons
        
# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)
# tomorrow1 = today + datetime.timedelta(days=2)
# tomorrow2 = today + datetime.timedelta(days=3)        


            
# loader('school.db', config.file_temp, config.WEBSITE)