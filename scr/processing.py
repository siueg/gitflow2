def filter_by_state(list_, state_='EXECUTED', prav=[]):
    for i in list_:
        if i['state'] == state_:
            prav.append(i)
    return prav
