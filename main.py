# John Elehwany
# CompSci PA01 Project
# Professor Zee

# This project is a text-based game. The player will make choices depending on the situation, and will earn an amount of points not displayed to them. This will also change depending on their confidence level. The player will receive text feedback and will learn if they win or not in the end.

score = 10 # initial amount
req_score = 20
confidence_multiplier = 1.0  # initial placeholder amount

# Asks the user for their name. Asks for re-input if the input is not composed of letters
while True:
    name = input('Welcome! Please input your name: ')
    if name.isalpha():
        break
    else:
        print('Invalid answer! Please re-input your name. ')

# Intro to the game
print(f"""
THE BIG DAY
Tuesday, the office, 12:15 PM

Well {name}, the time has come. It's another day at the office, but it's no ordinary day, for you. It's time to give your big presentation to your boss and colleagues!
One issue, though: you didn't prepare! You have the presentation slides, but you forgot it was today; you thought it was supposed to be the day after!
Too late now... your presentation is starting in only a few minutes! Your colleagues are all anxiously awaiting your exciting presentation as they sit around the meeting table.

The Boss, sitting at the head of the table, calls your name. "Alright {name}, you're up. As you may know, our company has been going through some tough hardships lately. I, and the rest
of us here, are hoping that you could pitch us some good advice for dealing with such an issue, as you have requested to do so. Please present to us now."

Well... it's time. It seems that this presentation has a lot riding on it. Let's do this!
""")

# Asks their user for their confidence level. Asks for re-input if it does not meet criteria
while True:
    confidence = input('On a scale of 1 to 5, how confident do you feel? (higher number = higher confidence) ')
    if confidence.isdigit() and 1 <= int(confidence) <= 5:
        confidence = int(confidence)
        break
    else:
        print('Invalid answer! Please only answer with an integer from 1-5.')

# Confidence level multiplier adjustments depending on input
if confidence == 1:
    confidence_multiplier = 1.1
elif confidence == 2:
    confidence_multiplier = 1.3
elif confidence == 3:
    confidence_multiplier = 1.6
elif confidence == 4:
    confidence_multiplier = 1.8
elif confidence == 5:
    confidence_multiplier = 2.1

# Continuation of the story via outputs. Dialogue changes depending on confidence level
if confidence == 1 or confidence == 2:
    print(f"""
You step up. It's time. But you're feeling a bit unconfident...
"Hey, um... hello, everyone. My name is. uh, {name}, and I'm here to discuss this... issue that we've been trying to deal with for the past few weeks."
The people around the table look a little concerned about your confidence in that sentence, but it's nothing to worry about... maybe.
""")
elif confidence == 3:
    score = score + 1
    print(f"""
You step up. You're feeling pretty neutral about this and it shows.
"Hello. My name is {name} and I'm here to discuss this issue that this company has been struggling with for the past few weeks."
A lot of neutral responses from around the room. But they still do look interested.
""")
elif confidence == 4 or confidence == 5:
    score = score + 2
    print(f"""
You step up. You're feeling good despite this predicament you're in.
"Hey, great to be here. My name is {name} and I'm here to provide insight on the issue that this company has been struggling with for the past few weeks. We can do this."
Your confidence has generated good responses from your colleagues!
""")

# First multiple choice section of the code (mc1)
print("""You try to act like you know what you're talking about. "As we all know, the latest major incident within our supply department has been..."

 A - "...has been something that is of utmost importance."
 B - "...has been something that is important but there are greater tasks at hand."
 C = "...has been something to not worry about."
 """)
while True:
    mc1 = input('What will you say? ')
    if mc1 in ['a', 'b', 'c']:
        break
    else:
        print('Invalid answer! Only answer by typing in A, B, or C.')

if mc1 == 'a':
    print("""
    Seemed like a good thing to say, especially considering the reactions of your peers!""")
    score = score + 5
elif mc1 == 'b':
    print("""
    An alright answer. Your Boss looks a little confused at that, but your colleagues seem invested.""")
    score = score + 3
elif mc1 == 'c':
    print("""
    Your colleagues share mixed looks to each other. Maybe not the best thing to say there...""")

# Written response (wr)
print("""
You continue, hoping to still make it through this with your job still intact.
"Our losses have been quite large. We've been seeing percentage losses of..."
(Wait, what was that percentage again? You could've sworn you saw it yesterday in the office.
You're pretty sure it was between 10% and 20%, but it also had some decimal places in it too...
It's all very fuzzy-- it was pretty early in the morning when you saw that yesterday. But now's not the time for flashbacks!
The boss looks a little unimpressed. Quick, say something! And try to be precise too!
""")
while True:
    wr = float(input('What percentage do you think it was? %'))
    if 10 <= wr <= 20:
        break
    else:
        print('Invalid answer! Put an answer only between 10 and 20.')

if 10 <= wr <= 13.5:
    print("""
    The room feels like they're unsure how to feel about that. Maybe you undershot that percentage by a bit. Darn!""")
    score = score + 2
elif 13.6 <= wr <= 16.5:
    print("""
    Seems pretty spot on! They're all impressed with that answer, especially the Boss.""")
    score = score + 5
elif 16.6 <= wr <= 20:
    print("""
    The room feels like they're unsure how to feel about that. Maybe you overshot that percentage by a bit. Darn!""")
    score = score + 2

# Continuation of the presentation, with scores dependent on confidence_multiplier
print("""
You continue your presentation. You go off whatever the presentation says for the next few minutes, saying whatever it says on the slides.
""")

# Calculate score based on confidence level
if confidence == 1:
    score = score + (1 * confidence_multiplier)
    print("""
    It seems that your confidence is a main factor in success here. And it seems like it's not winning them over...
    """)
elif confidence == 2:
    score = score + (2 * confidence_multiplier)
    print("""
    It seems that your confidence is a main factor in success here. And it seems like you're not doing the worst, but it could be doing better.
    """)
elif confidence == 3:
    score = score + (3 * confidence_multiplier)
    print("""It seems that your confidence is a main factor in success here. And it seems like you're doing alright. Pretty neutral responses all around the room.
    """)
elif confidence == 4:
    score = score + (4 * confidence_multiplier)
    print("""It seems that your confidence is a main factor in success here. And it seems like you're doing well! It's working on your colleagues.
    """)
elif confidence == 5:
    score = score + (5 * confidence_multiplier)
    print("""It seems that your confidence is a main factor in success here. And it seems like you're killing it! Great reactions from both the Boss and your colleagues here.
    """)

# Final multiple choice (mc2)

print("""
With these final points you make from the presentation slides, you start to bring your presentation to a close. You've got one final point to make!
You say, "In conclusion..."

A - "...I doubt that we will ever be able to fully recover from such a detrimental issue. I propose that we should cease funding for repairs, as such an issue is only to be fixed by time."
B - "...to get to the bottom of this, every department should spend all of their time and resources to fix such an issue, even if it causes more problems. We can't let this happen again."
C - "...we should do nothing about this and should all take a big smoke break in the lounge.:
D - "...we should take this slow and steady. It might be urgent, but rapid responses often lead to more mistakes. With enough time and evaluation, this will be a thing of the past."
""")
while True:
    mc2 = input('What will you say? ')
    if mc2 in ['a', 'b', 'c', 'd']:
        break
    else:print('Invalid answer! Please only answer A, B, C, or D')

if mc2 == 'a':
    score = score - 7
    print("""Not a very good answer there... The Boss looks very unpleased and your colleagues whisper things to each other.
    """)
elif mc2 == 'b':
    score = score + 7
    print("""Once you say this, the room fills with applause. You did well there. But was it enough for the Boss? Time to find out...
    """)
elif mc2 == 'c':
    score = score - 10
    print("""Pure silence across the room as you finish with that. Everyone looks shocked. You... messed up, to say the least.
    """)
elif mc2 == 'd':
    score = score + 10
    print("""As you finish with those words, a great eruption of applause and smiles go around, including the Boss. You did well! But was it good enough to keep your job?
    """)

# Final results
if score >=  req_score:
    print(f"""
And as your presentation comes to a close, your Boss says, "Hey, {name}, please come meet me in my office in a few."
And a few minutes later, you find yourself sitting across your Boss's big desk. He leans back a little in his swivel chair and says, "{name}, I think you did a pretty darn good job
back there. Everyone seemed really pleased with your competence to present today, and I am too. Good job."

You smile to yourself as you walk out of his office and back to your desk, knowing that you've just done exactly what you've been hoping to hear.
THE END
""")
elif score < req_score:
    print(f"""
And as your presentation comes to a close, your Boss says, "Hey, {name}, please come meet me in my office in a few."
And a few minutes later, you find yourself sitting across your Boss's big desk. As soon as you do, he wears a concerned look on his face. "{name}, you've been wonderful to this company,
but this presentation has proved otherwise. Your incompetence during this company's biggest crisis is too much for us to handle. I think it's time for you to go. I'm sorry."

You quietly walk out of his office and head to your desk to pack up. Time to start padding that resume again.
THE END
""")