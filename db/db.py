import json


days_translater = {
    'Понедельник' : 'monday',
    'Вторник' : 'tuesday',
    'Среда' : 'wednesday',
    'Четверг' : 'thursday',
    'Пятница' : 'friday',
    'Суббота' : 'saturday'
}



def day(day: str) -> list:
    for i in days_translater:
        if day == i:
            with open(f'db/{days_translater.get(i)}.json', 'r', encoding='utf-8') as f:
                ress = []
                res = json.load(f)
                for i in range(len(res)):
                    for j in res[i]:
                        
                        ress.append(res[i].get(j))
            break
    return(ress)        

