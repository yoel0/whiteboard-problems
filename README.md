# whiteboard-problems

CHALLENGE PROBLEM 1:   🦈 SHARK TALE!🦈
***
Your friend invites you out to a cool floating pontoon around 1km off the beach. Among other things, the pontoon has a huge slide that drops you out right into the ocean, a small way from a set of stairs used to climb out.
---
As you plunge out of the slide into the water, you see a shark hovering in the darkness under the pontoon... Crap!
---
You need to work out if the shark will get to you before you can get to the pontoon. To make it easier... as you do the mental calculations in the water you either freeze when you realise you are dead, or swim when you realise you can make it!
---
You are given 5 variables;
---
```python
sharkDistance = distance from the shark to the pontoon.
```
``` 
The shark will eat you if it reaches you before you escape to the pontoon.
```
```python
sharkSpeed = how fast it can move in metres/second.
```
```python
pontoonDistance = how far you need to swim to safety in metres.
```
```python
youSpeed = how fast you can swim in metres/second.
```
```python
dolphin = a boolean, if true, you can half the swimming speed of the shark as the dolphin will attack it.
```
```
The pontoon, you, and the shark are all aligned in one dimension.
If you make it, return "Alive!", if not, return "Shark Bait!".
```
# Example Function and Test Cases below:
```python
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    pass # Don't get eaten!
```
```python
(shark(12, 50, 4, 8, True) 
# should return "Alive!"

(shark(7, 55, 4, 16, True)
# should return "Alive!"

(shark(24, 0, 4, 8, True)
# should return "Shark Bait!"
```
---
CHALLENGE PROBLEM 2: 🧮 ALL POSSIBLE SUMS 🧮
***
Given a long number, return all the possible sum of each two digits within the number as a list.
For example, 12345:
all possible sum of each two digits from that number are:
```
[ 1 + 2, 1 + 3, 1 + 4, 1 + 5, 2 + 3, 2 + 4, 2 + 5, 3 + 4, 3 + 5, 4 + 5 ]
```
Therefore the result must be:
```
[ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]
```
# Example Function and Test Cases Below:
```python
def digits(num):
    return ???
digits(156)
# should return [ 6, 7, 11 ]
digits(81596)
# should return [ 9, 13, 17, 14, 6, 10, 7, 14, 11, 15 ]
digits(3852)
# should return [ 11, 8, 5, 13, 10, 7 ]
digits(3264128)
# should return [ 5, 9, 7, 4, 5, 11, 8, 6, 3, 4, 10, 10, 7, 8, 14, 5, 6, 12, 3, 9, 10 ]
digits(999999)
# should return [ 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18 ]
```
---
CHALLENGE PROBLEM 3:  🎧 DECODE DUBSTEP REMIX! 🎧
***
Polygradus works as a DJ, making dubstep remixes out of old songs.
You can assume that a song consists of some number of words (that do not contain "WUB").
--- 
To make the dubstep remix of this song, Polygradus may insert some number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then he glues all the words together, including "WUB", in one string and plays the song at the club.
---
For example, a song with the words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" but cannot transform into "WUBWUBIAMWUBX".
---
Recently, Adam heard Polygradus's new dubstep track, but since he isn't into modern music, he decided to figure out the lyrics of the initial song that Polygradus remixed. Help Adam restore the original song.
---
# Input
```
The input is a single non-empty string that consists of only uppercase English letters.  The string's length does not exceed 200 characters.
```
# Output
```
Return the words of the initial song that Polycarpus used to make his dubsteb remix. Separate the words with a space.
```
# Example and Test Cases below:
```python
dubstep_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
dubstep_decoder("AWUBBWUBC")
# should return "A B C"
dubstep_decoder("AWUBWUBWUBBWUBWUBWUBC")
# should return "A B C"
dubstep_decoder("WUBAWUBBWUBCWUB")
# should return "A B C"
```