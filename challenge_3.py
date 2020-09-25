def dubstep_decoder(song):
  return' '.join((song.replace('WUB', ' ')).split())

print(dubstep_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
  # =>  WE ARE THE CHAMPIONS MY FRIEND
print(dubstep_decoder("AWUBBWUBC"))
# should return "A B C"
print(dubstep_decoder("AWUBWUBWUBBWUBWUBWUBC"))
# should return "A B C"
print(dubstep_decoder("WUBAWUBBWUBCWUB"))
# should return "A B C"
print(dubstep_decoder("WUBIWUBPUSHWUBWUBMYWUBFINGERSWUBINTOWUBMYWUBWUBEYES...WUBWUB"))
# LOL 

# --The Logic--
# ''.join(song) Connect the strings in the list, where''space is the join character
# song.replace('WUB', ' ') Replace all WUB in the string with an empty space
# song.split() Divide a string into a list of several strings with spaces as the unit