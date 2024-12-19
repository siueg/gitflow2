def filter_by_state(list_, state_='EXECUTED', prav=[]):
    for i in list_:
        if i['state'] == state_:
            prav.append(i)
    return prav


def sort_by_date(list_):
    return sorted(list_, key=lambda x: x['date'][:10], reverse=True)
