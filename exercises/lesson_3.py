from user import User
from card import Card

Alex = User("Alex")

Alex.sayName()
Alex.setAge(33)
Alex.sayAge()

card = Card("1234 4567 4567 9876", "12/34", "Alex O")

Alex.addCard(card)
Alex.getCard().pay(1000)

