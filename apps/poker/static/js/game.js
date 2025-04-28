let heartEmoji = "♥️";
let diamondEmoji = "♦️";
let spadeEmoji = "♠️";
let clubEmoji = "♣️";
let jokerEmoji = "🃏";


const SUITS = ["hearts", "diamonds", "spades", "clubs"];
const SYMBOLS = {
  "hearts": heartEmoji,
  "diamonds": diamondEmoji,
  "spades": spadeEmoji,
  "clubs": clubEmoji
};
const RANKS = [
  "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
];

const CardTemplate = `
<div id="testcard" class="card" side="front" rank="{{rank}}" suit="{{suit}}">
  <div class="card__face">
    <div class="card__value" side="left">
      <div class="value__inner">
        <div class="rank">{{rank}}</div><div class="suit">{{suit__symbol}}</div>
      </div>
    </div>
    <div class="card__content">
    
    </div>
    <div class="card__value" side="right">
      <div class="value__inner">
        <div class="suit">{{suit__symbol}}</div><div class="rank">{{rank}}</div>
      </div>
    </div>
  </div>
  <div class="card__back">
  
  </div>
</div>
`;

const GameTemplate = `
<div class="game">
	<button onclick="flipCard('testcard')">test</button>

  <div class="game__deck">
  
  </div>
</div>
`;


var GameContainer = null;

function init() {
  GameContainer = document.getElementById("game-container");
  if (GameContainer) {
	  GameContainer.innerHTML = GameTemplate;
  }
  else {
    console.error("Game container not found");
  }
  afterLoad();
}

function afterLoad() {
  
  GameContainer.querySelector(".game__deck").innerHTML = GameContainer.querySelector(".game__deck").innerHTML + createCard("A", "hearts");
  GameContainer.querySelector(".game__deck").innerHTML = GameContainer.querySelector(".game__deck").innerHTML + createCard("2", "clubs");
  GameContainer.querySelector(".game__deck").innerHTML = GameContainer.querySelector(".game__deck").innerHTML + createCard("3", "spades");

}


function getCardSymbol(suit) {
  return SYMBOLS[suit] || suit;
}

function createCard(rank, suit) {
  let template = CardTemplate;
  template = template.replaceAll("{{rank}}", rank);
  template = template.replaceAll("{{suit}}", suit);
  template = template.replaceAll("{{suit__symbol}}", getCardSymbol(suit));
  return template;
}

function flipCard(id) {
  const card = document.getElementById(id);
  if (card) {
    card.setAttribute("side", card.getAttribute("side") === "front" ? "back" : "front");
  } else {
    console.error(`Card with id ${id} not found`);
  }
}




document.addEventListener("DOMContentLoaded", init);