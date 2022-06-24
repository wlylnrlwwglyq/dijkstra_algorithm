import sys

def get_data(text):
	graph_data = []
	line_count = 0
	for i in text.split("\n"):
		line_count += 1
		if line_count == 1:
			city_count = int(i.split(" ")[0])
			road_count = int(i.split(" ")[1])
		elif line_count == road_count+2:
			src_city = int(i.split(" ")[0])
			dst_city = int(i.split(" ")[1])
			break
		else:
			from_city = int(i.split(" ")[0])
			to_city = int(i.split(" ")[1])
			road_weight = float(i.split(" ")[2])
			graph_data.append([from_city,to_city,road_weight])
	#丸め誤差を防止するために整数に変換する
	power_len = 0
	for i in graph_data:
		if "." in str(i[2]) and power_len < len(str(i[2]).split(".")[1]):
			power_len = len(str(i[2]).split(".")[1])
	for i,value in enumerate(graph_data):
		graph_data[i][2] = round(graph_data[i][2]*pow(10,power_len))
	return (city_count,road_count),graph_data,(src_city,dst_city),power_len


def get_known_min_value_city(known_cities):
	min_value = -1
	min_city_index = -1
	for city_index,value in known_cities:
		if min_value == -1 or min_value > value:
			min_value = value
			min_city_index = city_index
	return min_city_index


def get_unknown_min_value_city(known_cities,dist_data):
	min_value = -1
	min_city_index = -1
	for city_index,value in enumerate(dist_data):
		exists = False
		for i in known_cities:
			if city_index == i[0]:
				exists = True
				break
		if exists == False and value != -1:
			if min_value == -1 or min_value > value:
				min_city_index = city_index
				min_value = value
	return min_city_index


def get_unkown_cities(graph_data,min_value_city,known_cities):
	unkown_cities = []
	for i in graph_data:
		if i[0] == min_value_city and not i[1] in known_cities:
			unkown_cities.append((i[1],i[2]))
		elif i[1] == min_value_city and not i[0] in known_cities:
			unkown_cities.append((i[0],i[2]))
	return unkown_cities


def get_connected_cities(city,graph_data,dist_data):
	connected_cities_data = []
	for i in graph_data:
		if i[0] == city:
			connected_cities_data.append((i[1],i[2],dist_data[i[1]]))
		elif i[1] == city:
			connected_cities_data.append((i[0],i[2],dist_data[i[0]]))
	return connected_cities_data


def get_route(route_data,graph_data,dist_data,src_city,dist):
	if route_data[-1] == src_city:
		return True
	connected_cities = get_connected_cities(route_data[-1],graph_data,dist_data)
	route = []
	for i in connected_cities:
		if dist-i[1] == i[2]:
			route.append((i[0],dist-i[1]))
	if len(route) == 0:
		return False
	for city,next_dist in route:
		route_data.append(city)
		if get_route(route_data,graph_data,dist_data,src_city,next_dist):
			return True
		route_data.pop(-1)
	return False


if __name__ == "__main__":
	filename = sys.argv[1]
	with open(filename,"r") as f:
		text = f.read()
	
	#データ読み込み
	(city_count,road_count),graph_data,(src_city,dst_city),power_len = get_data(text)

	#ダイクストラ法で最短経路の距離を調べる
	known_cities = [] #確定した場所をクリア
	dist_data = [-1]*city_count #すべての地点までの距離を未確定とする
	dist_data[src_city] = 0 #出発点までの距離を0とする
	while True:
		min_value_unknown_city  = get_unknown_min_value_city(known_cities,dist_data) #未確定の地点で一番小さい都市の番号を取得
		known_cities.append((min_value_unknown_city,dist_data[min_value_unknown_city])) #その都市を確定させる
		unkown_cities = get_unkown_cities(graph_data,min_value_unknown_city,known_cities) #確定に繋がった未確定地点のリストを取得
		if len(unkown_cities) == 0: #もう未確定地点が無い
			break
		for i in unkown_cities: #今までの距離よりも小さければ書き直す
			new_unkown_city_value = dist_data[min_value_unknown_city]+i[1] #確定地点の値に足し合わせる
			if dist_data[i[0]] == -1 or dist_data[i[0]] > new_unkown_city_value: #距離が無限大(-1)または大きい場合は小さい方へ書き換える
				dist_data[i[0]] = new_unkown_city_value
	dist = dist_data[dst_city]
	print("distance="+str(dist/pow(10,power_len))) #丸め誤差防止の整数から実数に戻す
	

	#最短距離から経路を逆算する
	route_data = [dst_city]
	get_route(route_data,graph_data,dist_data,src_city,dist)
	route_data.reverse()
	for i,value in enumerate(route_data):
		if i != 0:
			print("-",end="")
		print(value,end="")
	print()
