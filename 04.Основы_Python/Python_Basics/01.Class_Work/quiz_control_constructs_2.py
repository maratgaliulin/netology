def team_gatherer(req_pro:list):
    employee_base = {'Матвей Чтецов': 'менеджер', 'Егор Антипов': 'разработчик',
                     'Александр Сергеев': 'дизайнер', 'Алина Доброва': 'разработчик',
                     'Руслан Актинов': 'аналитик', 'Алёна Козлова': 'аналитик'}

    for name, pro in employee_base.items():
        if pro in req_pro:
            print(f'{pro} is found: {name}')
            req_pro.remove(pro)
    if len(req_pro) > 0:
        print(f"Couldn't gather the team \n Open vacations: {', '.join(req_pro)}")

# required_pro = ['аналитик', 'аналитик', 'разработчик', 'аналитик', 'менеджер', 'криптотрейдер']
#
# team_gatherer(required_pro)


houses_traits = {
    'Slytherin': ['хитрость', 'находчивость', 'амбициозность'],
    'Gryffindor': ['храбрость', 'благородство', 'честность'],
    'Hufflepuff': ['честность', 'верность', 'трудолюбие'],
    'Ravenclaw': ['мудрость', 'ум', 'творчество']
}

new_magicians = {
    'Arabella Skeeter': ['хитрость', 'творчество', 'находчивость'],
    'Stan Malfoy': ['амбициозность', 'благородство', 'храбрость'],
    'Morgana Granger': ['трудолюбие', 'верность', 'мудрость']
}

for name, personal_traits in new_magicians.items():
    matches = {'Slytherin': 0, 'Gryffindor': 0, 'Hufflepuff': 0, 'Ravenclaw': 0}
    for house, house_traits in houses_traits.items():
        # matches = {'Slytherin': 0, 'Gryffindor': 0, 'Hufflepuff': 0, 'Ravenclaw': 0}
        # if personal_traits in houses_traits.values():
        #     matches[house] += houses_traits[personal_traits]
        matches[house] += len(set(house_traits).intersection(personal_traits))
        # matches[house] += len(personal_traits)
    print(f'{name}: {matches}')