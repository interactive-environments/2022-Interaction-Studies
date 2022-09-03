// UI - Background
let day = true;
let dayColor;
let nightColor;
let dayScale = 0.0;
let bgColor;
let lCol;

let sun;
let sunimg;
let moon;
let moonimg;
let sunx;
let moonx = -270;

// UI - Sliders, text
let timeSlider;
let pulseText;
let textColor = 0;
let dayButton;

// Creatures
let spirit;
let creatures = [];
let creatureCount = 0;

// Timepulse
let timePulse = 1;
let lastPulse;
let pulseOpacity = 100;
let countDown = 0;

// Day-night timer;
let dayNightTimer = 18000;
let lastSwitch;

// Server connection
const socket = new WebSocket('wss://node.bykrijgsman.com');

socket.addEventListener('open', function (event) {
  print("Connected to server")
  updateInterval();
  
    let timeDay = 0;
  if (day == true){
    timeDay = 1;
  }
  
  socket.send(JSON.stringify({
        password: "InteractiveEnvironments2022",
        messageType: "changeDayNight",
        timeOfDay: timeDay
    }));
  
});

socket.addEventListener('message', function (event) {
    let data = JSON.parse(event.data)
    if(data.hasOwnProperty("messageType")){
      if (data.messageType == "addCreature"){
        print(data)
        addCreature(data);
      } 
      if(data.messageType == "updateEnergy"){
        print(data)
        updateEnergy(data)
      }
      if(data.messageType == "pulse"){
        onPulse();
      }
      if(data.messageType == "neighbours"){
        print(data)
        //updateNeighbors(data);
      }
    }
});

function updateNeighbors(jsonString){
  neighbors = jsonString.neighbours
  amtEntries = Object.keys(neighbors).length;
  for (i = 0; i < amtEntries; i++){
    for (j=0; j < creatures.length; j++){
      if (creatures[j].id == i){
        for (k=0; k < Object.values(neighbors)[i].length; k++){
          let newNeighbor = Object.values(neighbors)[i][k];
          creatures[j].neighbors.push(newNeighbor);
          // print("Added neighbor")
        }
        break;
      }
    }
    
  }
}

function preload() {
  sun = loadImage('sun.png');
  moon = loadImage('moon.png');
}

function setup() {
  
  // UI
  let cnv = createCanvas(windowWidth, windowHeight);
  buttonSetup();
  dayColor = color(255, 223, 143);
  nightColor =  color(0, 62, 106);
  sunx = windowWidth - 270;
  textFont('Roboto');
  
  // Creatures
  initSpirit();
  
//   for(i = 0; i < 16; i++){
//   jsonString = JSON.stringify({
//     "messageType": "addCreature",
//     "name": "creature"+i+"-" + i,
//     "energy": random(0, 10),
//     "neighbors": []
//   });
    
//   if (JSON.parse(jsonString).messageType == "addCreature"){
//      addCreature(JSON.parse(jsonString)); 
//     }
//   }
  
//   jsonString = JSON.stringify(
//   {
//     messageType: "neighbours",
//     name: "name",
//     neighbours: {
//     0: [1,14],
//     1: [0,2],
//     2: [1,3],
//     3: [2,4],
//     4: [3,5],
//     5: [4,6],
//     6: [5,7],
//     7: [6,8],
//     8: [7,9],
//     9: [8,10],
//     10: [9,11],
//     11: [10,12],
//     12: [11,13],
//     13: [12,14],
//     14: [13,0]  
//     }
//   });
  
//   updateNeighbors(JSON.parse(jsonString));
    
  
  // Time pulse
  timeSlider = createSlider(5, 15, 0);
  timeSlider.position(10, 190);
  timeSlider.style('width', '200px');
  timeSlider.addClass("mySliders");
  lastPulse = millis();
  lastSwitch = millis();
  this.timePulse = timeSlider.value();
}

function setBG(){
  switch(day) {
    case true:
      if(dayScale > 0.0){
          dayScale -= 0.01;
        } 
      
          if(sunx < windowWidth - 270){
      sunx += 8;
      moonx += 8;
    }
    else if (moonx > windowWidth){
      moonx = -270;
    }
      break;

    case false:
    if (dayScale < 1.0){
        dayScale += 0.01;
      }
          if(moonx < windowWidth - 270){
      sunx += 8;
      moonx += 8;
    }
    else if (sunx > windowWidth){
      sunx = -270;
    }
      break;

    default:
      break;
  }  
  
  let lCol = lerpColor(dayColor, nightColor, dayScale);
  background(lCol);
  
  moonimg = image(moon, moonx, 20, 250, 250);
  sunimg = image(sun, sunx, 20, 250, 250);
  
}

function draw() {
    noStroke()
  setBG();
  fill(255)
  textSize(14)
  
  // Daynight
  if(millis() > lastSwitch + dayNightTimer){
    switchDayNight();
    lastSwitch = millis();
  } 
  
  // Time pulse
  if (this.timePulse != timeSlider.value()){
    updateInterval();
    countDown = lastPulse + timeSlider.value()*1000;
  }
  if (millis() > countDown){
    countDown = lastPulse + timeSlider.value()*1000;
  }
  
  blendMode(DIFFERENCE)
    let timeLeft = Math.round((countDown - millis())/1000);
    if (timeLeft < 0){
      timeLeft = 0;
    }
   text("One pulse every " + timeSlider.value() + " seconds. Time left: " + timeLeft, 10, 170)   
  
  blendMode(BLEND)

  
  
  if (pulseOpacity > 100){
    pulseOpacity -= 2;
  } if (pulseOpacity < 100){
    pulseOpacity = 100;
  }
  this.spirit.setOpacity(pulseOpacity);
  
  // Creatures
  this.spirit.display();
  for (i = 0; i < creatures.length; i++){
    creatures[i].display();
  }
  
  if (this.spirit.energy > 1){
    this.spirit.setEnergy(this.spirit.energy - 0.005);
  }
  
  fill(255);
  
  displayNeighbors();
}

function displayNeighbors(){
  stroke(255)
  strokeWeight(2)
  let done = [];
  
  for (i=0; i < creatures.length; i++){
    let neighbors = creatures[i].neighbors
    if (typeof(neighbors) !== "undefined"){
    let startx = creatures[i].x
    let starty = creatures[i].y
    for (j=0; j < neighbors.length; j++){
        let findID = neighbors[j]
        for (k = 0; k < creatures.length; k++){
          let foundID =  parseInt(creatures[k].id)
          if (findID == foundID){
            let endx = creatures[k].x
            let endy = creatures[k].y

            line(startx, starty, endx, endy)

        }
      }
    
    }
  }
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  if (moonx < 0){
    moonx = 0 - 270;
  } else if (moonx < windowWidth){
    moonx = windowWidth - 270;
  }
  
  if (sunx < 0){
    sunx = 0 - 270;
  } else if (sunx < windowWidth){
    sunx = windowWidth - 270;
  }
  
  resetCreaturePos();
}

function buttonSetup(){
  this.dayButton = createButton("Make Night");
  this.dayButton.position(10, 220);
  this.dayButton.mousePressed(() => {
    switchDayNight();
  });
}

function updateInterval(){
  // this.timePulse = timeSlider.value();
  socket.send(JSON.stringify({
        password: "InteractiveEnvironments2022",
        messageType: "updateInterval",
        newInterval: this.timePulse
    }));
}

function switchDayNight(){
    day = !day;
  let timeDay = 0;
  if (day == true){
    timeDay = 1;
  }
    
    socket.send(JSON.stringify({
        password: "InteractiveEnvironments2022",
        messageType: "changeDayNight",
        timeOfDay: timeDay
    }));
    
    switch(day) {
    case true:
      this.dayButton.html("Make Night");
      break;
    default:
      this.dayButton.html("Make Day");
    }
}

function onPulse(){
  pulseOpacity = 255;
  lastPulse = millis();
}

function initSpirit(){
  let x = windowWidth/2-35;
  let y = 150;
  this.spirit = new Creature("Benevolent Spirit", x, y, 1, []);
}

function addCreature(jsonString){
  let x = (windowWidth/(creatureCount+1))/2 + creatureCount * windowWidth/(creatureCount+1);
  let y = random(windowHeight/2, windowHeight/4*3-70);
  if (creatureCount > 9){
    y = random(windowHeight/4*3, windowHeight-70);
  }
  
  for (i = 0; i < creatures.length; i++){
    if (creatures[i].name == jsonString.name.split("-")[0]){
      return;
    }
  }
        creatures.push(new Creature(jsonString.name, x, y, jsonString.energy, jsonString.neighbors));
      creatureCount++;

      resetCreaturePos();
}

function updateEnergy(jsonString){
  let match = false;
  for (i = 0; i < creatures.length; i++){
    if (creatures[i].name == jsonString.name.split("-")[0]){
      creatures[i].setEnergy(jsonString.energy);
      match = true;
    }
  }
  if (match == false){
    addCreature(jsonString);
  }
}

function resetCreaturePos(){
  for(i = 0; i < creatures.length; i++){
    let x = (windowWidth/(creatureCount >10 ? 10 : creatureCount))/2 + i * windowWidth/(creatureCount >10 ? 10 : creatureCount);
    if(creatureCount > 10 && i > 9){
      x = (windowWidth/(creatureCount-10))/2 + (i - 10)* windowWidth/(creatureCount-10);
    }
    creatures[i].setPos(x, creatures[i].y)
  }
  this.spirit.setPos(windowWidth/2, this.spirit.y)
}

// Creature class
class Creature{
  constructor(name, x, y, energy, neighbors){
  this.name = name.split("-")[0];
  this.id = name.split("-")[1];
  this.x = x;
  this.y = y;
  
  if (typeof(energy) == "undefined"){
      this.energy = 0;
    } else{
  this.energy = energy;
    }
  this.zoff = random(-10, 10);
  this.opacity = 100;
    
  this.floatrange = [y - 20, y + 20];
  this.floatx = random(0, 10);
  this.floaty = random(0, 10);
    
  this.neighbors = neighbors;
    
  }
  
  display(){
    noStroke();
    beginShape();
    let detailLevel = 0.3;
    let sizeranges = [2, 10, 20, 40];
    let zrange = [0.005, 0.0375];
    let textplacement = [0, 45];
    
    if(this.name == "Benevolent Spirit"){
      textAlign(LEFT);
      fill(255, 255, 255, this.opacity)
       stroke(255, 255, 255, 255)
      detailLevel = 0.05;
      sizeranges = [80, 100, 100, 180];
      zrange = [0.01, 0.02];
      textplacement = [50, 130]; 
    } 
    else {
      textAlign(CENTER);
      if(this.energy == 0){
        blendMode(MULTIPLY);
        fill(150, 150, 150, 130)
        blendMode(SCREEN)
        stroke(255, 255, 255, 180)
      } else{
      blendMode(SCREEN);
        fill(255, 255, 255, map(this.energy, 1, 10, 140, 240))
        stroke(255, 255, 255, map(this.energy, 1, 10, 180, 255))
      }
      
      // vertical floating
      let yfloat = this.y + map(noise(this.floatx, this.floaty), 0, 1, -0.5, 0.5);
      if (yfloat < this.floatrange[0]){
        yfloat = this.floatrange[0];
      } else if (yfloat > this.floatrange[1]){
        yfloat = this.floatrange[1];
      } 
      this.y = yfloat
      this.floatx += 0.005;
      this.floaty += 0.005;
    }
    // noisy circle
    for (let a = 0; a < TWO_PI; a += detailLevel) {
      let xoff = map(cos(a), -1, 1, 0, 2);
      let yoff = map(sin(a), -1, 1, 0, 2);
      let r = map(noise(xoff, yoff, this.zoff), 0, 1, map(this.energy, 0, 10, sizeranges[0], sizeranges[1]), map(this.energy, 0, 10, sizeranges[2], sizeranges[3]));
      if (this.energy == 0){
        r = map(noise(xoff, yoff, this.zoff), 0, 1, sizeranges[0], sizeranges[2]);
      }

      let x = r * cos(a);
      let y = r * sin(a);

      vertex(x + this.x, y + this.y);
    }
    endShape(CLOSE);
    if(this.energy != 0){
      this.zoff += map(this.energy, 0, 10, zrange[0], zrange[1]);
    }
    
    // text
    blendMode(DIFFERENCE);
    noStroke();
    fill(255, 255, 255);
    text(this.name, this.x-textplacement[0], this.y+textplacement[1]);
    blendMode(BLEND);
    textAlign(LEFT);
  }
  
  setPos(x, y){
    this.x = x;
    this.y = y;
  }
  
  setEnergy(newEnergy){
    this.energy = newEnergy;
  }
  
  setOpacity(opacity){
    this.opacity = opacity;
  }
    
}


