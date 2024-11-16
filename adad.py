
form = []


def get_form(tec, less):
    form.clear()
    if tec == 'Информатика' and less == 'Лукачевой':
        form.append('ИНФОРМАТИКА')
        form.append('Лукачева М.А.:1')
    elif tec == 'Информатика' and less == 'Лосевой':
        form.append('ИНФОРМАТИКА')
        form.append('Лосева Т.С.:2')
    elif tec == 'Английский язык' and less == 'Росляковой':
        form.append('Англ. язык')
        form.append('Рослякова Е.Ю.:2')
    elif tec == 'Английский язык' and less == 'Вихрист':
        form.append('Англ. язык')
        form.append('Вихрист М.С.:1')
    elif tec == 'Английский язык' and less == 'Борисовой':
        form.append('Англ. язык')
        form.append('Борисова И.Д.:1')
    elif tec == 'Английский язык' and less == 'Осолодкиной':
        form.append('Англ. язык')
        form.append('Осолодкина Д.В.:1')
    elif tec == 'Английский язык' and less == 'Сачковой':
        form.append('Англ. язык')
        form.append('Сачкова Н.А.:2')
    
    
    return form
