# Magic_Chronicle_User_Guide.pdf

Magic Chronicle User Guide 
 
Panels 
 
You can add new panels of any installed type from the Add Panels dropdown. Panels are added 
as new tabs in the main pane. You can create a new pane by dragging the panel around to 
create a row or column, then click on the divider to resize exactly how big that row or column is. 
I usually have a main view with the Chronicle and editing-heavy panels like the Character 
Sheet, Lore, Deck Editor, and so on taking up about ⅔ to ¾ of the screen and then a column on 
the left split into two, with my roller and calendar in the top left and my oracles, skills, health, 
and table of contents in the bottom left, and I’ll split health and skills out into a pair of righthand 
panels so I can have them in view at all times, even though that shrinks my main view 
considerably. It can be worth the Chronicle getting a little cramped if it means having ready 
access to Health and Skills while I’m in combat. That’s just me, though. You can arrange your 
panels any way you want. 
 
Essential Panels 
 
All Essential panels are part of Magic Chronicle Apprentice, the free version of the program. 
These are never listed as requirements for other panels even when they are in fact required 
because it should be impossible to have any version of Magic Chronicle that doesn’t have 
these. 
 
Chronicle 
 
The Chronicle panel is a basic word processor. It can do bold, italics, underline, strikethru, and 
six levels of headers, and it can also accept image uploads. 
 
You can make the image upload bar sticky so that it’ll follow you as you scroll downwards, or 
you can unstick it so it won’t clutter up the screen while you’re writing. Images can be justified 
left or right, in which case words will wrap around them, or be centered, in which case they’ll be 
at full resolution and on their own fully separate line of the page. 
 
A single word processor page gets pretty laggy somewhere around 50,000-100,000 words. 
Splitting your chronicle into separate volumes allows you to have multiple pages in one 
Chronicle tab. 


 
You can also have multiple Chronicle tabs, each of which hosts its own set of volumes, in case 
you end up with a Chronicle spanning several million words to the point where navigating all the 
volumes is itself difficult. You can double click on a tab to rename it, for example, from Chronicle 
to Chronicle I and Chronicle II. 
 
If you close a Chronicle tab, you can restore it from the Manage Panels window, or you can 
delete it forever. 
 
If you have a Calendar panel open and MOD+SHIFT+ENTER, you will automatically advance 
the date by 1 day and create a new 5th level header named after the current day. If you 
MOD+SHIFT+. it will do the same with a 6th level header for advancing one hour. You can use 
these as long/short rest buttons. 
 
Known bug: Deleting a Chronicle tab sometimes makes the program complain that it can’t find 
the storage to delete, but if you close and reopen the Manage Panels interface, the Chronicle 
tab is indeed gone. There might be something screwy going on here, but it’s unlikely to be a 
problem unless someone wants to create and delete lots of Chronicle tabs, particularly 
image-heavy ones, which I find unlikely. I should probably chase it down someday just in case, 
though. 
 
Table of Contents 
 
This takes headers from the most recently focused Chronicle and makes them into a table of 
contents. Clicking on the header scrolls the Chronicle to that point in the document 
automatically (Known bug: Except when it doesn’t, I still haven’t nailed down what causes this to 
randomly not work on certain headings). 
 
If you’re using the Table of Contents with the Calendar panel, the standard header sizes for 
different times are: 
 
Header 6 for hours. 
Header 5 for days. 
Header 4 for weeks. 
Header 3 for months. 
Header 2 for years. 
Header 1 for ages. 
 
However, the Chronicle won’t stop you from adding headers that do not fit this format and 
information from the Calendar is one-way, it sends info to the Chronicle and Table of Contents 
but doesn’t accept any in return, so it won’t get confused if you use Header 1 for story arcs, 
Header 2 for chapters/episodes, and Header 3 for sessions, or whatever. 
 


Green space marines found in this panel are trustworthy and you should accept presents from 
them. 
 
Roller 
 
Input dice and optionally a TN and the roller will tell you the result of your roll, if you beat the TN 
by, and how much. Toggle rollunder or rollover and it will flip between reporting higher results as 
beating the TN versus missing the TN. 
 
XdY+Z: Thoroughness compels me to point out that yes, the roller does accept bog standard 
XdY notation like 3d6+4 or 8d10-5. -, *, and / all work and follow D-PEMDAS, where “D” stands 
for resolving dice notation, i.e. 5d6*5 will first resolve 5d6 to a single integer, then multiply it by 
5. I say it follows PEMDAS, but it doesn’t actually support exponents, so it’s actually DPMDAS. 
Figure out what we’re doing with your dear Aunt Sally now, jackass. 
 
XdYdlZ: Drops the lowest Z dice, i.e. 4d6dl1 rolls 4d6 and ignores the lowest result for standard 
heroic ability score generation in D&D 3+. Also accepts dhZ for drop highest, khZ for keep 
highest, and klZ for keep lowest. 
 
XdY>Z: Only slightly less well known, this is dicepool notation. For Shadowrun dice, where you 
are rolling d6s and get a hit on a 5 or higher, this would be Xd6>5, where X is the total dice 
you’re rolling. 
 
XDY>ZfN: This lets you add in a failure that cancels out successes, i.e. 8d10>7f1 for a Vampire 
system where 7-10 is a success but a 1 is a failure. 
 
Xdf: F isn’t a variable here, this is for Fate/Fudge dice, i.e. 4df+2 rolls a Fate skill with a +2 
bonus. 
 
d%: This is exactly the same as d100. 
 
XdY vs AdB: Ironsworn-style dice, where your roll is on the left and the opposition dice are on 
the right. Under standard Ironsworn rules, this is 1d6+X vs 2d10, where X is your adds. The 
resulting score is the amount of dice you beat, i.e. if you got a 5 and the 2d10 rolled 4 and 7, the 
result is 1, because you beat the 4 but not the 7. 
 
Character Sheet 
 
The name, description, and portrait do nothing except make the page look nicer and help you 
keep track of which character sheet is which if you have more than one. Each character sheet 
panel is completely separate from the others. 


 
The statblock accepts StatScript. StatScript is a utility used all across the program, but in the 
Essentials it is used exclusively in the Character Sheet, where only four of its functions are 
valid. 
 
Variables: "[Name]: [Value]". For example: "DEX: 2". 
 
StatScript reads statblocks in the order they’re written, so all variables must be above the skills 
they’re used in. Variables can also have other variables in them (i.e. “Passive Perception: 10 + 
WIS + Proficiency”), subject to the same necessity to define the variables used before using 
them. 
 
Skill checks: "[Name]. [Type] Check: [dice notation]". For example "Acrobatics. DEX Check: 
1d20+DEX+Proficiency". 
 
“Check” is required to let the program know this is a skill check, not an attack roll. The character 
sheet does not use attack rolls. The type is used as a little badge in the Skills panel, which can 
make it easier to navigate. I usually prefer to make the StatScript sound choppy if it makes the 
badge look better, i.e. “DEX Save. Saving Throw Check: 1d20 + Proficiency + DEX” uses 
“Saving Throw Check” which is filed with the Department of Redundancy Department, but in the 
Skills panel it puts a badge labeled “Saving Throw” on the side, which is convenient. 
 
HP: "[Name]: [Current]/[Maximum] ([color])". For example: "HP: 5/5 (red)". There's a little over 
100 color names hardcoded in, plus you can do a hex value if you preface it with #. I hardcoded 
the names to colors using a standard list of CSS colors that I selected on the grounds that it was 
the first hit on Google and surely Google wouldn’t lie to me. I cannot find it anymore, but I’m 
pretty sure it’s the same as this one. 
 
Clock: "[Name] ([Current]/[Maximum]): [literally anything]". For example: "1st Level Spells (4/4): 
Magic Misslie, Shield, Sleep, Charm Person". It doesn't matter what you put after the colon, but 
the colon is necessary to let StatScript know it’s a clock. I like to add reminders of what the clock 
can be spent on, since clocks on character sheets are almost always for some kind of 
consumable resource like spell slots or ammo or HP if you like circle HP bars. 
 
You can also add HP bars and clocks using the visual tools, and these will be fully compatible 
with the ones added via StatScript. The new Character Sheet should also gracefully translate 
any stats or skills defined in the old 1.0.3 Character Sheet, the one that was a nightmare 
hedgemaze of dropdown menus, into StatScript. 
 
Concatenation: You can concatenate stats into a dice expression with &. For example, you 
could have a Magic skill check that is “Magic. Skill Check: INT & d6.” Then, if your INT is 3, your 
Magic skill check will roll 3d6. 
 


Health 
 
The Health panel takes HP bars and clocks from the most recently focused Character Sheet 
and displays them. You can edit them directly in the Health panel, so you can keep a small 
Health panel in the corner for reference and quick updates during play. All changes made to the 
Health panel propagate back to the Character Sheet. 
 
Known bug: Unless the health bar or clock was made in StatScript, in which case it will always 
be at its default value in the statblock and will reset to the default if you close and reopen the 
panel. 
 
Skills 
 
The skills panel takes skills from the statblock of the most recently focused Character Sheet (it 
ignores any other panel that accepts StatScript, i.e. NPCs). Clicking on a skill transfers the roll 
directly to the Roller tab, where you can set a TN and roll. 
 
If you live in the future, the Skills panel also has a toggle that will automatically roll a die when 
you click on the Roll button, rather than just sending it to the Roller panel and waiting for you to 
input the TN and click Roll in that panel. If you’re using a system like Ironsworn, where the TN is 
built into the roll, or a system like Apocalypse World, where the TN is always the same, this can 
save you a click. 
 
Quest Log 
 
A quest’s title and icon are displayed in the list of quests and helps you identify which is which 
and make them look nice. 
 
The title is also searchable, as are the type, source, and tags. The type and source (but not 
tags) are also used to distinguish quests from each other during an import. If you import a quest 
with an identical name, type, and source as one you already have, the program will assume it’s 
a duplicate and keep one while discarding the other. However, if you import a quest with the 
same name and type but a different source (i.e. one “Goblin Bandits” quest comes from Lost 
Mines of Phandelver and the other comes from Petals and Thorns) then the program will be 
able to recognize they’re different. This means you can import overlapping databases and, as 
long as they all use consistent types and spell their sources the same way, you won’t end up 
with a bunch of redundant quests, nor will quests with common names overwrite each other. 
 
If you live in the future, the quest log will have another input field part of the top block for 
location tags. Location tags are searchable just like tags, don’t get taken into consideration for 


deduplicating imports just like tags, but unlike tags, they’re used to determine which quests are 
valid as side objectives for which other quests in the Auction Panel. If you don’t have the 
Auction Panel, location tags are tags but again. 
 
Quests also have a clock, indicating how close you are to completing it. You can tick the clock 
up or down from the list view, which means you can use the list view as a corner panel and be 
able to easily add progress to any active quest. 
 
Once you start accumulating a lot of completed quests, or if you create or import a large number 
of quests in advance, you’ll need to use the dropdown filter: 
 
-All displays every quest, regardless of completion. 
-Unlocked displays all quests that are unlocked. Quests are locked by default and automatically 
unlocked when you fulfill their prerequisites on a quest tree or add them to a quest tree without 
any prerequisites. If you don’t have the Quest Tree panel, you can manually unlock a quest 
whenever you make/start it. 
-Not started displays all quests which are unlocked but have no progress. If you don’t have the 
Quest Tree panel, this is a list of all quests you’ve bothered manually unlocking but haven’t put 
a single point into progress yet. 
-In progress displays all quests that have at least one point of progress but which are not yet 
maxed out. 
-Incomplete displays all quests that are either not started or in progress, while ignoring any 
which are locked or completed. 
-Complete displays all quests that have maxed out progress clocks. 
 
As you can see, the most useful of these for using Quest Log as a corner panel are in progress 
and incomplete (in the latter case, especially if you’re creating quests as you go and manually 
unlock them immediately). 
 
Quests also come with no less than four different types of major text and image input fields just 
like the Chronicle, which you will most likely completely ignore unless you are building quests for 
export. The Preview is viewable even when the quest is locked. The Intro explains the hook and 
initial goal of the quest, and is viewable when the quest is unlocked. Chapters become viewable 
when a certain amount of progress has been accumulated, and can be used to introduce new 
twists and complications to the quest. Finally, the Complete field is viewable only when the 
quest’s progress clock is maxed out. I fill these in as I go to create a summary of the quest’s 
progress, writing in a line or two in the intro as a reminder of what my goal is and how I got into 
this mess in the first place, and then briefly summarizing the event that led to me marking 
progress in a new chapter every time I do so. 
 
Rulebook 
 


In retrospect there wasn’t really any good reason to add even a simple .pdf viewer to this 
program, as I’ve found it’s much easier to just use a dedicated .pdf viewer to reference 
rulebooks instead. It still works, though. 
 
Image Viewer 
 
The image viewer panel will display any images you upload to it. That’s it. It is purely there to 
make your setup look prettier. I have a couple of cool icons that I’ll stick in corner panels that I’m 
not currently using, so that my interface isn’t cluttered up with unused information, but I still have 
those panels properly sized when I return to them. 
 
Expanded Panels 
 
Expanded panels are either included in Magic Chronicle Adept, the standard version of the 
program, or else are intended as complete replacements for one or more panels in Adept, like 
the Battle Panel DLC, which is considered an upgrade of and wholesale replacement for the 
Battle Grid panel that comes packaged with Adept. 
 
None of these panels have requirements listed because the only thing they require is either an 
Essential panel or the panel they come packaged with. Battle Grid is pretty useless without 
NPCs, but it also comes with NPCs. 
 
Oracles and Deck Editor 
 
Oracles in Magic Chronicle are drawn as cards from a deck. You can have them work exactly 
like rollable tables if you want (that’s the default behavior, even), but there’s still gonna be a lot 
of card terminology while we’re talking about them. I just know I’m going to lose at least one 
sale because someone just can’t stand that the button for running Math.random() is labeled 
“Draw” instead of “Roll,” but $30 isn’t worth having people that neurotically entitled in my 
community. This is what people come to a user’s guide for: To see the creator of the program 
get angry at a guy he suspects exists. 
 
You can quickly search up oracles from your collection in the search bar, including by tag. When 
you draw a card from an oracle deck, the text of the card is printed in the Oracles panel, 
allowing you to use the Oracles panel as a corner panel. You can click on the title or text of the 
result to bring up a window that displays the full text on top of the oracle’s card image as a 
background. You can click on the text to see the background image alone, then click anywhere 
on the image to bring the text back. 
 


Shuffle, Decrease, and Discard 
 
Each result in the Deck Editor can have a weight attached to it, indicating how many copies of 
that card are in the deck. 
 
When you draw an oracle card, three options are displayed along with the short text result in the 
Oracles panel: Shuffle, Decrease, and Discard. 
 
“Shuffle” doesn’t affect the weight of the card at all, and in fact does nothing except hide the 
buttons. If you don’t click any of the buttons, or if you click Shuffle because the panel feels 
unfinished until you do, the deck will work exactly like a rollable table. 
 
“Decrease” decreases the weight of the card by 1, effectively removing one copy from the deck. 
This makes it less likely that you’ll encounter the same result again. You can use this to make 
the odds of an encounter lower the more you’ve already seen it. This can also be used to give 
the feeling of slowly clearing a place out, especially if you decrease some results but not others. 
You defeat any hostile goblins you encounter, but not any friendly elves, and slowly you become 
more and more likely to draw elves instead of goblins from the deck. 
 
“Discard” decreases the weight of the card to 0, effectively removing every copy from the deck. 
This guarantees you won’t encounter the same result again. This way you can still have some 
results be much more likely than others, but avoid all repetition. 
 
You can click on the overlapping windows icon to open up the details of an oracle deck as it is in 
play, right now, seeing not only its maximum weight (like you can see in the Deck Editor), but its 
current weight as well. You can also reset the deck from this view, bringing every weight back to 
maximum. 
 
Subdecks 
 
You can add subdecks to a deck. This is a card that instructs the program to draw a card from 
another deck, which it will do immediately. This means you can (for example) create decks for 
faction soldiers and decks for environmental hazards and quickly and easily combine them into 
encounter decks for areas with that terrain type which are controlled by that faction. It’s possible 
to nest these up to six decks deep, so you can have a Sea Encounters deck that includes an 
Aquatic Foes subdeck that includes a Pirates subdeck, and then you could do that three more 
times, which is further than I can even come up with a plausible example for. 
 
The subdeck card - that is, the card instructing the program to draw from that other deck - is 
separate from any of the cards in that deck, and can be shuffled, decreased, or discarded 
separately from those results. This means you can have a deck comprised of three subdecks, 


discard the subdeck after each result, and end up getting exactly one card from each subdeck in 
random order. 
 
If a subdeck is exhausted (i.e. the weight of all of its cards is 0), the subdeck card is 
automatically discarded, so it’s impossible to get a card instructing the program to draw from a 
deck that doesn’t have any cards left. 
 
NPCs 
 
NPCs are displayed as a list of cards, but are also used by all kinds of other panels for the 
images, StatScript, and other variables stored here. 
 
NPC Cards 
 
The NPC’s name and faction icon are displayed at the top of their NPC card, their type is 
displayed in its own bar just above the primary rules text, and their description is displayed in 
the larger text box below. 
 
The primary image is used as the NPC card’s background image. It’s also used as a fallback 
token in any panels which use NPC tokens. 
 
A bar at the bottom keeps track of the NPC’s favor and a clock that can be used to measure 
anything that might increase or decrease about the NPC. Mostly it’s there to keep track of HP 
from the card itself for people who want to use NPC cards rather than the Battle Grid for that 
purpose. Plus, it helps balance out the bottom of the card a little, although making the favor bar 
bigger would do the same thing. I might remove this from the card view, since it’s kind of 
vestigial, but it’s still there as of 1.1.1 and, presumably, whichever version of the program is 
current, seeing as how I apparently haven’t updated this paragraph. 
 
Favor, Friends, and Enemies 
 
NPCs start with an undeletable favor type, “Direct Favor,” and no friends or enemies. “Direct 
Favor” means favor that isn’t secondhand from the NPC’s friends and enemies influence, which 
means additional favor bars are also “Direct Favor,” although the program won’t notice or care if 
you fail to rename the original after adding other favor bars. However, the program does use 
that original favor bar preferentially for a lot of things. 
 
I usually use it for Quest favor, and add separate bars for Gift favor and Charm favor. Maxing 
out favor with someone will require helping them out, giving them gifts they appreciate, and 


generally being friendly with them by making Charm (or other skill) checks at them in 
conversation. 
 
Different characters care about these things different amounts, which is why each favor type 
comes with a weight. If a character weighs Quests at 3, Gifts at 2, and Charm at 1, then this is 
someone not easily flattered by words and who cares about action primarily, but also 
appreciates the effort required to pick out and pay for a gift relevant to their interests. Maxing out 
their quest bar will bring them up to 50% total favor even with no gifts or successful Charm 
checks at all, while simply making good Charm rolls at them while never actually helping them 
out will only ever give you 17% of their total favor. 
 
Weight is totally independent from the maximum value of the favor bar. Continuing the same 
example from before, if Quests has half the total weight (i.e. 3 out of 6) and has a maximum 
score of 10 (as in the default), then each point of Quest favor is worth 5%. If Quests had a 
maximum score of 20, each point of Quest favor would be worth 2.5%. This means you can use 
weights purely to control how much a character cares about that type of behavior while using 
maximums purely to indicate how much gameplay focus you want to have on that behavior. 
 
I usually use 10 points of quest favor, 20 points of gift favor, and 40 points of charm favor for 
every character, even though the weight changes radically (and is often determined randomly by 
rolling d3s). 10 points of quest favor is enough to need 2-3 quests’ worth (or alternatively, lots of 
quick 1-2 point quests completed as side objectives while mostly doing something else), 20 
points of gift favor provides a lot of granularity for gifts of different value and reflects the fact that 
it’s pretty low-effort writing-wise to mulch gp into favor this way, and 40 points of charm favor 
means that it takes a while to fill in even though there’s little penalty to spamming out a Charm 
roll at them any time I talk to them about anything. 
 
Influence is a special favor track that gets activated once an NPC has at least one friend or 
enemy. Influence is an average of the value of the first favor bar (the undeletable one) for every 
friend the NPC has and of the inverse average (i.e. 0% full means 100% favor and 100% full 
means 0% favor) for every enemy. This means people automatically like you a little bit for not 
making friends with their enemies, which is fine so long as most NPCs (who you actually bother 
tracking favor with, at least - you can just ignore it for NPCs like “goblin skirmisher” who exist to 
be battle tokens) have at least one enemy. This makes it impossible to max out favor with 
someone unless you also help out their friends and do not work with their enemies. 
 
You should generally keep the total number of friends and enemies low, but you can make an 
exception for faction representatives. If everyone is friends with their faction representative and 
you use that first favor type for quest favor, that means completing quests for the faction will 
give everyone in that faction a bit of favor with you. If everyone is enemies with the faction 
representatives of hostile factions, that means completing quests for hostile factions will make 
everyone in the faction dislike you. 
 


Friendships aren’t two-way automatically, so it’s on you to hook NPC friends and enemies to 
one another symmetrically, which allows you to have an NPC who’s a hanger on and will like 
you more if you’re friends with their senpai, but senpai does not notice or care if you’re friends 
with the hanger-on. This means a faction representative doesn’t have to be friends in return with 
all the NPCs who are friends with them. They can be, however, which means maxing out favor 
with that faction representative will require not just completing quests for that faction, but also 
completing the personal quests for every named NPC in the faction. And because influence is 
weighted just like any other favor track, you can adjust how much of the faction’s favor comes 
from those personal quests versus the faction-wide quests or any other favor type you add. 
 
NPC Tokens 
 
You can upload a token image, which panels that use NPC tokens (like Battle Grid) will use 
preferentially, in case you have topdown or stylized symbols for the battlemat but want to use 
proper face portraits for the card art (or even if you just want to crop them differently for the 
slightly different shapes). 
 
NPC tokens can also have any amount of HP bars which can be any color, can have a default 
size for their token (20 is the standard, so 40 is a double size token and 10 is half, although I 
find 1.5x is a better size step for size categories - keeps things feeling noticeably bigger/smaller 
than each other but it takes more size categories before it’s hard to use a consistent zoom 
level). 
 
This is also where you can set an NPC script, which matters only if you have the NPC Scripting 
panel. 
 
The Battle Grid comes with the NPCs panel for free. It’s a barebones, just-the-essentials VTT 
which allows you to upload a background for the battlemat, slap a grid on it, and add NPC 
tokens with healthbars. You can add a grid, but the program won’t snap anything to the grid, so 
it’s on you to count squares, and Battle Grid doesn’t make use of StatScript, so there’s no 
automated attacks, terrain-based movement, sightline checking, or AoEs. However, the 
interface for uploading maps and adding NPCs can be completely hidden, so Battle Grid does 
actually have one use over the DLC Battle panel, even though the latter was intended as a 
straight upgrade of and replacement for Battle Grid: Battle Grid can be used as a banner panel 
at the top or bottom of your Chronicle in the main view, slapping down a battle background and 
tokens for the enemies to keep track of how much health the bad guys have while also adding a 
neat vibe. 
 
StatScript 
 
StatScript is a single-purpose programming language designed to look like a human-readable 
TTRPG statblock while being interpretable by Magic Chronicle. Being a regular old computer 


program and not an LLM, Magic Chronicle is very particular about formatting, and if you put the 
colon in the wrong place or misspell a type, it’ll stare gormlessly at your statblock like a koala at 
a plate of eucalyptus leaves. 
 
But none of the Expanded panels use NPC StatScript at all. Battle Grid doesn’t even accept 
NPC HP from StatScript. So the explanation for what StatScript actually does can be found in 
the section for panels that actually use it. 
 
Lore 
 
The Lore panel is a database of lore articles that you can use to keep track of rules, setting 
information, character info if you’d rather have that in the same place as your worldbuilding 
instead of on your NPC cards (or if you’re upgrading piecemeal from Apprentice and don’t have 
the NPC panel), and basically anything else that you can write down or upload images for. A 
lore article takes text and images the same way the Chronicle does. The title and icon are 
primarily there to make the main list look nice and be easier to navigate, the tags are there for 
search, and the type and source help the program keep track of which imports are redundant 
and should be discarded and which are new things that happen to have the same name as an 
old article and both should be retained. 
 
Lore is one of a trio of article collections each of which connects to another Adept panel that can 
make use of it. Lore’s connected panel is the World panel. On the World panel you can upload 
an image as a background, define different overlays (for example, “Political,” “Geographic,” and 
“Blank,” the latter of which for when you just want to see the map), and then divide up different 
regions on each overlay (for example, different kingdoms in “Political” and different terrain types 
in “Geographic”). Each region can be assigned to a Lore article, which is displayed below the 
map when you click on the associated region. 
 
Power 
 
The Power panel is a database of power articles that works exactly like the Lore panel, except 
that it connects to the Abilities panel, not the World panel. 
 
The Abilities panel allows you to add nodes, attach powers to them, give that power an XP 
requirement, and then attach nodes to each other with different connectors to add prerequisites 
and create an ability tree. 
 
A one-way connector means that learning one power unlocks (meaning, it’s available to spend 
XP on, but not automatically learned) the other, but if you learn the other power (by unlocking it 
via a different connector), it does not unlock the first. 
 


A two-way connector means that learning either power unlocks the other. 
 
A key connector means that the destination power is unlocked only when every key is learned. 
While a power unlocked by two different one-way connectors will be unlocked when either 
power is learned, a power unlocked by two different key connectors will be unlocked only when 
both powers are learned. 
 
An excluder connector means that once one power has been learned, the other is locked. You 
can use this to create ability trees that require you to pick one power or another at certain steps, 
then give both of them one-way connectors to the next step to allow the player to continue on 
the path. 
 
An automatic connector means that the destination power is not just unlocked, but learned 
automatically when the origin power is learned. You can use this to create class features that 
come bundled with lots of powers that would otherwise have to be unlocked separately. 
 
You can have multiple ability panels for i.e. different classes or specializations. If you close an 
ability panel, you can get it back from the Manage Panels button, and it will only go away 
completely if you delete the panel. You can also export an ability panel to create a save of just 
the data in that panel and the powers attached, in order to save a clean version you can reset to 
whenever you start over without sacrificing the rest of your project. 
 
You can filter the Powers database by learned/unlearned on a specific ability tree to get a list of 
only the powers you actually have versus a complete list for planning builds or editing details. 
 
Equipment 
 
The equipment panel is an article collection like Power and Lore. The panel Equipment 
connects to is Inventory. Inventory allows you to upload an image of your character, draw boxes 
on that image to create inventory slots (i.e. “weapon,” “helmet,” “cloak,” etc.) and then assign 
equipment articles to each slot. 
 
There’s also a text-input field at the bottom to write down items you want to keep track of, but 
which do not need a dedicated inventory article. For example, it might be important to know 
whether or not you have 50 feet of rope, but there aren’t any rules text associated with that in 
most systems. It’s just 50 feet of rope and allows you to do things that 50 feet of rope intuitively 
permits. It’s also a good place to keep track of your gp. 
 
Your equipment collection can be filtered for equipped/unequipped just like powers can be for 
learned/unlearned. 
 


Esoteric Panels 
 
Esoteric panels are DLC panels, except for the two that aren’t, because I didn’t have the 
specifics nailed down very well when I was first splitting the panels up. 
 
Esoteric panels are far more likely to have specific prerequisites, but even then, usually 
prerequisites within their own pack. I really expected this to be more convoluted, like the way 
the Esoteric Panels are mostly but not completely DLC panels because I didn’t have the 
organization totally nailed down when I split up the Panels menu into submenus, and the early 
panels have lots of weird bugs because I made them first and they show a lot of scars of 
someone who was treating this like a learning project up until around the Oracles panel. But, 
nah, prerequisites just worked out. 
 
Chronology Pack 
 
Requirements: Lore (for Timeline) 
 
The Calendar panel allows you to define hours, days, weeks, months, years, and ages for your 
setting and creates a nice calendar layout for them which can be useful as a corner panel if your 
system is one of the ones where timekeeping is important or alternatively if you just think it looks 
nice. 
 
Hours are only displayed in the date when you short rest using MOD+SHIFT+. on the Chronicle, 
and there’s a toggle to suppress the date so that only the hour is displayed when this happens. 
 
Days can be named anything you like. While Sunday and Monday are named after the sun and 
moon and make sense in most settings, Tuesday is named after Tyr, Wednesday is named after 
Wotan, Thursday is named after Thor, Friday is named after the Rebecca Black hit single, and 
Saturday is named after Saturn. A lot of fantasy worlds vary both the name and number of the 
days, and the calendar will build itself properly no matter how many day names you enter 
(although I only tested this up to a Faerunian tenday, go further at your peril). 
 
Weeks can be named if you like, but you can also suppress them in the date so that name is 
never actually shown. Personally, I like my fantasy calendar with four named weeks exactly in 
each month, and you may also have a very specific fantasy calendar you favor with named 
weeks of the month just like there’s named days of the week. If you want to clearly communicate 
time in your setting to even one single other human being, however, you really should just use 
the “suppress week” option and stick to recognizably named days and unnamed weeks. 
 
You can rename months, but only if you give them extremely on-the-nose names like “early 
winter” so people can still keep track of what season it is. As a best writing practice for 
communicating the passage of time clearly to other people, I mean. In terms of what the 


program can handle, you can name the months anything you want, and if you’re playing solo, 
you’re the only one who has to learn all the new month names, so go nuts. You can put the 
number of days in each month in brackets after each month. The default is 30. 
 
Years are usually numbered, and there are plenty of places that will generate a list of ascending 
numbers for you, although you can also give the years portentious names like the Year of the 
Burning Hawk or the Year of Falling Stars. You only need years on your calendar for times that 
your Chronicle and Timeline actually cover, and depending on how long your Timeline is, that 
might only be four or five years or even just one, in which case giving them individual names will 
not be that hard. If you need a list of years going from 1 to 25,000, there are websites that will 
machine generate that for you. 
 
You can put the starting year of an age in brackets, so you can have the Age of Destiny begin in 
the Year of Crimson Blooms or just 1254 or whatever. 
 
The Calendar panel comes with Magic Chronicle Adept (I hadn’t worked out exactly what was 
going to be DLC yet when I split the panels menu into submenus), but the Timeline panel can 
only be acquired via the DLC download. The Timeline panel allows you to define the duration of 
events, color them appropriately, and place them on any number of different timeline panels. 
You can use this to keep track of festivals in a year in one timeline while the other keeps track of 
actual events, or to keep track of two different kingdoms’ histories separately so it’s easy to 
keep track of the cause-and-effect of internal events in one at a time instead of both mixing 
together on a single unified timeline. 
 
Quest Pack 
 
Requirements: – 
 
The Quest Tree allows you to arrange quests into a tree the same way as the Abilities panel 
allows you to arrange powers. You can have multiple quest trees, and unlike the Abilities panel, 
they share unlock status across trees. Partly this is just because of a difference in how the 
Quest Log panel works, since it has built-in completion tracking. But also it’s intentional, 
because sometimes the same power appears on multiple classes and learning a Fighting Style 
as a Fighter should not instantly multiclass you into Ranger and Paladin, but having a side quest 
tree which is unlocked by reaching a certain stage of the main quest is useful and it’s rare that 
you have the exact same quest in multiple different quest trees the way that you’ll often have the 
exact same power unlocked by multiple different classes. 
 
Battle Pack 
 


Battle Panel 
 
Requirements: NPCs 
 
The Battle Panel allows you to upload background images and pull tokens in from your NPC 
collection. You can then use StatScript statblocks on the associated NPCs to automate attacks 
and skill checks. Each NPC token is completely independent after being generated based on 
the NPC card’s statblock, so you can have a generic NPC like “Goblin Skirmisher” and each 
individual goblin skirmisher token will have separately tracked HP. 
 
If you box-select or CMD+Select multiple tokens, you can mass edit the HP of the tokens by 
name. So you can apply i.e. -4 damage against the HP of all selected tokens, and any tokens 
that have an HP bar called HP will have their HP reduced by 4, while any tokens that lack any 
bar labeled as such will be unaffected. This means you can select every token that failed the 
save against that Fireball and apply -27 Health to them all at once, instead of going one token at 
a time (it’s still on you to pick out which ones made the save versus which ones failed, but you 
can also set up automated AoE attacks to resolve the attack with a single click). 
 
Zones and Cells 
 
You can draw zones on the Battle canvas and then define connections between them. There are 
no automatic connections between zones even if they’re overlapping, as the program makes no 
assumptions about where walls might be located, so you have to connect zones directly. By 
default, zone connections are both transparent and passable, but they can also be opaque but 
passable (blocking line of sight but allowing movement) or transparent but impassable (blocking 
movement but allowing line of sight). 
 
You can add a grid of either hexes or squares (collectively called “cells”) to any map tile you 
upload. Tokens on a grid will obey the movement rules of that grid. They will still be affected by 
tags associated with zones they’re in, but they’ll move one square or hex at a time rather than 
entire zones at a time. Tokens are not hardcoded to zones, squares, or hexes, so you can use a 
token designed for one on a map using another and they will work in the sense that they 
function. Tokens designed for squares or hexes are usually fully interchangeable, but tokens 
designed for zones usually have movement speeds and ranges measured in 1-3 zones, which 
is a comically short space in squares or hexes. 
 
StatScript Variables 
 
Variables, skill checks, HP bars, and clocks use the same format as character sheets. Clicking 
on a token will display all of its skill checks in the righthand inspector column. Clicking on the 
skill check will display the roll over the token automatically. 
 


Variables can also be set to “per token.” If a variable is “per token,” then the dice notation for it 
will be recalculated every time a token is generated, but not altered afterwards. You can use this 
to set, for example, “Hit Dice: 2d8+4 per token” and then set “HP: Hit Dice/Hit Dice” and every 
time a copy of that token is generated, Hit Dice will be rolled for that token and then HP will be 
set to that value, so you can have variable HP amounts for each specific token of a generic like 
the dire wolf or the owlbear or that goblin skirmisher from earlier. 
 
StatScript Tags 
 
If you add in just plain words with no colon anywhere, that will be stored as a tag, so, for 
example, if one line of your stat block just says “human”, then the NPC will have the tag 
“human.” This is identical to tags added via the tags on the NPC card so far as the Battle Panel 
is concerned, and allows for NPC statblocks to be copypasted in a single MOD+C/MOD+V 
without having to then plug tags in specifically to the tags field. 
 
You can also add sets of tags through a line like “vulnerability: cold, fire, psychic”. The type is 
used as a suffix to each of the specific tags given, with the colon removed, so that example 
would add the tags “cold vulnerability”, “fire vulnerability”, and “psychic vulnerability” to the 
token. 
 
Tags don’t actually do anything in the raw Battle Panel, but they affect a lot of things for Rule 
Scripting, so see that section for why you would actually want to do this. The vanilla Battle Panel 
is still capable of accepting tags, so you can use StatScript statblocks created for use with Rule 
Scripting even if you don’t have Rule Scripting. Some of their features will be unavailable, but 
nothing will be broken because of it. 
 
StatScript Attacks 
 
The format for attacks is “[Name]. [Type] Attack: [Attack expression] against [Defense 
expression] range X, [area]. Hit: [effects]. Miss: [effects]. Cost: [cost]. 
 
When you select a token on the Battle canvas, the inspector on the right will list any StatScript 
attacks it has. If you click on the attack and then click on the target, it will execute the attack 
automatically, rolling the dice to determine a hit or miss according to the attack and defense 
expressions and then applying the effects of a hit or miss as listed. 
 
Attack/Defense Expressions 
 
An attack expression is the dice expression used to determine the attack value, for example, 
“1d20 + DEX + Proficiency”. A defense expression is the same, except that any stats referenced 
will be pulled from the target’s character sheet, not the attacker’s (i.e. “1d20 + DEX + 


Proficiency against AC” will roll 1d20, add the attacker’s DEX and Proficiency, and compare that 
to the target’s AC). 
 
You can also use static variables, like “1d20 + DEX + Proficiency against 15” for a system where 
the TN for an attack is always 15. 
 
You can also specify “rollunder” for when a successful hit is below the TN instead of above it 
(exact ties still count as a hit - if you hit the target, you hit). 
 
Range 
 
“Range” determines how many cells (i.e. squares or hexes) or zones (for arbitrary zones) an 
attack can move through. Keep in mind that the token will measure range using whatever type 
of map it’s on, so if you have range 1, that’s a melee attack on a square or hex map but a 
ranged attack into an adjacent zone on a zones-only map. 
 
The program will prevent you from using any attacks outside their allowed range, with a tooltip 
next to your cursor to indicate whether the reason the attack is blocked is due to exceeding the 
maximum range or passing through an opaque zone connection or (if you have the Rule 
Scripting panel) terrain type. 
 
AoE 
 
The valid area effects are “line,” “radius,” and “cone.” 
 
On a square or hex map, a line effect passes through a number of squares equal to the number 
indicated (i.e. “line 12” passes through 12 cells) in a straight line. On a zones-only map, a line 
effect passes through a number of zones equal to the number indicated and affects all tokens it 
physically passes over. This means you can get radically different results by repositioning your 
token within whatever zone you’re in. 
 
On a zone map, a radius includes the target zone and all connected zones out to a number of 
connections indicated by the number (i.e. “radius 1” affects all tokens in the target zone and all 
tokens in connected zones). On a hex map, the radius is simply the number of hexes outward 
from the target hex it affects. On a square map, it is the number of squares that can be reached 
in X movement assuming diagonal steps cost 1.5x as much. This forms something similar to the 
familiar star shapes of D&D square templates, but beware they are slightly different due to being 
centered on a square and not an intersection of squares. All radius AoEs can have a radius of 0, 
which will affect only a single cell on a grid map and may as well be single target, but on 
zone-only maps, it will target all tokens in that zone. 
 


A hex-based map defines a cone in actual hexes: it is every hex covered by a drawing a straight 
line out of two adjacent faces of a hex the indicated number of hexes (i.e. “cone 3” goes out 3 
hexes) including the shared origin hex, along with every hex in a straight line connecting those 
two lines. It sounds convoluted to articulate it in text, but visually it’s totally intuitive: It’s a cone. 
On a square map, I couldn’t figure out any mathematical definition, so I cheated by just drawing 
an invisible cone of the length indicated in squares and futzing with the arc radius until it looked 
kinda like standard D&D templates. Zone-based cones really just don’t make sense, so they 
aren’t just sloppy under the hood but also really weird: They are just an actual cone of length 
equal to 40 pixels times the length indicated (i.e. “cone 3” is 120 pixels). 
 
In general, radius attacks are the only AoEs that look good on zones-only maps, and even then 
mostly only as radius 0 effects. 
 
Hit and Miss 
 
When an attack hits, it can deal damage, in the format “[expression] [type] damage to [HP]”. For 
example, “2d6+STR slashing damage to Health.” The type has no effect without Rule Scripting 
included. 
 
It can also deal healing, using the format “[expression] [type] healing”. For example, “2d8+WIS 
radiant healing to Health”. As you would expect, this increases the target’s HP instead of 
decreasing it. 
 
It can also cause a counterattack, which is especially useful for systems where NPCs don’t take 
turns of their own, only retaliate when your rolls against them fail. The format for this is “[type] 
Attack against attacker.” For example, “Miss: Melee Attack against attacker” would select the 
first Melee Attack the program can find on the list and automatically roll it against the attacker if 
the attacker missed. 
 
You can also skip the attack/defense expression entirely and have the counterattack auto-hit 
using “[type] Attack hits attacker”, or make it an auto-miss with “[type] Attack misses attacker”. I 
don’t know why you would want missing an attack to cause the target to automatically miss the 
attacker, but it was easy to add after I already had the automatic hit, so it’s an option. 
 
Finally, a hit or miss can cause a status effect using the keywords “inflicts” or “applies”, i.e. “Hit: 
8d6 fire damage and inflicts burning” or “Hit: 4d8 radiant healing and applies haste”. Status 
effect durations can be overridden with the keyword “for”. For example, “Hit: 8d8 fire damage 
and inflicts burning for 1d3 rounds” would override the usual burning duration to have it instead 
last 1d3 rounds, and “Hit: 8d8 fire damage and inflicts burning for DEX Save against caster’s 
Spell Save DC to negate” would cause the status effect to persist until the target made a DEX 
Save that met or exceeded the caster’s (i.e. the token using the attack) Spell Save DC at the 
end of their turn in the initiative. 
 


Status effects only do anything if they’re defined in the Rule Scripting panel, but if you only have 
the vanilla Battle panel, they are gracefully ignored while the rest of the effects of the hit/miss 
are applied. 
 
Hit and Miss work exactly the same as each other except in that one is triggered by the attack 
expression equaling or exceeding the defense expression and the other is triggered by the 
defense expression exceeding the attack expression. This means you can have attacks that 
damage on a hit but heal on a miss or vice-versa, or attacks that deal full damage and inflict a 
status effect on a hit but half damage and no status effect on a miss, and so on. 
 
Cost 
 
A cost decreases the corresponding HP bar or clock by the indicated amount any time the 
attack is attempted, whether it succeeds or fails. For example, if you have “Ki Points (4/4): Flurry 
of blows, step of the wind” defined, and then elsewhere you have “Ki Punch; 1d20 + DEX + WIS 
+ Proficiency against AC, cost 1 ki points. Hit: 1d8+DEX+WIS bludgeoning damage.” This 
means any time you attempt a Ki Punch, you lose 1 ki point from your ki points clock. 
 
StatScript Actions 
 
You can define an action that executes multiple attacks or skill checks. For example, 
“Multiattack. Attack Action: Longsword, Longsword.” This will search for an attack or skill check 
called “Longsword” and run it twice in a row when the Multiattack action is selected. 
 
Rule Scripting Panel 
 
Requirements: NPCs, Battle 
 
Rule Scripting allows you to add global game rules in blocks defined by open and close tags like 
[damageTypes] followed by [/damageTypes]. 
 
Damage and Healing 
 
And the reason why we use blocks with start and end tags is so that damage and healing types 
don’t get confused, although it’s also useful for i.e. factions with damage types named after 
them. 
 
If an attack deals a damage type that’s defined in the damageType block, then it will deal 
modified damage to all tags defined in that damage type. The tags are [damageTypes] and 
[/damageTypes] and the format is: 


 
“[damage type]: 
[damage expressions]”​
 
For example: 
 
“Fire damage: 
*0 damage against fire immunity. 
*0.5 damage against fire resistance. 
*1.5 damage against fire vulnerability. 
-X damage against fire absorption(X). 
-Spell Defense damage against elemental resistance.” 
 
Most of these are self-explanatory, but “-X damage against fire absorption(X)” means that a 
token tagged with “fire absorption(3)” will take -3 fire damage, and “-Spell Defense damage 
against elemental resistance” means that a token tagged “elemental resistance” will reduce fire 
damage by its Spell Defense stat (if it has no Spell Defense stat in its stat block, it will reduce 
the damage by 0, i.e. be ignored). 
 
Healing types work the same way, but are separate so that you can decide whether you want 
“radiant immunity” to mean immune to both radiant damage and radiant healing or to have it 
ignore radiant damage but treat radiant healing normally or to have it double radiant healing or 
what. The radiant damage type and the radiant healing type are fully separate, so you can write 
whatever rules for them you want. 
 
Terrain Types 
 
Tags are [terrainTypes] and {/terrainTypes]. 
 
The format for a terrain type is:​
​
“[terrain type]: 
[Movement expressions] 
[Visibility]” 
 
For example: 
 
“Light forest: 
Run: 2 
Climb: 2​
Fly: 1 
Visibility: Semi-transparent(3)” 
 


Terrains have two factors: Movement and visibility. 
 
Movement 
 
A terrain can have any number of movement types defined. A token that doesn’t have at least 
one of those movement types cannot move through that terrain at all. This means a terrain type 
with no movement types defined is completely impassable. 
 
A movement type can be anything. The program scans the token for a matching variable. For 
example, if the terrain type “grassland” has the movement type “Run: 1” then the program will 
scan tokens for a Run variable and if they have it, it will let them enter grassland. If you pick up 
a token on the Battle canvas and press Q, it will show you how much of each movement type 
you’re spending and prevent you from moving beyond what that token can cross in a single 
move. 
 
Visibility 
 
Visibility can be transparent, opaque, or semi-opaque. Transparent does not block line of sight 
at all. Opaque blocks line of sight immediately. Semi-transparent is followed by a number in 
parentheses (i.e. “Visibility: Semi-transparent(2)”). You can only target a token in 
semi-transparent terrain if the total amount of semi-transparent terrain you’re looking through is 
equal to or lower than the lowest semit-transparency score. 
 
So, if the terrain type “light forest” has “Visibility: Semi-transparent(3)” and “heavy jungle” has 
“Visibility: Semi-transparent(1)”, then you can maintain line of sight through up to 3 squares, 
hexes, or zones of light forest, only into one cell or zone of heavy jungle, and if you tried to 
target a creature in light forest through a zone of heavy jungle, you would be unable to. Your line 
of sight is passing through two semi-transparent zones and the maximum allowance for 
semi-transparent zones in heavy jungle is 1, so even though your target is in light forest, which 
allows 3, and even though you could target enemies in the heavy jungle zone itself, your line of 
sight is blocked by the combination of the light forest and the heavy jungle. 
 
Status Effects and Auras 
 
Status effects use [statusEffects] and {/statusEffects] tags and have the following format: 
 
“[Name]. [Buff/Debuff]: [modifiers]. Duration: [duration]” 
 
Either Buff or Debuff can be used for any status effect. it has no effect, just distinguishes status 
effects from similarly formatted attacks and skill checks. 
 


Modifiers 
 
A status effect can modify a stat with +, -, or *, and can add either a flat value (i.e. “+3 STR”) or 
a value based on the caster’s statblock (i.e. “+caster’s INT STR” will add the caster’s INT to the 
target’s STR). 
 
A status effect can also give “advantage on [type]” or “disadvantage on [type]”, where [type] is 
any type applied to attacks or skill checks, i.e. “advantage on Melee Attacks” or “disadvantage 
on Spell Attacks”. The program will scan the target token for any attacks or skill checks with a 
matching type, find how many dice they roll, and increase or decrease the dice rolled as 
appropriate, dropping the lowest/highest. This means that giving advantage to an attack that 
rolls 3d6 will turn it into 4d6dl1, and adding advantage to an attack that already rolled 4d6dl1 
makes it 5d6dl2. 
 
A status effect can also give “cannot use [type]” which will prevent the use of attacks or skill 
checks with that type altogether, i.e. “Mute. Cannot use Spell Attacks. Duration: 3 rounds”. 
 
A status effect can apply “cannot move”, which will prevent the token from moving (although on 
a zones-only map, tokens with “cannot move” can still move within a zone). 
 
A status effect can apply “cannot do anything,” which combines “cannot move” with a blanket 
“cannot use” preventing any attacks or skill checks of any kind, for a stun effect. 
 
Status effects can also apply DoTs (“Damage over Time”) or HoTs (“Healing over Time”) which 
is applied whenever the token’s turn begins in the initiative order on the Battle panel. This is 
formatted the same way as damage in attack, just using DoTs or HoTs instead of damage or 
healing (i.e. “1d6 fire DoTs to HP.”). 
Duration 
 
Duration can either be a fixed amount of time (i.e. “Duration: 3 rounds.” or “Duration: 1d6 
rounds.”), a save to negate, or a save to persist. 
 
Save to negate is formatted as “Duration: Target’s [save expression] against [TN expression] to 
negate,” for example “Duration: Target’s CON save against caster’s Spell Save DC to negate”. 
This causes the token to automatically roll to save every time its turn ends in the Battle panel’s 
initiative, ending the status effect on success. Save to persist works the same way, except that 
passing the save causes the status effect to continue (presumably it’s beneficial, or maybe the 
save is designed to be stronger against foes who are stronger at something, i.e. a spell that 
uses your own magic power against you so that it is harder to end the higher your Magic stat is). 
 
Factions 
 


Factions use [factions] and [/factions] in the following format: 
 
“[name]:​
Allies: [factions] 
Enemies: [factions]” 
 
For example: 
 
“Tavern: 
Allies: Tavern, town guard​
Enemies: Goblins, demons” 
 
If you press ALT+I, you can inspect which tokens your selected token considers to be an ally or 
enemy. Any tokens that have matching ally tags and no enemy tags are highlighted in green, 
any with enemy tags but no ally tags are highlighted in red, and any which have neither (or both, 
if a token shows up in both ally and enemy tags for one faction or if a token has tags making it 
part of two opposed factions) they show up as blue neutrals. 
 
If a faction has defined allies but no enemies, then all non-allies are their enemies, and 
vice-versa. 
 
Faction allegiance is used to determine valid targets for NPC Scripting, but with only Rule 
Scripting and the Battle panel, all it does is highlight friends vs. enemies using ALT+I. 
 
Dead Tokens 
 
This section is bracketed in [Death] and [/Death] and is used to define when a token is dead so 
that automated NPCs won’t keep attacking dead tokens, nor will dead tokens take turns. It 
doesn’t do anything without NPC Scripting. 
 
The format is “Dead at [condition]”, i.e. “Dead at 0 HP” or “Dead at 5 or more wounds”. The 
program recognizes both “or more” and “or less” as well as >, <, >=, and <=. Any token that 
meets any of the defined death conditions will be considered dead for purposes of NPC 
scripting. 
 
NPC Scripting Panel 
 
Requirements: NPCs, Battle, Rule Scripting 
 
An NPC script can be created in this panel and assigned to a token in the Battle panel. You can 
also assign default NPC scripts to NPC cards, in which case that script will be assigned to every 
token created from that card. 


 
NPC scripts have two sections, marked by block tags. 
 
Doctrine 
 
Marked by [Doctrine] and [/Doctrine]. 
 
Doctrine determines how the NPC picks specific tactics to employ. The program picks the first 
tactic in the list whose prerequisites are met. If the program makes it to the bottom of the 
doctrine section without any tactic meeting its prerequisites, it picks one at random. 
 
You can create an index of tactics, for example: 
 
“1-2 Aggression 
2-5 Caution 
6 Ultimate” 
 
You can then create an instruction like “Roll 1d6” which will then roll 1d6, picking Ultimate on 6, 
Caution on 3-5, Aggression on 1, and picking randomly between Aggression and Caution (but 
not Ultimate) on a 2, since the ranges overlap. 
 
You can also increase or decrease variables on the target token, i.e. “Roll 1d6 and add 1 
momentum” or “Roll 1d6 and subtract 1 momentum”. You can then use these variables for 
tracking countdowns, for example: 
 
“1-3 Aggression 
4-6 Caution 
If momentum is 5, use Ultimate and subtract 1 momentum. 
Roll 1d6 and add 1 momentum.” 
 
This doctrine causes the token to randomly pick between Aggression and Caution for 5 turns. 
On the 6th turn, momentum is 5, so it uses the Ultimate tactic. Using the Ultimate tactic only 
subtracts 1 momentum, so once the token uses its first Ultimate, it will then use its Ultimate 
every other round. 
 
You can also make conditional statements based on stats from the token’s statblock that aren’t 
directly affected by doctrine, i.e. “If Health is less than 25%, use Cautious.” You can use 
non-percentages, but especially for HP bars, using a percentage means the same NPC script 
can be used for any NPC with the same personality and/or fighting style and it will remain valid 
even if they have significantly different stats. 
 
Instead of selecting a tactic, you can also switch to a different script entirely using the “switch to” 
keyword, i.e. “if Health is less than 25%, switch to Berserker”. 


 
Script switching and indices can be used together to create enemies that change their approach 
intelligently based on the situation, but still act with some amount of randomness so that they 
don’t have easily predicted and exploited attack patterns. For as powerful as these scripts are, 
however, I recommend keeping them pretty simple and just using a 1d6 or 1d8 index with a total 
of 3 or 4 different tactics, both because this makes the scripts better able to be used on many 
different NPCs and because designing an (seemingly) intelligent script with situational 
awareness and a wide variety of different tactical approaches based on the circumstances of the 
battle is also going to require you to then balance that encounter, which means you will have to 
fight it multiple times and finetune the difficulty. If you’re a third-party publisher planning on 
selling this, that makes sense, but if this is for personal use, it does not, particularly. 
 
Tactics 
 
A “tactic” is a collection of specific commands executed in order, packaged together into a single 
option that can be selected by the doctrine. It doesn’t matter what order you write your tactics in. 
 
Movement Commands 
 
Movement commands are formatted as “Move to [target].” or “Move to within [type] range of 
[target].” 
 
Target 
 
Valid targets are: 
 
Random enemy: Selects completely randomly from amongst tokens recognized as an “enemy” 
by faction scripting. 
Nearest enemy: Whichever enemy requires the least movement to reach, breaking ties 
randomly. 
Biggest enemy: The enemy who is largest as measured by token size. Useful for wild animals or 
dim-witted thugs who measure the strength of things purely by how big they are. 
Smallest enemy: The enemy who is smallest as measured by token size. 
Strongest([metric]) enemy: The “metric” by which you determine strength can be any stat. For 
example, “Strongest(HP) enemy” means the enemy with the most HP. You can use this to make 
scripts that focus fire on enemies with powerful unchanging stats like “Strongest(level)” or 
enemies which spread their damage around using “Strongest(HP)”. 
Weakest([metric]) enemy: Since this targets the enemy with the lowest metric, you can use it for 
scripts who fish for enemy casters by targeting enemies with low AC, or who try to finish off 
enemies with low HP, or who pick on enemies with the lowest level or proficiency bonus. 
 


For both “strongest” and “weakest” you can create special stats that are only used by NPC 
scripts like “visible armor” where plate is 8 and chainmail is 6 and studded leather is 2, so NPCs 
will pick targets based on how much armor they can see but will get fooled by things like Monks 
who are very tanky for how much armor they wear. 
 
Instead of targeting an enemy, you can also target an ally, i.e. “move to weakest(HP) ally” for a 
healer trying to set up a limited range healing move like Cure Wounds, “neutral” which you can 
use in combination with doctrine to create murderous brigands who prioritize attacking enemy 
tokens but will target neutrals if they can’t find any threats (kind of a narrow use-case since you 
probably don’t want to use strict turn order and combat rules to process what happens to the 
neutral tokens after the good guys are defeated - surely the combat is over by then - but it was 
easy to program in neutral targeting once I already had neutrals defined, so maybe you can find 
a use for it), and “any token” which, as the name implies, will ignore faction completely. 
 
You can also have a command directly target a specific tag, i.e. “move to nearest elf”. Even if 
“elf” isn’t a defined faction, the token will move to the nearest token tagged as “elf”. It’s 
recommended you use the generic “ally” and “enemy” because this makes the script more 
flexible, something you can add to any token of the right temperament. 
 
Move Within Range 
 
When a token is instructed to move within range of a certain attack, it will examine its statblock 
for any attack with that exact name, and then for the first listed attack that has that type. If it 
finds something, it will move to within range of the target using that weapon. The format for this 
is: 
 
“Move to within [type] range of [target].” 
 
For example: 
 
“Move to within Ranged Attack range of weakest(armor) enemy.” 
 
This will scan the token for an attack literally called “Ranged Attack” and, if it can’t find one 
(likely), it will instead scan the token for an attack given the type of “Ranged Attack”. It will read 
the range of that attack and then try to move to within range of that attack. This means you can 
have the same script on a token with a range 1 shortbow and a token with a range 3 longbow 
and they’ll both act intelligently (at least in the sense of not wasting time getting extremely close 
or stopping far outside range of their longest usable attack) with regards to their statblock. 
 
Attack Commands 
 
Attacks use the format “Attack [target]” or “[type] [target]”. For example: “Melee Weapon Attack 
nearest enemy.” 


 
“Attack” will simply use the first attack the program finds in the statblock, read from top to 
bottom. Picking a specific type, like Ranged Weapon Attack or Melee Weapon Attack, will cause 
the program to use the first attack of that type it can find. 
 
Targets work the same for attacks as they do for movement. 
 
Magic Chronicle Version History 
 
1.0.0 
 
-Initial release. 
 
1.0.1 
 
-Windows version unchanged, but critical update to the Mac version in that it, uh, functioned at 
all. 
 
1.0.2 
 
-Made dev and prod versions of the program save to separate storage folders so they wouldn’t 
crush each other’s auto-saves. Never released to the public. 
 
1.0.3 
 
-Added name, portrait, and description to Character Sheet on user suggestion. 
 
1.1.0 
 
-Converted Character Sheet to StatScript and changed the guts of the program a bunch in 
anticipation of the release of the Battle Panel. 
 
-Accidentally broke the Battle Grid. 
 
1.1.1 
 
-Fixed the Battle Grid. 
 
-Rewrote a bunch of stuff so that the Expanded panels could be torn out to make the free Magic 
Chronicle Apprentice version and could also be readded as DLC to allow for piecemeal 
upgrades to the full Magic Chronicle. 
 


-Fixed that bug where adding 5 or more inventory slots would make the inventory image change 
size. 


