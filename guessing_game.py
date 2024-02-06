import random

class GuessingGame():
  def __init__(self, answer):
    self.answer = answer
    self.solved = False
    # print(self.solved)
    # print(type(self.solved))

  def guess(self,guess):

    last_guess  = guess 
    last_result = None
    # print(self.solved)
    # print(type(self.solved))

    while self.solved == False:
      if last_guess == self.answer:
        print('Your guess was correct')
        self.solved = True
      elif last_guess != self.answer: 
        if last_guess > self.answer:
          last_result = 'your guess was too high'
        elif last_guess < self.answer:
          last_result = 'your guess was too low' 
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print(last_result)
        print(self.answer)

        last_guess  = int(input("Enter your guess: "))
        #

guessed = int(input("Enter your guess: "))

game = GuessingGame(random.randint(1,100))
game.guess(guessed)


# game = GuessingGame(random.randint(1,100))
# last_guess  = None
# last_result = None

# while game.solved() == False:
#   if last_guess != None: 
#     print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
#     print("")

#   last_guess  = input("Enter your guess: ")
#   last_result = game.guess(last_guess)


# print(f"{last_guess} was correct!")