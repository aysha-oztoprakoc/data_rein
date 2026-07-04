# Automatic Generation of Graceful Programs.pdf

Automatic Generation of Graceful Programs
Yiyan Lin
Department of Computer Science and Engineering
Michigan State University
East Lansing, USA
linyiyan@cse.msu.edu
Sandeep Kulkarni
Department of Computer Science and Engineering
Michigan State University
East Lansing, USA
sandeep@cse.msu.edu
Abstract—Traditionally, (nonmasking and masking) fault-
tolerance has focused on ensuring that after the occurrence of
faults, the program recovers to states from where it continues
to satisfy its original speciﬁcation. However, a problem with
this limited notion is that, in some cases, it may be impossible
to recover to states from where the entire original speciﬁcation
is satisﬁed. For this reason, one can consider a fault-tolerant
graceful-degradation program that ensures that upon the
occurrence of faults, the program recovers to states from
where a (given) subset of its speciﬁcation is satisﬁed. Typically,
the subset of speciﬁcation satisﬁed thus would be the critical
requirements.
In this paper, we focus on automatically revising a given
program to obtain a corresponding graceful program, i.e.,
a program that satisﬁes a weaker speciﬁcation. Speciﬁcally,
this step involves adding new behaviors that satisfy the given
subset of speciﬁcation. Moreover, it ensures that during this
process, it does not remove any behavior from the original
program. With this motivation, in this paper, we focus on
automatic derivation of the graceful program, i.e., a program
that contains all behaviors of the original program and some
new behaviors that satisfy the weaker conditions. We note
that this aspect differentiates this work from previous work
on controller synthesis as well as automated addition of fault-
tolerance in that this work requires that no new behaviors are
added in the absence of faults.
I. INTRODUCTION
We are increasingly dependent on highly available com-
puter systems to provide fully functional and stable services.
However these existing programs are often subjected to new
types of faults that are not considered the original design.
This may occur due to changing user requirements or due
to deployment of the program in a new environment. It is
especially important that the addition of such fault-tolerance
be done correctly, i.e., the addition indeed provides the
required fault-tolerance and that the existing functionality
of the program is preserved.
Some of the existing approaches for automated addition of
fault-tolerance include [1]–[3], where three different levels
of fault-tolerance, namely nonmasking, masking and stabi-
lizing, are considered. In all these levels, if the fault perturbs
the program then it is guaranteed to recover to legitimate
This work is supported by NSF CNS-0914913 and AFOSR Award
FA9550-10-1-0178.
states from where it satisﬁes its speciﬁcation. Masking fault-
tolerance includes an additional requirement that the safety
property is preserved during such recovery process. And,
stabilizing fault-tolerance requires that even if faults perturb
the program to an arbitrary state, the program still recovers
to legitimate states.
However, one limitation of these approaches is that in
many scenarios, it is impossible for the program to recover to
the original program behavior after faults occur. In such sce-
narios, it is desirable that the program exhibits some graceful
behavior, i.e., behavior that is close to its original behavior.
A canonical example of a graceful behavior program in-
cludes the case where the original program provides core
services and auxiliary services. However, after recovery, the
program may only provide core services and fail to provide
the auxiliary services. More generally, in such a system, it
is expected that the program will satisfy its speciﬁcation
under normal circumstances. However, upon occurrence of
faults, it may satisfy (a given) weaker (respectively, relaxed)
speciﬁcation.
The idea of such graceful degradation has been introduced
in [4], where authors consider the speciﬁcation to consist
of a set of n properties. Subsequently, they consider 2n
possible speciﬁcations for each possible subset of these n
properties. Thus, theoretically, we can consider 2n possible
programs depending upon the exact subset of properties that
are expected to be satisﬁed under different circumstances.
In practice, however, considering such 2n speciﬁcations is
unnecessary. For example, in the above scenario, there is
no need to consider a program that only provides auxiliary
services. Likewise, there is also no need to consider a
program that provides neither the core nor the auxiliary
services. In other words, in the above example, we need
to consider two programs, one that guarantees that both the
core and auxiliary services are provided, and another that
guarantees that at least the core services are provided.
To further illustrate application of graceful degradation,
we use the printer example shown in [4]. A printer system
consists of computers sending printing tasks to a collection
of printers. The tasks are organized in a queue and each
printer executes a transaction in which it dequeues only one
task and then prints it. In an ideal scenario, one may prefer
2012 31st International Symposium on Reliable Distributed Systems
1060-9857 2012
U.S. Government Work Not Protected by U.S. Copyright
DOI 10.1109/SRDS.2012.8
225
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on July 02,2026 at 14:09:22 UTC from IEEE Xplore.  Restrictions apply. 


that printer system ensure that the printing occurs in FIFO
order, i.e., the task that is dequeued ﬁrst is printed ﬁrst.
Thus, in an ideal setting, the speciﬁcation requires that at
most one dequeue operation can occur at a time. And, the
next dequeue operation occurs only after the current task is
printed. As one can imagine, although this is a very simple
speciﬁcation, it results in reduced availability. Moreover, in
the presence of faults such as network delays, computer
crashes, it may not be possible to guarantee that the program
can recover to states from where this speciﬁcation would be
satisﬁed. Hence, one possible weaker speciﬁcation (consid-
ered in [4]) is to allow a limited out-of-order printing. For
example, the simplest such speciﬁcation is that task n is
printed only after task n −2 is printed although task n may
be printed before task n −1.
Based on the above examples, we can view a graceful
degradation program to have the following properties. In the
absence of faults, the program satisﬁes its original (stronger)
speciﬁcation. However, if faults occur then it is guaranteed
to recover to states from where it satisﬁes the degraded
(weaker) speciﬁcation. Our goal in this paper is to focus on
automated addition of graceful degradation to an existing
program. Thus, in our algorithm, we begin with the fault-
intolerant program that satisﬁes the original speciﬁcation,
the original and degraded speciﬁcation and faults. And, the
goal of the algorithm is to obtain a fault-tolerant graceful
degradation.
One of the difﬁculties in generating the fault-tolerant
program that provides graceful degradation lies in the fact
that the input does not contain a program that satisﬁes the
weaker speciﬁcation. Asking the designer to specify such a
program is undesirable, since it increases the overhead for
the designer.
With this motivation, in this work, we focus on generation
of a graceful program where we begin with a program,
say p, that satisﬁes the original speciﬁcation and constructs
a program, say pg, that satisﬁes the weaker speciﬁcation.
Clearly, pg cannot satisfy the weaker speciﬁcation in an
arbitrary way. Hence, we constrain this step to require that
pg has all transitions of program p. However, it may include
additional transitions that allow it to exhibit behaviors that
only satisfy the weaker speciﬁcation.
Revisiting our previous example to illustrate generation of
graceful programs, we begin with a program that ensures that
the print ordering is FIFO. Our work will generate a program
that will include the FIFO behavior as well as the behavior
where some limited out-of-order printing is permitted. In
other words, the generated program will not prevent FIFO
behavior but it will not guarantee it. Additionally, it will
prevent excessive out-of-order printing.
Observe that the generation of the graceful program does
not take into consideration the effect of fault that may require
one to provide graceful degradation. Instead, it generates
a program, pg, whose behaviors could be used to provide
Relaxed
Speciﬁcation
Legitimate
States
Program
Automatic
Program
Generation
Graceful
Program
Figure 1: Design of Graceful Program
recovery in the presence of faults. Although this part is
outside the scope of this paper due to reasons of space, one
can design a fault-tolerant graceful degradation program pf
using the algorithm in this paper. Speciﬁcally, in this case,
we use the input of the original program, p, the graceful
program, pg, and faults as input to generate pf such that
pf behaves like p in the absence of faults. However, in the
presence of faults, it recovers to the behaviors of pg (instead
of p). We refer the reader to [5] for this extension.
Contributions of the paper.
The contributions of the
paper are as follows:
−We deﬁne the problem of automated addition of grace-
ful degradation and present an algorithm to solve it.
Unlike previous algorithms [6] that focus on removing
behaviors in the absence of faults, this algorithm
focuses on adding new behaviors while ensuring that
these behaviors still satisfy the weaker speciﬁcation.
−We illustrate our algorithm with one case study,
namely the printer system from [4].
Organization of Paper.
The rest of paper is organized
as follows: We deﬁne the notion of program, speciﬁcation
and speciﬁcation relaxation in Section II. In Section III, we
formally state the problem of automated generation of the
graceful program. In Section IV, we present the algorithm
to generate the graceful program from the original program
and the speciﬁcation (original and relaxed). In Section V, we
present one case study to demonstrate the graceful program
generation step by step. Finally, in Section VI we discuss
related work and in Section VII, we present the conclusion
and discuss future work.
II. PRELIMINARY
In this section, we give formal deﬁnitions of programs,
program speciﬁcations, and graceful degradation. The pro-
gram is speciﬁed in terms of its state space and transitions.
The deﬁnition of speciﬁcation is adapted from [7]. The
notion of graceful degradation is adapted from [4].
A. Program
A program p, speciﬁed as a tuple ⟨Sp, δp⟩, consists of its
state space Sp and transitions δp, where δp ⊆Sp × Sp. A
state predicate of p is any subset of Sp. A state predicate
S is closed in p (respectively, δp) iff (∀(s0, s1) ∈δp : (s0 ∈
S ⇒s1 ∈S)). A sequence of states, ⟨s0, s1, · · ·⟩(denoted
226
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on July 02,2026 at 14:09:22 UTC from IEEE Xplore.  Restrictions apply. 


by σ), is a computation of p iff(1) ∀j : 0 < j < length(σ) :
(sj−1, sj) ∈δp, and (2) if σ is ﬁnite and terminates in state
sl then there does not exist state s such that (sl, s) ∈δp.
In other words, in each step of the computation of p, some
transition of p is executed. And, the computation is ﬁnite iff
p does not have any transition in the ﬁnal state.
The projection of program p on state predicate S, denoted
as p|S is the program ⟨Sp, {(s0, s1) ∈δp ∧s0, s1 ∈S}⟩. In
other words, p|S includes transitions of p that begin and end
in S.
Notation. In the remaining part of this paper, if the context
is clear, we use p and δp (transitions of p) interchangeably.
Also, we say that a state predicate S is true in state s iff
s ∈S.
B. Speciﬁcation
Following Alpern and Schneider [7], we let the speciﬁca-
tion of program consisting of a safety speciﬁcation and a
liveness speciﬁcation. The safety speciﬁcation is speciﬁed
in terms of a set of bad states, say Sfbs, that program is
not allowed to reach, and a set of bad transitions, Sfbt, that
the program is not allowed to execute. Thus, a sequence
⟨s0, s1, · · ·⟩(denoted by σ) satisﬁes the safety speciﬁcation
iff (1) ∀j : 0 ≤j < length(σ) : sj̸ ∈Sfbs, and (2)
∀j : 0 < j < length(σ) : (sj−1, sj)̸ ∈Sfbt.
The liveness speciﬁcation, on the other hand, denotes
“good thing” happens during program execution. We use
leadsto property (L ⇝T ) to denote liveness speciﬁcation,
where both L and T are state predicates. Thus, a sequence
⟨s0, s1, · · ·⟩(denoted by σ) satisﬁes the safety speciﬁcation
iff ∀j : (L is true in sj ⇒∃k : j ≤k < length(σ) :T is
true in sk).
A speciﬁcation, say spec is a tuple ⟨Sf, Lv⟩, where Sf
is a safety speciﬁcation and Lv is a liveness speciﬁcation.
A sequence σ satisﬁes spec iff it satisﬁes Sf and Lv.
Hence, for brevity, we say that the program speciﬁcation
is an intersection of a safety speciﬁcation and a liveness
speciﬁcation.
Given a program p, a state predicate S, and speciﬁcation
spec, we say S is invariant of p iff (1) S is closed on p; (2)
Every computation of p that starts in a state, say s, where
s ∈S satisﬁes spec; and (3) S̸ = ∅.
C. Graceful Degradation
In graceful degradation, it is expected that the program
will satisfy a stronger speciﬁcation under normal circum-
stances. And, it will satisfy a weaker speciﬁcation under
some other circumstances (e.g., in the presence of faults).
Let spec = ⟨Sf, Lv⟩and specr = ⟨Sfr, Lvr⟩be two
speciﬁcations. We say that specr is weaker than spec iff
for any sequence σ if σ satisﬁes specr then σ satisﬁes spec.
III. PROBLEM STATEMENT
In this section, we formally deﬁne the problem of gen-
eration of program that satisﬁes the weaker speciﬁcation
(cf. Problem 1). We begin with a program p that satisﬁes
the speciﬁcation spec from I. We derive a program, say
pg, and its invariant Ig such that pg satisﬁes a weaker
speciﬁcation, say specr from Ig. Next, we consider the
relation between p and pg as well as I and Ig to identify
the problem statement. One requirement on pg is that pg is
supposed to add new behaviors that potentially violate spec
while satisfying specr. And, it is not allowed to remove any
behaviors of p that satisfy spec. Since the correctness of p
is known from its invariant I, based on this requirement,
it follows that I should be a subset of Ig. Additionally,
pg cannot remove any behaviors (respectively, transitions)
within the original invariant I. Thus, the problem statement
is shown as follows:
Problem Statement III.1:
Given p, I, spec and specr such that
p satisﬁes spec from I.
Identify pg and Ig such that:
A1: pg|I = p|I, I ⊆Ig.
A2: pg satisﬁes specr from Ig.
A3: pg|I satisﬁes spec from I.
Remark.
The above problem statement has a requirement
that I be a subset of Ig. This requirement differs from [6]
in that this enlarges the invariant by adding new states from
where the new speciﬁcation can be satisﬁed. By contrast,
in [6], the problem statement requires that the generated
invariant be a subset of the original invariant. For this
reason, existing algorithms cannot be used to solve the above
problem.
IV. ALGORITHM FOR GENERATING GRACEFUL
PROGRAM
Speciﬁcally, we begin with the given program p, its
invariant I and its two speciﬁcations (stronger) spec and
(weaker) specr. In turn, spec and specr are speciﬁed in
terms of the corresponding safety and liveness speciﬁcation.
Our goal is to construct pg and Ig such that they satisfy
constraints of Problem III.1.
Our program also takes an additional input which is a state
predicate, namely Sa. The intuition for Sa arises from the
fact that the program is expected to satisfy the speciﬁcation
specr under certain constraints. Predicate Sa is used to
characterize these constraints. If such constraints are not
easily identiﬁable, Sa can be instantiated to be Sp −I, i.e.,
all states except those in I.
The algorithm ﬁrst computes IΔ to be the set of states in
Sa except those that violate safety (i.e., those in Sfrbs). The
ﬁrst guess for Ig, the invariant for the graceful program is
then set to I ∪IΔ (Line 2). Then, the algorithm computes
the ﬁrst guess for pg. Speciﬁcally, in pg, we reuse all the
transitions in p that begin in I. We also include all transitions
that begin in IΔ unless they violate safety Sfrbt (Line 3).
Starting from Line 4, the algorithm revises the program by
227
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on July 02,2026 at 14:09:22 UTC from IEEE Xplore.  Restrictions apply. 


ensuring the liveness speciﬁcation is satisﬁed. From Line 6
to 9, for the generated program we ﬁrst exclude the deadlock
states, i.e., states from where no transitions originate from
Ig. Then we recompute pg such that all the reachable states
by pg starting from I′(or I) remains in I′(or I respectively).
To ensure liveness, we deﬁne a function rank that assigns
each state an integer value that represents the length of the
shortest path from that state to reach a target state predicate
T . Then, on Line 11 and 12, we exclude transitions where
rank does not decrease. Removal of such transitions ensures
that there will be no cycles that prevent the program from
reaching T . One potential side effect of removing transitions
is that the new program may include deadlock states. To
resolve deadlock states we repeat the loop starting at Line
4. Finally, this process stops once a ﬁxpoint is reached.
Algorithm 1 Graceful Program Generation
Input: state predicate Sa, program transitions p, invariant I,
weaker speciﬁcation specr including weaker safety speciﬁ-
cation Sfr (consisting of Sfrbs and Sfrbt), and liveness
speciﬁcation Lvr (consisting n leads-to properties of the form
Fi ⇝Ti, i ∈1 · · · n).
Output: graceful program pg and invariant Ig with weaker spec-
iﬁcation.
1: IΔ := Sa −Sfrbs
2: I′ := I ∪IΔ
3: p′ := {(s0, s1)|s0, s1 ∈I′ :: (s0 ∈I ∧(s0, s1) ∈p) ∨(s0 ∈
IΔ ∧(s0, s1) /∈Sfrbt)}
4: repeat
5:
Iold := I′
6:
repeat
7:
p′ := maxp(p′, I, I′)
8:
I′ := I′ −deadlock(I′, p′)
9:
until Iold = I′
10:
Iold := I′, pold := p′
11:
p′ := p′ −
i∈1···n{(s0, s1)|s0 ∈I′ ∧rank(s0, Ti, p′) ≤
rank(s1, Ti, p′) ∧rank(s0, Ti, p′)̸ = 0
∧rank(s1, Ti, p′)̸ = ∞}
12:
I′ := I′ −
i∈1···n{s|rank(s, Ti, p′) = ∞∧s ∈Fi ∧s /∈
I}
13: until Iold = I′ ∧pold = p′
14: return p′ as pg, I′ as Ig if I′̸ = ∅, otherwise declare no
graceful program generated.
Function: maxp(t: transition predicate, S1,S2,· · · :set of state
predicates where S1 ⊆S2 ⊆· · · )
return {(s0, s1)|t ∩(s0 ∈S1 ⇒s1 ∈S1) ∧(s0 ∈S2 ⇒s1 ∈
S2) ∧· · · }
Function: deadlock(S: state predicate , t: transition predicate)
return {s0|s0 ∈S ∧(∀s1 ∈S : (s0, s1) /∈t)}
Function: rank(s: state , T : state predicate , t: transition predi-
cate)
return the shortest path length from s to one of the state in T , if
the path(consisting only transitions in t) exists; or ∞, otherwise.
Theorem 1. Algorithm 1 is sound.
V. CASE STUDIES
In this section, we demonstrate process of generating the
graceful program with one case study, namely the printer
system. In the case study, we ﬁrst deﬁne the program with
its speciﬁcation (including the original and the graceful
speciﬁcation). Then we simulate the algorithm on each case
study step by step.
A. Printer System
In the ﬁrst case study, we focus on the printer sys-
tem considered in [4]. In the original speciﬁcation, the
printer system is required to satisfy the FIFO speciﬁcation.
However, as argued in [4], it may be necessary to relax
this requirement under certain constraints. In particular, the
weaker requirement considered in [4] requires that some out-
of-order printing is permitted.
To model this state space and transitions concisely, we
use variables (associated with a domain) and actions.
And, the state space Sp of p is obtained by assigning
each variable a value from its respective domain. Thus,
the use of variables allows us to represent the state space
compactly. Additionally, to compactly represent δp, we use
actions of the form: guard −→statement where guard
is a constraint involving program variables and statement
updates program variables. An action guard −→statement
denotes the set of transitions {(s0, s1) : guard is true in
s0 and s1 is obtained by changing s0 as prescribed by
statement}. We use x(s) to denote the value of variable
x in state s.
Original program.
The program in [4] consists of
several clients and several print servers. Using the trans-
action semantics, the clients ‘enqueue’ their print request in
a shared queue. The print servers remove from this queue
and print the task. For simplicity, we do not model the
transactions used for concurrency control. Furthermore we
omit the enqueue operation since it does not affect the
behavior we interested in.
Hence, the original program, say A, consists of two parts
(1) once ith task has been dequeued (di = 1) and it has not
been printed (pi = 0), then print it (pi := 1) and (2) if the
ith task has been printed (pi = 1), then the next task (i + 1)
in queue get a chance to be dequeued (di+1 := 1). Thus
actions are as follows:
di = 1 ∧pi = 0 −→
pi := 1
pi = 1 −→
di+1 := 1
Safety Speciﬁcation.
Recall that the safety speciﬁcation
in terms of a set of bad states program should not reach
and a set of bad transitions that the program should not
execute. The ﬁrst speciﬁcation Sfbs 1 is satisﬁed by the
original program and requires that the printing must occur in
order and, hence, task j cannot be dequeued until task j −1
is printed. The graceful speciﬁcation permits the possibility
that task j can be dequeued even if task j −1 is not printed.
However, it requires that task j cannot be dequeued until
task j −2 is printed. Thus, the safety speciﬁcation (original
228
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on July 02,2026 at 14:09:22 UTC from IEEE Xplore.  Restrictions apply. 


and graceful) that identiﬁes the states that should not be
reached is speciﬁed as follows:
Sfbs 1 := ∃i, j ∈1 · · · n, pi(s) = 0 ∧dj(s) = 1 ∧j > i
Sfbs 2 := ∃i, j ∈1 · · · n, pi(s) = 0 ∧dj(s) = 1 ∧j > i + 1
Observe that Sfbs 1 is the stronger speciﬁcation capturing
the notion of FIFO, and Sfbs 2 is a weaker speciﬁcation
since it allows at most two tasks be dequeued without
ﬁnishing the pending printing. One could consider further
relaxation that allows more out-of-order printing. Our algo-
rithm can be applied in this context by applying Algorithm 1
to the program generated at the end of this section. However,
the detailed analysis of this generation is outside the scope
of this paper.
In addition to bad states, safety speciﬁcation can include
bad transitions that the program is not allowed to execute.
The bad transitions, Sfbt c, describe structural constraints
that have to be satisﬁed by the printer system. In particular,
Sfbt c states that a printed task cannot be reset to unprinted.
Likewise, once the task has been dequeued it cannot be re-
enqueued. And, a task cannot be printed until it is dequeued.
Note that the structural constraints have to be satisﬁed in the
original as well as the graceful program. Also, at most one
variable can be changed in any transition. Thus,
Sfbt c := {(s, s′)|∃i, j ∈1 · · · n,
(pi(s) = 1 ∧pi(s′) = 0)
∨(di(s) = 1 ∧di(s′) = 0)
∨(di(s′) = 0 ∧pi(s′) = 1)
∨(i̸ = j ∧di(s)̸ = di(s′) ∧dj(s)̸ = dj(s′))
∨(i̸ = j ∧pi(s)̸ = pi(s′) ∧pj(s)̸ = pj(s′))
∨(di(s)̸ = di(s′) ∧pj(s)̸ = pj(s′))}
Thus, we identify safety speciﬁcation for original program
as Sfbs 1 and Sfbt c; for graceful program as Sfbs 2 and
Sfbt c. Note that although the set of bad transitions are the
same here, it is not a requirement for Algorithm 1.
Liveness Speciﬁcation.
The liveness speciﬁcation re-
quires that eventually all tasks are printed. Thus,
Lv := true ⇝SL, where SL := ∀i ∈1 · · · n, di = pi(s) = 1
Application of Algorithm 1. We instantiate Algorithm
1 with following inputs:
−program p: is instantiated to be transitions correspond-
ing to program A. For simplicity, we assume that
there are three tasks in the system. Hence, the state of
the program is represented as (d1d2d3, p1p2p3), where
di (respectively, pi) denotes whether task i has been
dequeued (respectively printed).
−The safety speciﬁcation is instantiated so that the set
of bad states is Sfbs 2 and the set of bad transitions
is Sfbt c
−Liveness speciﬁcation is speciﬁed to be Lv.
−Invariant I is instantiated to be the states reached in
the computation of A by starting from the initial state
(000, 000).
−State predicate Sa is instantiated to be Sp −I
First consider the candidate states generated outside I
from Line 1 that also excludes those violate Sfbs 2. In
general, as the weaker safety speciﬁcation requires, new
program allows two tasks can be dequeued regardless either
one ﬁnished printing or not and a new task can then be
dequeued if either one of two previous dequeued tasks
ﬁnishes printing. In other words,
IΔ = {(110, 000), (110, 010), (111, 010), (111, 011),
(110, 110), (111, 100), (111, 101), (010, 000), (010, 010),
(011, 010), (011, 011)}
The new program transitions generated are all possible
pair of states in IΔ plus those recovered from IΔ to I
provided that they do not violate Sfbt c. There are no
deadlock states on Line 8. Moreover, since every state in
I or IΔ has a path to a state where all tasks are completed,
no state and transition are removed on Lines 11 and 12.
Now, we evaluate the new behavior of the printer system
in pg provided the context shown in ﬁgure 2. Ideally, the
program stays in invariant I while satisfying Sfbs 1, Sfbt c
and Lv. However, if the program is perturbed to be outside I
then it will satisfy Sfbs 2, Sfbt c and Lv. Figure 2 shows the
behavior of the graceful program. Note that in this program,
the tasks being printed is not totally out of order, though
it is not FIFO. For example, task 3 cannot precedes task 2
provided that task 1 has not been printed.
000,000
100,000
100,100
110,100
110,110
111,110
111,111
111,100
111,101
110,000
110,010
111,010
111,011
101,100
101,101
010,000
010,010
011,010
011,011
Figure 2: Printer System with original invariant I
=
{(000,000),(100,000),(100,100),(110,100),(110,110),(111,110),(111,111)}
and invariant (under weaker speciﬁcation) Ig =
I ∪{(110,000),(110,010),(111,010),(111,011),(110,110),(111,100),(111,101),
(010,000),(010,010),(011,010),(011,011)}
VI. RELATED WORK
The work in this paper is closely related to that of
controller synthesis, game theory and automated addition of
fault-tolerance. Controller synthesis considers the following
problem: Given two languages U (plant) and D (desired
system), identify a third language C (controller), such that
U ∩D ⊆C [8]. Thus, the goal is to begin with the plant
and add controller to obtain the desired system. The idea of
transforming a fault-intolerant system into a fault-tolerant
system using controller synthesis is was used in in [9]. Also
in [10], Girault and Rutten demonstrate the application of
229
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on July 02,2026 at 14:09:22 UTC from IEEE Xplore.  Restrictions apply. 


discrete controller synthesis in automated addition of fault-
tolerance in the context of untimed systems. Our work in
this paper differs from this work in that we are trying to
relax the speciﬁcation of the given system whereas they are
trying to strengthen it. In the context of game theoretical
approach for model revision, program is automatically ﬁxed
as a game [11], [12]. The game is played on the model of
two players [13], i.e., program and environment. A program
is considered to win the game if the speciﬁcation is always
satisﬁed no matter how the environment interacts with the
program. Game theoretic methods are generally based on
the theory of tree automata [14].
The model repair for probabilistic system [3] is to revise
a probabilistic system M such that the new system M ′
satisﬁes a probabilistic temporal logic formula. M ′ differs
from M only in the transition ﬂows of controllable states.
Our work is orthogonal to that in [3] in that this work can
be extended in the context of dealing with probabilities and
their work can be extended to deal with addition of graceful
degradation. Algorithms for automatic addition of fault-
tolerance [1], [6] add fault-tolerance concerns to existing
untimed or real-time programs in the presence of faults, and
guarantee the addition of no new behaviors to the original
program in the absence of faults. In the context of this paper,
we utilize the synthesis algorithm for adding fault-tolerance.
Our work builds on this work by enabling repair in scenarios
where the previous work fails to perform repair or has a
signiﬁcantly higher overhead for the designer.
VII. CONCLUSION
In this paper, we presented the approach for generating
the graceful program. We presented a sound algorithm for it.
Additionally, we illustrated our approach with one example:
printer system. The example is chosen from [4] where a
similar graceful requirement is considered in the context of
manual design.
As we saw from the case study, the algorithm tries to
construct the graceful program to have maximal choice
(non-determinism). This algorithm also differs from previous
work on automated addition of fault-tolerance in that previ-
ous work on automated addition of fault-tolerance disallows
adding transitions in the absence of faults. By contrast,
in the design of graceful program, removing transitions is
disallowed. This ensures that the graceful program has all the
behaviors of the original program. Additionally, it adds new
behaviors that satisfy the weaker speciﬁcation. These new
behaviors are crucial in providing recovery in the presence
of faults.
Although it is outside the scope of this paper, it
is
possible
to
combine
algorithms
for
adding
fault-
tolerance/multitolerance to the problem of designing grace-
ful programs. Speciﬁcally, it is possible to add fault-
tolerance to the printer system discussed in this paper.
Other examples where this approach has been used include
byzantine agreement and ventilation control at Ohio Coal
Research Center (OCRC).
REFERENCES
[1] B. Bonakdarpour and S. S. Kulkarni, “Exploiting symbolic
techniques in automated synthesis of distributed programs,” in
In IEEE International Conference on Distributed Computing
Systems, 2007, pp. 3–10.
[2] F. Abujarad and S. Kulkarni, “Constraint based automated
synthesis of nonmasking and stabilizing fault-tolerance,” in
Reliable Distributed Systems, 2009. SRDS ’09. 28th IEEE
International Symposium on, sept. 2009, pp. 119 –128.
[3] E. Bartocci, R. Grosu, P. Katsaros, C. R. Ramakrishnan, and
S. A. Smolka, “Model repair for probabilistic systems,” in
TACAS, 2011, pp. 326–340.
[4] M. Herlihy and J. M. Wing, “Specifying graceful degrada-
tion,” IEEE Trans. Parallel Distrib. Syst., vol. 2, no. 1, pp.
93–104, 1991.
[5] Y. Lin, S. Kulkarni, and W. Leal, “Tech-report: Automated
multi-graceful degradation: A case study,” in www.cse.msu.
edu/ ∼sandeep/publications/ocrctech/tech.pdf.
[6] S. S. Kulkarni and A. Arora, “Automating the addition
of fault-tolerance,” in Formal Techniques in Real-Time and
Fault-Tolerant Systems (FTRTFT), 2000, pp. 82–93.
[7] B. Alpern and F. B. Schneider, “Deﬁning liveness,” Informa-
tion Processing Letters, vol. 21, no. 4, pp. 181 – 185, 1985.
[8] P. J. Ramadge and W. M. Wonham, “The control of discrete
event systems,” Proceedings of the IEEE, vol. 77, no. 1, pp.
81–98, 1989.
[9] K. H. Cho and J. T. Lim, “Synthesis of fault-tolerant su-
pervisor for automated manufacturing systems: A case study
on photolithography process,” IEEE Transactions on Robotics
and Automation, vol. 14, no. 2, pp. 348–351, 1998.
[10] A. Girault and ´E. Rutten, “Automating the addition of fault
tolerance with discrete controller synthesis,” Formal Methods
in System Design (FMSD), vol. 35, no. 2, pp. 190–225, 2009.
[11] A. Pnueli and R. Rosner, “On the synthesis of a reactive
module,” in Principles of Programming Languages (POPL),
1989, pp. 179–190.
[12] B. Jobstmann, A. Griesmayer, and R. Bloem, “Program repair
as a game,” in Conference on Computer Aided Veriﬁcation
(CAV), 2005, pp. 226–238, LNCS 3576.
[13] W. Thomas, “On the synthesis of strategies in inﬁnite games.”
in Theoretical Aspects of Computer Science (STACS), 1995,
pp. 1–13.
[14] ——, Handbook of Theoretical Computer Science: Chapter
4, Automata on Inﬁnite Objects.
Elsevier Science Publishers
B. V., 1990.
230
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on July 02,2026 at 14:09:22 UTC from IEEE Xplore.  Restrictions apply. 


