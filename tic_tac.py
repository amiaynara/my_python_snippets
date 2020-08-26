# Creating display
def grid_disp():
  pipe='     |     |     '
  global Global_index
  dash='-'*18
  X='X'
  Y='Y'
  X='  '+X+'  '
  Y='  '+Y+'  '
  each_line=''
  for i in range(3):
    print(pipe)
    for j in range(3*i,3*i+3):
      each_line+='  '+Global_index[j]+'  ' 
      if(j%3==2):
        pass
      else:
        each_line+='|'
    print(each_line)
    each_line=''
    print(pipe)
    if(i!=2):
      print(dash)
# Choice Validity
def check_choice_validity():
  choices=['X','O']
  choice='T'
  choice=input("Choose 'X' or 'O': ").upper()
  while choice not in choices:
    choice=input("Choose 'X' or 'O': ").upper()   # for 'special characters' upper does nothing; this allows to be so forword  

  return choice 

# take index input for the real game and check whether it has valid index
def get_move(player_symbol):
  valid_range=list(range(1,10))
  valid_range=[str(x) for x in valid_range]
  global Global_index
  global indices
  index=9999
  while index not in valid_range:
    index=input("Choose a number in [1-9]")
    if(index in indices):
      print("A cell cannot be overwritten!")
      index=' '

  indices.append(index)    # A cell cannot be overwritten
  Global_index[int(index)-1]=player_symbol 

# checks whether the game has to still go on
# technically it should run only after the 5th move. 
def check_game_status():
  global Global_index
  arr=Global_index

  # if any three row has same symbol => winner and game over
  # conditions for winning the game.
  for i in range(3):
    if(arr[i]==arr[i+3] and arr[i+3]==arr[i+6] and arr[i]!=' '):
      print('Congratulations! You have won.')
      return False
  for i in range(0,9,3):
    if(arr[i]==arr[i+1] and arr[i+1]==arr[i+2] and arr[i]!=' '):
      print('Congratulations! You have won.')
      return False # Game won by current player
  if(arr[0]==arr[4] and arr[4]==arr[8] and arr[0]!=' '):
    print('Congratulations! You have won.')
    return False
  if(arr[6]==arr[4] and arr[4]==arr[2] and arr[2]!=' '):
    print('Congratulations! You have won.')
    return False

  # if none of the conditions satisfied => no one has won yet. 
  return True # Game is still On[True] 
  
  # Same for any column

  # Check the diagonal as well

  return True
  
# Game creator
replay_choice="yes"
while replay_choice=='yes':
  Global_index=[' ']*9
  indices=[]
  yes_no=['yes','no']
  # Present the choice for 'X' or 'O'
  user_choice=check_choice_validity()
  ready='No'
  while ready!='yes':
    ready=input('Are you ready to play? Enter Yes or No').lower()
    
  if(user_choice=='X'):
    print('Player1 will go first!')
  else: 
    print('Player2 will go first!')



  # Move acceptor
  for i in range(9):
    grid_disp()
    if(i%2==0):
      get_move('X') # player1 will always be 'X'
    else:
      get_move('Y') 
    if(check_game_status()):
      pass
    else:
      grid_disp()
      break
    if(check_game_status() and i==8):
      grid_disp()
      print("Well played Both of you! It's a DRAW!!!")
      break
  replay_choice="wrong_choice"
  while replay_choice not in yes_no:
    replay_choice=input("Do you want to play again? Yes or No").lower()
  
