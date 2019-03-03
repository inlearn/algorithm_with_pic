stations = {'knoe': {'id', 'nv', 'ut'}, 'ktwo': {'wa', 'id', 'mt'}, 'kthree': {'or', 'nv', 'ca'},
            'kfour': {'nv', 'ut'}, 'kfive': {'ca', 'az'}}
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
final_stations = set()
best_station = None
states_covered = set()
for station, states_for_station in stations.items():
    covered = states_needed & states_for_station  # 计算未被选择过的station 与 要求的 州重叠的州数
    if len(covered)>len(states_covered):
        states_covered=covered
        best_station=station
