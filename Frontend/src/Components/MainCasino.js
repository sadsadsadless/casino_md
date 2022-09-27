import React from "react"
import Header from "./Header"
import BG2 from "./image/bag.png"

function BuildTable(table,i){
 let color = "red";
 if (table["Type"] == "roulette"){
	 color = "green";
 }
 if (table["Type"] == "poker"){
	color = "blue";
}
	return(

	<div className={table["Type"]} style={{position: "absolute", 
		height: `${table["Location"]["height"]}px`, 
		width: `${table["Location"]["width"]}px`, 
		left: `${table["Location"]["x"]}px`,
		top: `${table["Location"]["y"]}px`,
		backgroundColor: color}}>
	</div>
	)
}

function BuildPlace(place,i){
	let color = "black";
	   return(
   
	   <div className={place["Type"]} style={{position: "absolute",
		   left: `${place["playerPlaces"]["x"]}px`,
		   top: `${place["playerPlaces"]["y"]}px`,
		   backgroundColor: color}}>
	   </div>
	   )
   }

function buildAllTables(tableList){
	let listToRet = [];
	let i = 0;
	while (i < tableList.length){
		listToRet.push(BuildTable(tableList[i],i));
		i+=1;
	}
	return listToRet;
}

// function buildAllPlaces(placeList){
// 	let listToRetPlace = [];
// 	let i = 0;
// 	while (i < placeList.length){
// 		listToRetPlace.push(BuildPlace(placeList[i],i));
// 		i+=1;
// 	}
// 	return listToRetPlace;
// }


function CasinoTablePos() {
	let gen = generate();
	console.log(gen);
  return (//Класс построение игровых автоматов
    
    <div className="MainCasiino">
    <Header/>
	<main>
      <img src={BG2} alt="" style={{width: "100%",height: "100%", objectFit: "cover",zIndex: "-1", position: "fixed"}}/>
        <div className="Casino">
		<li>
			<div className="Room" style={{position: "absolute", 
				height: `${gen["Room size"].h}px`, 
				width: `${gen["Room size"].w}px`, 
				left: `${gen["Room size"].x}px`,
				top: `${gen["Room size"].y}px`}}>
          	</div>
			{/* <div className="Point" style={{position: "absolute", 
				height: `${gen["Entrance point"].h}px`, 
				width: `${gen["Entrance point"].w}px`, 
				left: `${gen["Entrance point"].x}px`,
				top: `${gen["Entrance point"].y}px`,}}>
			</div> */}
		
		<div className="Tables">
			{buildAllTables(gen["Tables"])}
		</div>
		{/* <div className="Places">
			{buildAllPlaces(gen["Tables"]["playerPlaces"])}
		</div> */}
		</li>
        </div>
	</main>
    </div>
    );
  }


const util = require('util');
const width = 1220
const height = 800
const x = 10
const y = 10

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}


 let games = {
	"one_armed_bandit": {
		"dimentions": {
			"x": 50,
			"y": 50
		},
		"playerPlaces": [
			{
				"x":0,
				"y": 25
			}	
		]
	},
	"poker":{
		"dimentions": {
			"x": 100,
			"y": 200
		},
		"playerPlaces": [
			{
				"x":0,
				"y": 40
			},
			{
				"x":0,
				"y": 80
			},
			{
				"x":0,
				"y": 120
			},
			{
				"x":0,
				"y": 160
			}
		]
	},
	"roulette":{
		"dimentions": {
			"x": 150,
			"y": 150
		},
		"playerPlaces": [
			{
				"x":0,
				"y": 50
			},
					{
				"x":0,
				"y": 100
			},
					{
				"x":50,
				"y": 0
			},
					{
				"x":100,
				"y": 0
			},
					{
				"x":50,
				"y": 150
			},
			{
				"x":100,
				"y": 150
			}
		]
	}
}


function generate()
{
	let room = {
		"Room size": {
			"x": x,
			"y": y,
			"h": height,
			"w": width
		},
		"Entrance point": {
			"x": x,
			"y": y,
			"h": height/10,
			"w": width/10
		},
		"Tables": []
	}
	
	const yOff = 80;
	const xOff = 80;
	let curX = xOff;
	let curY = yOff;
	let curGame = 0;
	let firstRow = true;
	for(;;)
	{
		let game = getRandomInt(3);
		let curGameData;
		let curGameType;
		if(game==0)
		{
			curGameData = games["one_armed_bandit"];
			curGameType = "one_armed_bandit";
		}else
		if(game==1)
		{
			curGameData = games["poker"];
			curGameType = "poker";
		}else
		if(game==2)
		{
			curGameData = games["roulette"];
			curGameType = "roulette";
		}
		if(curX + curGameData["dimentions"]["x"]>width)
		{
			if(firstRow)
			{
				firstRow = false;
				curX = xOff;
				continue;
			}
			else
			{
				break;
			}
		}
		if(!firstRow)
		{
			curY = height-yOff-curGameData["dimentions"]["y"];
		}
		room["Tables"].push({"Type": curGameType});
		room["Tables"][curGame]["playerPlaces"] = curGameData["playerPlaces"];
		room["Tables"][curGame]["Location"] = {
			"x": curX,
			"y": curY,
			"width": curGameData["dimentions"]["x"],
			"height": curGameData["dimentions"]["y"]
		}
		curX += curGameData["dimentions"]["x"];
		curX += xOff;		
		curGame++;
	}
	return room;
}

let room = generate();

export default CasinoTablePos;