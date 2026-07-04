# Using Architectural Properties to Model and Measure.pdf

Using Architectural Properties to Model and Measure
System-Wide Graceful Degradation
ABSTRACT
System-wide graceful degradation may be a viable approach to
improving dependability in computer systems.  In order to evaluate
and improve system-wide graceful degradation we present initial
work on a component-based model that will explicitly define
graceful degradation as a system property, and measure how well a
system gracefully degrades in the presence of multiple
combinations of component failures.  The system’s software
architecture plays a major role in this model, because the interface
and 
component 
specifications 
embody 
the 
architecture’s
abstraction principle.  We use the architecture to group components
into subsystems that enable reasoning about overall system utility. 
We apply this model to an example distributed embedded control
system and report on initial results.
1. INTRODUCTION
De pend abil ity is a term that cov ers many sys tem prop er ties such as
re li abil ity, avail abil ity, safety, main tain abil ity, and se cu rity [4]. 
Sys tem de pend abil ity is es pe cially im por tant for em bed ded com -
puter con trol sys tems, which per vade ev ery day life and can have se -
vere con se quences for failure.  These sys tems in creas ingly
im ple ment a sig nif i cant portion of their func tion al ity in soft ware,
mak ing soft ware de pend abil ity a ma jor is sue.
Grace ful deg ra da tion may be a vi a ble ap proach to achiev ing better
soft ware de pend abil ity.  If a soft ware sys tem can grace fully de grade 
au to mat i cally when faults are de tected, then in di vid ual soft ware
com po nent fail ures will not cause com plete sys tem fail ure.   Rather,
com po nent fail ures will re move the func tion al ity de rived from that
com po nent, while still pre serv ing the op er a tion of the rest of the
sys tem.  Spec ifying and achiev ing sys tem-wide grace ful deg ra da -
tion is a dif fi cult re search prob lem.  Cur rent ap proaches re quire
spec i fy ing ev ery sys tem fail ure mode ahead of time, and de sign ing
a spe cific re sponse for each such mode (e.g., [2]).  This is im prac ti -
cal for a com plex soft ware sys tem, es pe cially a fine grained dis trib -
uted em bed ded sys tem with hun dreds or thou sands of soft ware and
hard ware com po nents.
In or der to eval u ate and im prove sys tem-wide grace ful deg ra da tion, 
we pres ent a com po nent-based sys tem model that pro vides a means
for eval u at ing and pre dict ing how well a sys tem should grace fully
de grade, as well as how grace ful deg ra da tion in flu ences de pend -
abil ity prop er ties.  We base the model on us ing the sys tem’s in ter -
face definitions and com po nent con nec tions to group the sys tem’s
com po nents into sub sys tems.  We hy poth e size that the soft ware ar -
chi tec ture, re spon si ble for the over all or ga ni za tion of and con nec -
tions among com po nents, can fa cil i tate the sys tem’s abil ity to
im plic itly provide the prop erty of grace ful deg ra da tion, with out
spec i fy ing a re sponse to each pos si ble fail ure mode at de sign time. 
We de fine a fail ure mode to be a set of sys tem com po nents fail ing
con cur rently.  By us ing the model to mea sure how gracefully a sys -
tem de grades, we pre dict that we can iden tify what ar chi tec tural
prop er ties fa cil i tate and im pede sys tem-wide grace ful deg ra da tion.
Re lated to our con cept of grace ful deg ra da tion is the term sur viv -
abil ity.  Sur viv abil ity is an other prop erty of de pend abil ity that has
been pro posed to ex plic itly de fine how sys tems will de grade func -
tion al ity in the pres ence of fail ures [3].  Our work dif fers from sur -
viv abil ity specifications in that we are in ter ested in build ing
im plicit grace ful deg ra da tion into sys tems with out spec i fy ing fail -
ure sce nar ios a pri ori, and hav ing the sys tem “do the right thing” in
the pres ence of com po nent fail ures.  Also, we are fo cus ing on dis -
trib uted em bed ded sys tems rather than on large-scale crit i cal in fra -
struc ture in for ma tion sys tems.
The re main der of this pa per is or ga nized as follows.  Sec tion 2 de -
scribes our ini tial sys tem model and key as sump tions.  Sec tion 3 de -
scribes our rep re sen ta tive dis trib uted em bed ded sys tem and its
ar chi tec ture, and ap plies our model to this ar chi tec ture.  Sec tion 4
in cludes dis cus sion about the model’s pre dic tions, and how they
com pare to ini tial fault in jec tion tests we ran with a sim u lated ver -
sion of the con trol sys tem.  Sec tion 5 wraps up with con clu sions and 
fu ture work.
2. SYSTEM MODEL
As a first step, we are con cen trat ing on soft ware ar chi tec ture at a
high level of ab strac tion.  Our sys tem model ini tially fo cuses on the
“func tion al ity” com po nents of the sys tem: soft ware, sen sors, and
ac tu a tors.  We make the ini tial as sump tions that in di vid ual soft ware
com po nents each have their own pro cess ing el e ments, that there is
enough net work band width to trans mit all needed sen sor val ues,
and that there are enough sys tem re sources to sat isfy real-time re -
quire ments.  These sys tem as pects will all in flu ence sys tem-wide
grace ful deg ra da tion, but we are plan ning to in clude them in the
model at later stages.
We con sider a sys tem as a set of soft ware, sen sor, and ac tu a tor com -
po nents.  We use the in ter faces among com po nents to de fine a set of
sys tem vari ables through which all com po nents com mu ni cate. 
These vari ables can rep re sent any com mu ni ca tion struc ture in the
Charles P. Shelton
ECE Department
Carnegie Mellon University
Pittsburgh, PA, USA
cshelton@cmu.edu
Philip Koopman
ECE Department
Carnegie Mellon University
Pittsburgh, PA, USA
koopman@cmu.edu


soft ware im ple men ta tion.  Ac tu a tors re ceive in put vari ables and
out put to the en vi ron ment, while sen sors re ceive in put from the en -
vi ron ment and out put sys tem vari ables.   We as sume that com po -
nents can ei ther be in one of two states: work ing or failed.  Working
means that the com po nent has enough re sources to out put its spec i -
fied sys tem vari ables.  Failed means the com po nent can not pro duce
its spec i fied out puts.
The fault model for our sys tem uses the tra di tional fail-fast, fail si -
lent as sump tion.  All faults are man i fested as the loss of sys tem vari -
able com mu ni ca tion among com po nents.  Com po nents ei ther
pro vide their out put vari ables or do not.  Thus, fail ures can be de -
tected when com po nents do not pro vide their out puts when spec i -
fied.  This does not ac count for more com plex types of fail ures such
as pro vid ing in valid but syn tac ti cally cor rect in for ma tion, and as -
sumes com po nent fail ures can be quickly de tected.  Fault de tec tion
and prop a ga tion is sues are chal leng ing re search ar eas in and of
them selves, and are out side the scope of this work.  Ad di tionally,
since soft ware com po nent fail ure rates are dif fi cult to iden tify, we
make an ini tial as sump tion that all com po nents have ap prox i mately
equal fail ure rates.
A key con cept in our model is the no tion of util ity.  Util ity is a mea -
sure of how much ben e fit can be gained from the en tire sys tem, a
cer tain sub sys tem, or an in di vid ual com po nent.  For the en tire sys -
tem, the over all util ity is de ter mined by a non lin ear func tion of its
in di vid ual sub sys tem util i ties.  Each sub sys tem’s util ity is de ter -
mined by a non lin ear func tion of its in di vid ual com po nent util i ties. 
For in di vid ual com po nents, we de fine a com po nent’s util ity to be 1
when work ing and 0 when failed.  We as sume that if all com po nents
are work ing the sys tem will be at its max i mum util ity, and if all
com po nents are failed, the sys tem will have an over all util ity of
zero.  Thus, a sys tem grace fully de grades if in di vid ual com po nent
and sub sys tem fail ures re duce sys tem util ity grad u ally.
In our model, we ini tially con cen trate on mea sur ing whether the
sys tem has zero or pos i tive over all util ity by iden ti fy ing how re sis -
tant crit i cal sub sys tems are to com po nent fail ures.  De ter mining the
func tions that quan ti ta tively mea sure how work ing com po nents im -
prove sub sys tem and sys tem util ity val ues is a chal leng ing prob lem.  
How ever, with out know ing these func tions we can ini tially make a
dis tinc tion be tween a sys tem that is work ing and has pos i tive but
not nec es sar ily max i mum util ity, and a failed sys tem that has zero
util ity.  In or der to make this dis tinc tion we must have a clear def i ni -
tion of what “work ing” means for the en tire sys tem.  In other words,
we must spec ify what fea tures of the sys tem are nec es sary for the
sys tem to com plete its pri mary func tions.  In most cases, this is not
all the fea tures avail able in the sys tem.  For ex am ple, the pri mary
func tion of a car is to pro vide trans por ta tion.  Crit i cal fea tures nec -
es sary for the car to con tinue work ing in clude en gine and trans mis -
sion con trol, brakes, and steer ing.  The power win dows, emis sions
con trol, air con di tion ing, and ra dio pro vide aux il iary func tion al ity
not nec es sary for the car to com plete its pri mary task, and can be
lost with out caus ing a cat a strophic fail ure.  
The sys tem can have many dif fer ent com po nent con fig u ra tions
based on which com po nents are work ing or failed.  If n is the num -
ber of com po nents in the sys tem, then there are 2n dif fer ent con fig u -
ra tions that can be con sid ered.  The sys tem’s com po nent
con fig u ra tion de ter mines the util ity of all its sub sys tems, and thus
the util ity of the en tire sys tem.  An ide al grace fully de grad ing sys -
tem is one where a large frac tion of these 2n con fig u ra tions re sult in
a sys tem with over all pos i tive util ity; i.e., the sys tem can tol er ate
mul ti ple com bi na tions of com po nent fail ures and still pro vide use -
ful func tion al ity.
Our first met ric for grace ful deg ra da tion is the sys tem’s re sis tance
to com plete fail ure (zero sys tem util ity).  We de ter mine this value
by look ing at how many con fig u ra tions re sult in a sys tem with pos i -
tive util ity.  The ra tio of log2 [num ber of valid com po nent con fig u ra -
tions] / n gives a mea sure of how many con fig u ra tions will pro vide
util ity rel a tive to the to tal num ber of sys tem con fig u ra tions.  This
value is 0 (only one valid con fig u ra tion) for a brit tle sys tem, and 1
for a per fect sys tem where any com po nent con fig u ra tion can pro -
vide some util ity (ig nor ing the triv ial con fig u ra tion of zero com po -
nents that re sults in no sys tem at all).
Clearly, if we had to con sider the util ity of ev ery pos si ble com po -
nent con fig u ra tion in di vid u ally, then specifying grace ful deg ra da -
tion be comes ex po nen tially dif fi cult as the num ber of com po nents
in creases.  How ever, we can use the sys tem’s soft ware ar chi tec ture,
which de fines sys tem soft ware com po nents, in put and out put in ter -
faces, and con nec tions among components, to group com po nents
into sub sys tems ac cord ing to the sys tem variables they pro vide, and
thus re duce complexity.
We de fine these sub sys tems in our com po nent model as fea ture sub -
sets.  A fea ture sub set is a set of com po nents (soft ware com po nents,
sen sors, ac tu a tors, and pos si bly other fea ture sub sets) that work to -
gether to pro vide a set of out put vari ables.  Fea ture sub sets may or
may not be dis joint and can share com po nents across dif fer ent sub -
sets.  Fea ture sub sets have util ity val ues based on which of their
com po nents are work ing, and con trib ute to over all sys tem util ity.  A
fea ture sub set is crit i cal if its func tion al ity is re quired by the sys tem; 
i.e., the to tal sys tem util ity is zero when ever any crit i cal fea ture sub -
set has zero util ity.  Thus, the sys tem will have pos i tive util ity if and
only if all of its crit i cal fea ture sub sets have pos i tive util ity.  If we
view the sys tem as a set of fea ture sub sets rather than in di vid ual
com po nents, then we should only need to con sider valid com po nent
con fig u ra tions of crit i cal fea ture sub sets rather than con fig u ra tions
of all sys tem com po nents to de ter mine how well the sys tem grace -
fully de grades.
In ad di tion to group ing com po nents into fea ture sub sets, we de fine a 
set of de pend ency re la tion ships be tween fea ture sub sets and their
com po nents.  A fea ture sub set may have strong de pend ence on
some of its com po nents, weak de pend ence on oth ers, and some of
its com po nents may be com pletely op tional.  A fea ture sub set
strongly de pends on one of its com po nents if the loss of that com po -
nent re sults in the fea ture sub set’s hav ing zero util ity.  A fea ture sub -
set weakly de pends on one of its com po nents if the loss of that
com po nent re duces the fea ture sub set’s util ity to zero in some, but
not all, con fig u ra tions in which that com po nent was working.  For
ex am ple, if there are two com po nents that out put a re quired sys tem
vari able, loss of both will re sult in the fea ture sub set hav ing zero
util ity, but loss of only one or the other will not.  If a com po nent is
op tional to a fea ture sub set, then it may pro vide en hance ments to
the fea ture sub set’s util ity, but is not crit i cal to the op er a tion of the
fea ture sub set.  Ev ery valid com po nent con fig u ra tion of the fea ture
sub set where that com po nent is work ing still pro vides pos i tive (but
pos si bly lower) util ity when that com po nent is bro ken.  These de -
pend ency re la tion ships can also ex ist among in di vid ual com po -
nents as well, based on their in put and out put in ter faces.  A
com po nent that re quires a cer tain sys tem vari able as an in put will
de pend on the com po nents that pro vide it as an out put.
We can use this model to de velop a space of sys tems with vary ing
de grees of grace ful deg ra da tion.  At one end of the spec trum, we
have ex tremely “brit tle” sys tems that are not ca pa ble of any grace -
ful deg ra da tion at all.  In these sys tems, any one com po nent fail ure
will re sult in a com plete sys tem fail ure.  In our model, this would be
a sys tem where ev ery com po nent is within a crit i cal fea ture sub set,


and each fea ture sub set strongly de pends on all of its com po nents. 
There fore, ev ery com po nent must be func tion ing to have pos i tive
sys tem util ity.
Sim i larly, any mod u lar re dun dant sys tem can be rep re sented as a
col lec tion of sev eral crit i cal fea ture sub sets, where each fea ture sub -
set con tains mul ti ple cop ies of a com po nent plus a voter.  The valid
con fig u ra tions that pro vide pos i tive util ity for each fea ture sub set
are those that contain the voter plus one or more com po nent cop ies. 
This re dun dant sys tem can tol er ate mul ti ple fail ures across many
fea ture sub sets, but can not tol er ate the fail ure of any one voter or all
the com po nent cop ies in any one fea ture sub set.
At the other end of the spec trum, an ideal grace fully de grad ing sys -
tem is one where any com bi na tion of com po nent fail ures will still
leave a sys tem with pos i tive util ity.  In our model, this sys tem would 
be one where none of its fea ture sub sets would be la beled as crit i cal, 
and ev ery com po nent would be com pletely op tional to each fea ture
sub set in which it was a mem ber.  The sys tem would con tinue to
have pos i tive util ity un til ev ery com po nent failed.
3. EXAMPLE SYSTEM: A DISTRIBUTED
ELEVATOR CONTROL SYSTEM
To il lus trate how we can ap ply our sys tem model to a con trol sys -
tem, we will use a model of a rel a tively com plex dis trib uted el e va -
tor con trol sys tem.  The com plete de tails of the model have been
pub lished in [6], but we will de scribe a por tion of the sys tem and the 
soft ware ar chi tec ture here for clar ity.
The gen eral re quire ment for an el e va tor is that it must safely trans -
port peo ple among floors in a build ing.  The con trol sys tem has a set
of sen sors (door opened/closed, el e va tor speed, but ton sen sors, etc.) 
for de ter min ing the cur rent en vi ron ment and pas sen ger re quests, a
set of ac tu a tors (door mo tor, drive mo tor, emer gency brake, lights,
etc.) for per form ing tasks and in form ing pas sen gers about sys tem
state, and a set of soft ware ob jects (door con trol ler, drive con trol ler,
dis patcher, etc.) that im ple ment the con trol logic to per form the el e -
va tor’s func tions.
Ta ble 1 sum ma rizes the list of sen sors, ac tu a tors, and soft ware com -
po nents in the el e va tor con trol sys tem.  In the ta ble, f rep re sents the
num ber of floors in the el e va tor’s build ing, and d rep re sents a
choice of two di rec tions, up or down.  For ex am ple, there are f floor
sen sors and f car but ton sen sors (one for each floor), two hoistway
limit sen sors (the “up” sen sor is at the top of the hoistway, and the
“down” sen sor is at the bot tom), and 2f - 2 hall but ton sen sors (two
per floor in each di rec tion, ex cept for the top and bot tom floors,
which only have one but ton).  In the ta ble each sen sor has a spec i -
fied out put vari able, and each ac tu a tor has a spec i fied in put vari -
able.  The soft ware com po nents have sev eral in puts and a few
out puts.  There are a to tal of 14 + 11f com po nents in the sys tem.
The sys tem’s soft ware ar chi tec ture de fines each com po nent’s in put
and out put in ter face, as well as con nec tions among com po nents,
which can be used to con struct the sys tem’s fea ture sub sets.  Fig ure
1 shows the crit i cal fea ture sub sets of the sys tem, and the de pend en -
cies be tween the fea ture sub sets and com po nents.  Each ar row in the 
fig ure rep re sents a sys tem vari able be ing com mu ni cated be tween
com po nents.  In an el e va tor con trol sys tem, the only crit i cal func -
tions of the el e va tor are that it must be able to ser vice all floors, open 
and close the doors, and en sure the safety of the pas sen gers.  All
other func tion al ity, such as re spond ing to pas sen ger re quests, pro -
vid ing pas sen ger feed back, and min i miz ing wait time and travel
time, are en hance ments over the ba sic el e va tor re quire ments. 
There fore, the crit i cal fea ture sub sets for this sys tem are only the
fea ture sub sets that are re quired to op er ate the drive mo tor, door
mo tor, and emer gency brake ac tu a tors.
The soft ware components are de signed to have a de fault be hav ior
based on their re quired in puts, and to treat op tional in puts as “ad -
vice” to im prove func tion al ity when those in puts are avail able.  For
ex am ple, the Door Con trol and Drive Con trol com po nents can lis -
ten to each other’s com mand out put vari ables in ad di tion to the
Drive Speed and Door Closed sen sors to syn chro nize their be hav ior
(open the doors more quickly af ter the car stops), but only the sensor 
val ues are nec es sary for cor rect be hav ior.  Likewise, the Drive Con -
trol com po nent has a de fault be hav ior that stops the el e va tor at ev -
ery floor, but if the DesiredFloor vari able is avail able from the
Dis patcher com po nent, then it can use that value to skip floors that
do not have any pend ing re quests.  Also, the Door Con trol com po -
nent nor mally opens the door for a spec i fied dwell time, but can re -
spond to but ton presses to re open the doors if a pas sen ger ar rives. 
We also enu mer ated the other non-crit i cal fea ture subsets in the el e -
va tor sys tem such as the var i ous pas sen ger feed back lights in the el -
e va tor, but we omit them here for the sake of brev ity.
4. ANALYSIS
In or der to de rive the grace ful deg ra da tion met ric for our el e va tor
con trol system, we need only con sider the crit i cal fea ture sub sets
and the com po nents upon which they de pend.  There fore, all con fig -
u ra tions con tain ing enough com po nents to pro vide work ing Drive
Sen sor Type
#
Out put Vari able
Ac tu a tor Type
#
In put Vari able
Soft ware Com po nent
#
Out put Vari able
DriveSpeed
1
DriveSpeed
Drive Motor
1
DriveMotor
Drive Control
1
DriveMotor
CarPosition
1
CarPosition
Door Motor
1
DoorMotor
Door Control
1
DoorMotor
AtFloor
f
AtFloor[f]
Emer gency Brake
1
EmergencyBrake
Safety
1
EmergencyBrake
HoistwayLimit
2
HoistwayLimit[d]
Car Lanterns
2
CarLantern[d]
Dispatcher
1
DesiredFloor
DoorClosed
1
DoorClosed
Car Po si tion Indicator
1
CarPositionIndicator
Vir tualAtFloor
f
AtFloor
DoorOpened
1
DoorOpened
Car But ton Lights
f
CarLight[f]
Lan tern Control
2
CarLantern[d]
DoorReversal
1
DoorReversal
Hall But ton Lights
2f-2
HallLight[f,d]
Car Po si tion In di ca tor Control
1
CarPositionIndicator
Car Buttons
f
CarCall[f]
Car But ton Control
f
CarLight[f]
Hall Buttons
2f-2
HallCall[f,d]
Hall But ton Control
2f-2
HallLight[f,d]
Table 1.  Sensors, Actuators, and Software Components in the Elevator Architecture


Con trol, Door Con trol, Safety, and AtFloor fea ture sub sets are
valid, and can con tain any ar bi trary com bi na tion of other optional
sys tem com po nents.  There are 1 + 9f optional sys tem com po nents
(which can be ar ranged in 21 + 9f dif fer ent ar bi trary com bi na tions),
leav ing 13 + 2f crit i cal com po nents (com po nents within crit i cal fea -
ture sub sets) that have con fig u ra tions that re quire ex am in ing (and
213 + 2f  com po nent com bi na tions left to con sider in di vid u ally).
By ex am in ing the crit i cal fea ture sub sets, we can see that they are
strongly de pend ent on the Drive Speed, Door Closed, Door Opened, 
Door Re ver sal, and Hoistway Limits sen sors, the Drive Con trol,
Door Con trol, and Safety soft ware com po nents, and the Drive Mo -
tor, Door Mo tor, and Emer gency Brake ac tu a tors.  Any valid con -
fig u ra tion must have all of these twelve com po nents pres ent. 
There fore, we can re strict the num ber of con fig u ra tions we cal cu -
late by not con sid er ing any con fig u ra tions in which these com po -
nents are bro ken.
This leaves 1 + 2f com po nents (the Car Po si tion sen sor, the AtFloor
sen sors, and the VirtualAtFloor soft ware com po nents) in the
AtFloor fea ture sub set to be con sid ered.  By ex am in ing the crit i cal
fea ture subsets, we have sys tem at i cally re duced the grace ful deg ra -
da tion cal cu la tion from con sid er ing 214 + 11f com bi na tions to 21 + 2f
com bi na tions.  Now we can de ter mine the num ber of valid con fig u -
ra tions for the AtFloor fea ture by not ing that all floors must be ser -
viced by the el e va tor.  There fore, on each floor there must be a
work ing AtFloor sen sor or a work ing VirtualAtFloor com po nent
with a work ing Car Po si tion sen sor.  If the Car Po si tion sen sor
breaks, then all AtFloor sen sors must work.  Since all the AtFloor
sensors must work in this sit u a tion, they are fixed and have one con -
fig u ra tion.  How ever, the VirtualAtFloor com po nents can ei ther
work or not work since their fail ure will not af fect the avail abil ity of
the AtFloor sys tem variables, making 2f valid com bi na tions for the
various VirtualAtFloor com po nents.  If the Car Po si tion sen sor
work s, then one or both AtFloor sen sor and VirtualAtFloor com po -
nent must work for each floor, so the only in valid com bi na tions are
when both have failed for at least one floor.  This means there are 3
valid com bi na tions per floor, mak ing 3f valid com bi na tions out of
the pos si ble 22f.  Thus there are 2f + 3f valid com bi na tions of com po -
nents in the AtFloor fea ture sub set.
Mul ti plying this with the num ber of com bi na tions of optional com -
po nents re sults in a to tal of (2f + 3f)(21 + 9f) valid com po nent con fig -
u ra tions.  Taking the base 2 log of this and di vid ing it by the to tal
num ber of sys tem com po nents (14 + 11f) gives us our grace ful deg -
ra da tion met ric.  If we cal cu late this value for an el e va tor that serves 
seven floors, we get 0.83.
For com par i son, we also con sider an el e va tor sys tem that does not
con tain any VirtualAtFloor soft ware 
com po nents.  The
VirtualAtFloor com po nents im proved the sys tem’s abil ity to grace -
fully de grade be cause they pro vided a way to com pen sate for
AtFloor sen sor fail ures by us ing in for ma tion pro vided by other sys -
tem sen sors to syn thesize AtFloor sen sor values.  There fore, if we
re move the VirtualAtFloor com po nents, the re sul tant sys tem should 
also re ceive a lower grace ful deg ra da tion value.
In our model, the re moval of the VirtualAtFloor com po nents re -
duces the AtFloor fea ture sub set to be ing strongly de pend ent on all
of the AtFloor sen sors.  There fore there is only one valid con fig u ra -
tion for the AtFloor fea ture sub set in which ev ery AtFloor sen sor
must work.  Since this is a crit i cal fea ture sub set, all valid sys tem
con fig u ra tions must con tain a work ing AtFloor fea ture sub set.  Ad -
di tionally, the Car Po si tion sen sor be comes an op tional sys tem com -
po nent be cause the AtFloor fea ture sub set no lon ger de pends on it. 
This re sults in there be ing only 22 + 9f valid sys tem con fig u ra tions
since most of the com po nents in the crit i cal fea ture sub sets must
work and only the op tional com po nents can have mul ti ple valid
con fig u ra tions.  The to tal num ber of sys tem com po nents is also re -
duced by the re moval of the f VirtualAtFloor com po nents, leav ing
14 + 10f to tal sys tem com po nents.  For a seven-floor el e va tor, this
re sults in a grace ful deg ra da tion score of 0.77.
The grace ful deg ra da tion met ric pro vides a con crete com par i son
among sim i lar sys tems.  We can quan ti ta tively as sess how add ing or 
sub tract ing com po nents to the sys tem af fects its abil ity to grace fully 
de grade.  How ever, this met ric may be mis leading when com par ing
two sys tems that are substantially dif fer ent in terms of func tion al ity
and num ber and type of sys tem com po nents.
We have de vel oped a dis crete event sim u la tor that im ple ments our
el e va tor ar chi tec ture, and have run some ini tial fault in jec tion ex -
Drive Motor
Drive Control
Feature
Drive Control
Component
Door Control
Feature
At Floor
Feature
Desired Floor
Feature
Drive
Speed
Door
Closed
Car
Position
Door Motor
Drive Control
Feature
Door Control
Component
Door Control
Feature
At Floor
Feature
Desired Floor
Feature
Drive
Speed
Door
Closed
Door
Reversal
Door
Opened
Hall Buttons
Feature
Car Buttons
Feature
At Floor
Feature
Drive
Speed
At Floor
Sensors
Car
Position
Virtual At Floor
Components
At Floor
Feature
Drive
Speed
Door
Closed
Hoistway
Limits
Safety
Feature
Safety
Component
Emergency Brake
Sensor
Feature Subset
Software Component
Actuator
Strong Dependence (Necessary for all configurations)
Weak Dependence (Necessary for some configurations)
Optional (Provides non-critical utility enhancement)
Diagram uses multiple identical components in different
places for clarity.  Components/Feature subsets with the same
name actually represent only one component or feature subset
in the system.
Optional feature subsets not shown:
Car Button Lights, Hall Button Lights, Car Position Indicator,
Car Lanterns
Car Button
Sensors
Hall Button
Sensors
Figure 1.  Critical Feature Subsets in the Elevator Control System


per i ments to eval u ate whether the im ple mented sys tem ac tu ally
grace fully degrades.  So far, ev ery test we have run with one of the
pos si ble valid con fig u ra tions was able to suc cess fully de liver all
pas sen gers to their des ti na tion floors, in clud ing a test that fail ed all
com po nents but the crit i cal ones and the AtFloor sen sors.
5. CONCLUSIONS AND FUTURE WORK
We have dem on strated a com po nent-based sys tem model that can
pro vide in sight into how well a sys tem will per form grace ful deg ra -
da tion in the pres ence of mul ti ple com po nent fail ures.  We de vel -
oped an ini tial met ric for grace ful deg ra da tion that in di cates how
many com bi na tions of com po nent fail ures can be tol er ated by ex -
am in ing crit i cal sub sys tem con fig u ra tions rather than con sid er ing
ev ery pos si ble sys tem com po nent con fig u ra tion.  In some ini tial ex -
per i ments on a sim u lated im ple men ta tion of the ex am ple con trol
sys tem stud ied, we found that the ar chi tec ture de scribed was re sis -
tant to cer tain com bi na tions of com po nent fail ures, as pre dicted by
the model.
We did not incorporate fail ure re cov ery sce nar ios for ev ery pos si ble
com bi na tion of com po nent fail ures, but rather built the soft ware
com po nents to the ar chi tec tural spec i fi ca tion.  The in di vid ual com -
po nents were designed to ig nore op tional in put vari ables when they
were not avail able and fol low a de fault be hav ior.  This is a fun da -
men tally dif fer ent ap proach to sys tem-wide grace ful deg ra da tion
than spec i fy ing all pos si ble fail ure combinations to be han dled
ahead of time.
Prop erties of the soft ware ar chi tec ture such as the com po nent in ter -
faces and the iden ti fi ca tion and par ti tion ing of crit i cal sys tem func -
tion al ity from the rest of the sys tem seem to be key to achiev ing
sys tem-wide grace ful deg ra da tion.  The model we de vel oped il lus -
trates how well a sys tem can grace fully de grade by us ing the soft -
ware ar chi tec ture’s com po nent connections to de com pose the
sys tem.  We are also ex plor ing how to use an ar chi tec tural de scrip -
tion lan guage such as Acme [1] to pro vide rig or ous com po nent in -
ter face spec i fi ca tions and fa cil i tate de vel op ment of our sys tem
model.
For this par tic u lar sys tem, it is rel a tively easy to cal cu late the pos si -
ble valid con fig u ra tions by ex am in ing the soft ware ar chi tec ture
with out the model.  How ever, the model pro vides a sys tem atic
frame work for par ti tion ing the sys tem based on its soft ware ar chi -
tec ture,  and we hy poth e size that it will be use ful in eval u at ing any
ar chi tec tural spec i fi ca tion that has a well-de fined component in ter -
face.  This frame work al lows us to mea sure the grace ful deg ra da tion 
prop er ties of in di vid ual fea ture sub sets with re spect to their com po -
nents as well.  The ar chi tec ture and model also iden tify a set of crit i -
cal sys tem com po nents within the crit i cal fea ture sub sets that must
con tinue to op er ate to pro vide any sys tem func tion al ity.  This can be 
used to de ter mine on which sys tem com po nents to spend ef fort en -
sur ing com po nent re li abil ity through re dun dancy and other fault
tol er ance mea sures.
Our next step is to ex tend this model to in cor po rate the al lo ca tion of
the soft ware com po nents to hard ware units.  In a dis trib uted sys tem, 
com po nents that com mu ni cate via the net work are strongly de pend -
ent on the net work for their re quired in put vari ables, mak ing the
net work a sin gle point of fail ure.  Also, soft ware com po nents are
strongly de pend ent on the hard ware node on which they are hosted. 
These con straints will surely in flu ence a sys tem’s abil ity to grace -
fully de grade (hard ware fail ures might re move mul ti ple com po -
nents si mul ta neously), but may be ame lio rated by sys tem-wide
re con fig u ra tion as pro posed in [5].  Ad di tionally, we want to fur ther
de velop the con cept of sys tem util ity to not only dis tin guish be -
tween when the sys tem is “bro ken” or “not bro ken,” but also dif fer -
ent lev els of func tion al ity avail able in dif fer ent sys tem
con fig u ra tions.  We have iden ti fied which con fig u ra tions re sult in
sys tems with pos i tive util ity, but we also need to quan ti ta tively de -
ter mine which of those con fig u ra tions have higher util ity than oth -
ers.  This will be based on de ter min ing which fea tures are more
use ful than oth ers based on mea sures such as per for mance and func -
tion al ity.
6. ACKNOWLEDGMENTS
This work was sup ported by the Gen eral Mo tors Sat el lite Re search
Lab at Car ne gie Mellon Uni ver sity, and Lu cent Tech nol ogies. 
Thanks to Beth Latronico, Bill Nace, Orna Raz, and Yang Wang for
their help in de vel op ing the ideas pre sented.
7. REFERENCES
[1]
Garlan, D., Monroe, R.T., Wile, D., “Acme: Architectural
Description of Component-Based Systems,” Foundations of
Component-Based Systems, Leavens, G.T., Sitaraman, M.
(eds), Cambridge University Press, 2000, pp. 47-68.
[2]
Herlihy, M. P., Wing, J. M., “Specifying Graceful
Degradation,” IEEE Transactions on Parallel and
Distributed Systems, vol.2, no.1, pp. 93-104, 1991.
[3]
Knight, J.C., Sullivan, K.J., "On the Definition of
Survivability," University of Virginia, Department of
Computer Science, Technical Report CS-TR-33-00, 2000.
[4]
Laprie, J.-C., "Dependability of Computer Systems:
Concepts, Limits, Im prove ments", Pro ceed ings of the Sixth
In ter na tional Sym po sium on Software Reliability
Engineering, Toulouse, France, Oct. 1995, pp. 2-11.
[5]
Nace, W., Koopman, P., “A Product Family Approach to
Graceful Degradation,” Distributed and Parallel Embedded
Systems (DIPES), October 2000.
[6]
Shelton, C., Koopman, P., “Developing a Software
Architecture for Graceful Degradation in an Elevator Control 
System,” Workshop on Reliability in Embedded Systems (in
conjunction with Symposium on Reliable Distributed
Systems/SRDS-2001), October 2001, New Orleans, LA.


