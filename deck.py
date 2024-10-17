from flask import Blueprint

import random

DeckApp = Blueprint('deck', __name__)

Route = '/deck'

Cards,Suits = [
    {'Card': 'A','Values': [11, 1]},
    {'Card': '2','Values': [2]},
    {'Card': '3','Values': [3]},
    {'Card': '4','Values': [4]},
    {'Card': '5','Values': [5]},
    {'Card': '6','Values': [6]},
    {'Card': '7','Values': [7]},
    {'Card': '8','Values': [8]},
    {'Card': '9','Values': [9]},
    {'Card': '10','Values': [10]},
    {'Card': 'J','Values': [10]},
    {'Card': 'Q','Values': [10]},
    {'Card': 'K','Values': [10]},
], ["Spades","Hearts","Clubs","Diamonds"]

def NewDeck():
    Deck = []
    
    for Card in Cards:
        for Suit in Suits:
            Deck.append({
                "Suit": Suit,
                "Card": Card["Card"],
                "Values": Card["Values"]
            })
    
    return Deck

@DeckApp.route(Route, methods=['GET'])
def GetDeck():
    return NewDeck()

@DeckApp.route(f"{Route}/random", methods=["GET"])
def GetRandomDeck():
    Deck = NewDeck()
    
    random.shuffle(Deck)
    
    return Deck

@DeckApp.route(f"{Route}/suits", methods=["GET"])
def GetAllSuits():
    return Suits

@DeckApp.route(f"{Route}/cards", methods=["GET"])
def GetAllCards():
    return Cards

@DeckApp.route(f"{Route}/seed/<int:Seed>", methods=["GET"])
def GetFromCardsSeed(Seed):
    Deck = NewDeck()
    
    random.seed(Seed)
    random.shuffle(Deck)
    
    return Deck