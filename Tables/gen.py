import random

width = 100
height = 50

games = {
	"one_armed_bandit": {
		"dimentions": {
			"x": 5,
			"y": 5
		},
		"playerPlaces": [
			{
				"x":0,
				"y": 2.5
			}
		]
	},
	# "poker":{
	# 	"dimentions": {
	# 		"x": 10,
	# 		"y": 20
	# 	},
	# 	"playerPlaces": [
	# 		{
	# 			"x":0,
	# 			"y": 4
	# 		},
	# 		{
	# 			"x":0,
	# 			"y": 8
	# 		},
	# 		{
	# 			"x":0,
	# 			"y": 12
	# 		},
	# 		{
	# 			"x":0,
	# 			"y": 16
	# 		}
	# 	]
	# },
	# "roulette":{
	# 	"dimentions": {
	# 		"x": 15,
	# 		"y": 15
	# 	},
	# 	"playerPlaces": [
	# 		{
	# 			"x":0,
	# 			"y": 5
	# 		},
	# 				{
	# 			"x":0,
	# 			"y": 10
	# 		},
	# 				{
	# 			"x":5,
	# 			"y": 0
	# 		},
	# 				{
	# 			"x":10,
	# 			"y": 0
	# 		},
	# 				{
	# 			"x":5,
	# 			"y": 15
	# 		},
	# 		{
	# 			"x":10,
	# 			"y": 15
	# 		}
	# 	]
	# }	todo()
}

def generate():
    room = {
        "Room size": {
            "x": width,
            "y": height
        },
        "Entrance point": {
            "x": 0,
            "y": height / 2
        },
        "Tables": []
    }

    yOff, xOff = 10, 10
    curX, curY = yOff, xOff
    curGame = 0
    firstRow = True

    while True:
        curGameType = random.choice([i for i in games])
        curGameData = games[curGameType]

        if curX + curGameData["dimentions"]["x"] > width:
            if firstRow:
                firstRow = False
                curX = xOff
                continue
            else:
                break

        if not firstRow:
            curY = height - yOff - curGameData["dimentions"]["y"]

        room["Tables"].append({
            "Type": curGameType,
            "playerPlaces": curGameData["playerPlaces"],
            "Location": {
                "x": curX,
                "y": curY,
                "width": curGameData["dimentions"]["x"],
                "height": curGameData["dimentions"]["y"]
            }
        })
        curX += curGameData["dimentions"]["x"]
        curX += xOff
        curGame += 1


    return room