const CARD_IMAGES = {};

function loadCardImages() {
    let cardTypes = PlayingCard.RANKS * PlayingCard.SUITS;
    let loadCount = 0;
    
    return new Promise((resolve, reject) => {
        PlayingCard.SUITS.forEach((suit, _) => {
            CARD_IMAGES[suit] = {};
            for (let rank = 0; rank <= PlayingCard.ACE; rank++) {
                let card = new PlayingCard(rank, suit);
                const image = new Image();
                image.src = card.getSVGFilePath();
                image.onload = () => {
                    CARD_IMAGES[suit][rank] = image;
                    if (loadCount === cardTypes) {
                        resolve();
                    }
                }
                image.onerror = reject;
            }
        });
    })
}


window.onload = () => {
    loadCardImages().then(() => {
        let x = 50;
        let y = 50;
        let h = 0;
        for (let suit in CARD_IMAGES) {
            for (let rank in CARD_IMAGES[suit]) {
                let image = CARD_IMAGES[suit][rank];
                Context.drawImage(image, x, y, image.width, image.height);
                x += image.width + 50;
                if (image.height > h) { h = image.height; }
                h = image.height;
            }
            y += h;
        }
    }).catch(error => {
        console.error("Error loading card images: ", error);
    });
    
}



/**
 * Class containing all information about an individual player.
 * @class
 */
class Player {
    /**
     * @param { number } hp - Player's current hitpoints
     * @param { number } mhp - Player's maximum hitpoints
     * @param { number } balance - Player's money balance
     * @param { [JokerCard] } jokers - Player's active jokers
     * @param { [PlayingCard] } deck - Cards that the Player can draw from
     * @param { [PlayingCard] } graveyard - Cards that the Player has already played or discarded
     * @param { number } handSize - Number of cards the Player should draw to
     * @param { [PlayingCard] } hand - Cards that are in the players hand
     */
    consturctor() {
        this.hp = 10;
        this.mhp = 10;

        this.balance = 1000;
        this.jokers = [];
        this.deck = [];
        this.graveyard = [];
        
        this.handSize = 8;
        this.hand = [];

    }

    /**
     * Plays the currently selected hand.
     */
    play() {
        let selectedCards = [];
        this.hand.forEach((card, index) => {
            this.selectedCards.push(card);
            this.hand.splice(index, 1);
        });


        this.jokers.forEach((card, index) => {
            card
        });


    }

    draw() {
        while (this.deck.length != 0 && this.hand.length < this.handSize) {
            let card = this.deck.pop();
            this.hand.push(card);
            card.onDraw(this);
        }
    }

    /**
     * Discards all selected cards in hand.
     */
    discard() {
        let amountDiscarded = 0;
        this.hand.forEach((card, index) => {
            if (card.isSelected === true) {
                this.graveyard.push(card);
                this.hand.splice(index, 1);
                card.onDiscard(this);
                amountDiscarded++;
            }
        })

        return amountDiscarded;
    }
}

/**
 * An abstract class for all types of cards.
 * @abstract
 * @class
 */
class Card {
    /**
     * Constuct a new Card instance
     * @param { boolean } isSelected - Indicated if the player current has this card selected.
     * @param { number } sellValue - Value this card will be sold for.
     * @param { number } baseValue - Base value of the card.
     * @param { number } baseMulti - Base multiplier of the card, added to total multiplier.
     * @param { [] } modifiers - List of all modifiers applied to this card.
     */
    constructor() {
        this.isSelected = false;
        this.sellValue = 0;
        this.baseValue = 0;
        this.baseMulti = 0;
        this.modifiers = [];
    }

    draw(context, x, y, width, height) {
        
    }

    onActivate(player) {

    }

    /**
     * Invoked when this card instance is scored.
     * @param { Player } player 
     * @returns {{ value: number, multi: number }}
     */
    onScore(player) {
        let score = { 
            value: this.baseValue, 
            multi: this.baseMulti 
        };

        return score;
    }

    /**
     * Invoked when this card instance is drawn.
     * @param { Player } player 
     */
    onDraw(player) {

    }

    /**
     * Invoked when this card instance is discarded.
     * @param { Player } player 
     */
    onDiscard(player) {

    }
}

class JokerCard extends Card {
    constructor() {
        super();
    }
}

class TarrotCard extends Card {
    constructor() {
        super();
    }
}

class PlayingCard extends Card {
    KING = 13;
    QUEEN = 12;
    JACK = 11;
    TEN = 10;
    NINE = 9;
    EIGHT = 8;
    SEVEN = 7;
    SIX = 6;
    FIVE = 5;
    FOUR = 4;
    THREE = 3;
    TWO = 2;
    ACE= 1;

    RANKS = [
        PlayingCard.TWO, PlayingCard.THREE, PlayingCard.FOUR, PlayingCard.FIVE, PlayingCard.SIX, PlayingCard.SEVEN, PlayingCard.EIGHT, PlayingCard.NINE, PlayingCard.TEN,
        PlayingCard.JACK, PlayingCard.QUEEN, PlayingCard.KING, PlayingCard.ACE
    ]

    CLUB = 'C';
    DIAMOND = 'D';
    HEARTS = 'H';
    SPADES = 'S';
    SUITS = [PlayingCard.CLUB, PlayingCard.DIAMOND, PlayingCard.HEARTS, PlayingCard.Spades];

    /**
     * @param { number } rank 
     * @param { string } suit 
     */
    constructor (rank, suit) {
        super();
        this.rank = rank;
        this.suit = suit;

        this.baseValue = this.rank;
        this.baseMulti = 0;
    }

    getSVGFilePath() {
        return `static/svg/cards/${this.toString()}.svg`;
    }

    toString() {
        let suitString = `${this.suit}`
        let rankString = `${this.rank}`;
        if (rankString === PlayingCard.ACE) { rankString = 'A'; }
        else if (rankString === PlayingCard.KING) { rankString = 'K'; }
        else if (rankString === PlayingCard.QUEEN) { rankString = 'Q'; }
        else if (rankString === PlayingCard.JACK) { rankString = 'J'; }
        return `${rankString}${suitString}`;
    }

    isFaceCard() {
        return this.rank === PlayingCard.KING || this.rank === PlayingCard.QUEEN || this.rank === PlayingCard.JACK
    }
}


const Canvas = document.getElementById("gameCanvas");
const Context = Canvas.getContext("2d");


const localPlayer = new Player();










document.addEventListener("DOMContentLoaded", function () {
    const socket = new WebSocket('ws://localhost:8000/ws/poker/');

    socket.onopen = function () {
        console.log("WebSocket connected");
        socket.send(JSON.stringify({ 'message': 'Hello, Server!' }));
    };

    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        console.log("Received from server: ", data.message);
    };

    socket.onclose = function () {
        console.log("WebSocket disconnected");
    };
});