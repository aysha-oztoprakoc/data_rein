# Graceful Degradation in the Presence of Exceptions.pdf

Graceful Degradation in the Presence of Exceptions
Nikolas Nehmer
University of Kaiserslautern
Department of Computer Sscience
P.O. Box 3049, 67653 Kaiserslautern, Germany
nnehmer@informatik.uni-kl.de
+49 (0) 631 - 205 2644
Abstract
In today’s software development processes, exception
handling is mostly considered as an issue of minor impor-
tance. Furthermore, explicit and systematic exception han-
dling strategies and tool-support for reasoning about excep-
tion ﬂow and exception compatibility between components
are very rare. Nevertheless exceptions not handled appro-
priately can seriously harm a software system – uncaught
exceptions for example usually lead to a crash or shutdown
of the whole system. In this paper a novel approach to sys-
tematic exception handling using appropriate tool-support
is presented. Static code analysis is used to detect and iden-
tify exception handling related problems. Identifying and
isolating affected data structures during runtime is a ma-
jor part of this approach. A generic system-mechanism re-
stricting error propagation to contain the fault’s impact on
the overall system is introduced. The overall objective is to
achieve graceful degradation in the presence of exceptions
of any kind.
keywords: exception handling, graceful degradation,
dynamic fault containment, static code analysis, exception
propagation
submission category: regular paper
1
Introduction
Exception-handling is a programming language con-
struct or computer hardware mechanism designed to handle
the occurrence of conditions that change the normal ﬂow of
program-execution. The condition raising the control-ﬂow
change is called an exception. In general exceptions are
used for signaling error (exceptional) conditions.
Unfortunately, the presence failures[2] is a fact of life
today’s software has to deal with. Modern programming
languages such as C#[9], C++[23] or Java[7] provide ex-
plicit exception handling mechanisms as programming lan-
guage constructs to handle these exceptional conditions and
to ease the difﬁculty of developing robust software systems.
Exception-handling mechanisms provide means for raising
exceptional conditions explicitly and means for specify-
ing blocks of code to handle one or more of these excep-
tional conditions[6]. Handling exceptions includes a vari-
ety of different means; from sending simple error notiﬁca-
tion messages to client applications to complex forward er-
ror recovery mechanisms. In general, exception-handling
mechanisms are intended to make developers design and
build more robust and dependable software systems by sep-
arating code regions that handle unusual system behavior
on the one hand from code that deals with normal process-
ing on the other hand. This separation of concerns leads to
consequences for system design. As exceptions are not nec-
essarily handled at the place of their occurrence, exceptions
can ﬂow to an arbitrary point within the system and even
beyond system boundaries if they are not handled appropri-
ately. Developers must be aware of every exception type
possibly raised at any program point or that can be prop-
agated to it from lower-level modules. Some exception-
handling techniques provided by current programming lan-
guages like Java help developers in this reasoning process
by adding exception information to the method declara-
tions, for example. Common compilers make use of excep-
tion declarations to check whether the corresponding excep-
tion handlers are provided by a client application.
Anyhow, this kind of exception-handling support pro-
vided by a multitude of programming languages is insuf-
ﬁcient for several reasons.
• Unspeciﬁc throws – Modern object-oriented languages
allow sub-typing of exceptions which may lead to un-
speciﬁc throws.
• Implicit catches – The classiﬁcation of exceptions into
type hierarchies complicate reasoning about exception
structures and may lead to implicit catches[17].


• Exception handling “ad hoc” – developers have to deal
with exception handling without tool or infrastructure
support. A default exception handling mechanism at
the programming language runtime level is missing.
• Uncaught exceptions – In some programming lan-
guages like Java checked and unchecked exceptions
are distinguished. Unchecked exceptions bypass the
compiler-check and consequently developers of client
modules are not forced to handle these exceptions
types. This fact may lead to uncaught exceptions. If
exceptions are not handled appropriately and hence
ﬂow through the system until they reach the system’s
entry point the program’s execution will be aborted im-
mediately. Crashing the entire software system is the
usual fate of uncaught exceptions.
Uncaught exceptions may have the most fatal and ob-
vious impact on the system behavior.
But beyond that,
there are further shortcomings regarding exception handling
mechanisms in today’s programming languages. The list
below mentions a few:
• Stack trace propagation harms trust (e.g. in service ori-
ented architectures based on today’s web service tech-
nology)
• No clear responsibilities for exception handling
• Exception hierarchy is futile (often only applicable to
academic examples)
• Without strict programming discipline, improper han-
dling of exceptions will jeopardize the stability of the
system
– Throw – catch without handling – rethrow the
same exception or a superclass (wrapping excep-
tions often only applicable to academic exam-
ples)
– Catch {} with an empty handler
– Decorating methods with “throws Exception”
where Exception is the superclass of all excep-
tions
• Only a few reasonable handling patterns for exceptions
(decentralized error handling leads to redundant code
at different places e.g. user notiﬁcation)
– User notiﬁcation
– Graceful degradation
– Application speciﬁc error handling
• Unstable interfaces (e.g. adding exceptions)
• Scalability issues (especially in systems of systems)
“Real world” examples such as Windows blue-screens
or the crash of the Ariane 5[15, 12] rocket illustrate the
possible impact of inappropriate exception handling on the
overall system dependability. The impact reaches from data
or content loss in ofﬁce or mail applications to catastrophic
crashes of air carriers or erroneous medical equipment com-
promising human life. This clariﬁes the need for a system-
atic and defensive approach to exception handling. In the
following some meaningful examples are given.
Everyday life software - The ﬁrst example that comes in
mind when thinking of inappropriate exception handling is
software used in everyday life such as windows, ofﬁce ap-
plications or computer games. In windows uncaught excep-
tions often end up in the well known blue-screen leaving up
the user with a listing of affected memory areas and a tex-
tual hint on how to restart the computer. In ofﬁce applica-
tions or applications like computer games uncaught excep-
tions often just terminate the main application (including
side effects such as loosing data) and a simple stack trace is
displayed on a pop-up window. It seems that the exception
handling strategy used in both examples does not improve
the system overall dependability. An illustrating screen shot
is given below in ﬁgure 1.
Figure 1. Microsoft Ofﬁce Error
Therac 25 - The Therac 25[14] was a medical linear ac-
celerator used as a radiation therapy machine for the treat-
ment of cancer in several US and Canadian hospitals. It
was involved in at least six known accidents between 1985
and 1987, in which at least six patients were given massive
overdoses of radiation, three of them died afterwards. The
failure of the radiation therapy machine is based on one of
the most momentous software errors in history. The ma-
chine offered two operational modes - electron mode and
photon (or x-ray) mode.
When operating in the photon mode, the machine was
designed to rotate four components into the path of the elec-
tron beam - especially a target, which converted the high
energy electron beam into low energy x-rays. The acci-
dents occurred when the high-power electron beam was ac-
tivated for x-ray therapy, without the target having been ro-
2


tated into place. Consequently, a potentially lethal dose of
radiation was applied to the patients. Each incident had a
similar pathology. The operator initiated the treatment, but
received an error message indicating that no dose had been
applied. Accustomed to the machine’s quirky behavior, op-
erators were used to retry by pressing the “try again”-button
several times. In fact, the radiation machines were applying
a dose on each trial with radiation levels sometimes 30 to
100 times higher than originally desired. The root cause of
this disaster was a complex chain of events. The software
failures were mostly due to dynamic issues resulting from
concurrency aspects including a race condition initiated by
the operator’s quick handling of the machine. Nevertheless,
inappropriate exception handling displaying an error mes-
sage indicating that no dose had been applied (which in fact
was absolutely wrong), contributes to the chain of events.
Ariane 5 crash - On June 4th, 1996, the maiden ﬂight 501
of the European Ariane 5[15, 12] launcher crashed about 40
seconds after takeoff. This crash was arguably one of the
most expensive software errors in history causing a loss of
roughly 0.5 Billion $. An international inquiry board ana-
lyzed the accident, identifying the root cause as a chain of
events - an out-of-range data condition in a software module
that was not even needed during the crash (reusing Ariane
4 software) raised an uncaught exception. This uncaught
exception lead to a subsequent automatic shutdown of crit-
ical subsystems which lead to the catastrophic crash of the
carrier. Again inappropriate exception handling caused an
accident.
Exception handling is a very complex and poorly tool-
supported task for software developers. Although in pro-
gramming languages such as Java compilers help in reason-
ing about exception ﬂow, many problems related to type-
subsumption, unchecked exceptions or uncaught exceptions
have to be detected and resolved by the developers manu-
ally during the development process and even still persist
undetected in deployed software systems. Especially in to-
day’s large and complex systems, systems of systems, com-
ponent architectures or particularly in service oriented ar-
chitectures reasoning about exception propagation and ex-
ception ﬂow without proper tool-support seems to be un-
manageable. For some reason, exception handling is often
not considered high priority when building systems. This
is because architectures can be viewed as having two sides
– positive and negative. The positive side includes algo-
rithms and functions; the negative side includes handling
exceptional conditions. Perhaps it is because exception han-
dling does not deliver tangible functionality to users. Sys-
tem mechanisms supporting software developers in this rea-
soning process and in designing robust software systems
by establishing sound exception handling mechanisms are
strongly required.First of all, developers need tool- and
infrastructure-support that helps deriving exception propa-
gation information from component code. Secondly, system
runtime mechanisms have to be made available to provide
means for automatic fault containment by building quaran-
tine areas around “infected” data structures during runtime.
In this paper a novel and systematic approach to cop-
ing with some of the shortcomings mentioned above is pre-
sented. Especially reasoning about exception propagation
within applications using a graph-based static code analy-
sis approach is emphasized. The aim of the graph-based
analysis is to identify exception related problems such as
uncaught exceptions and long exception propagation paths.
The information extracted from the code analysis should be
used for static code repair as well as for dynamic fault con-
tainment purposes collecting and isolating ”infected” data
structures during runtime as introduced in this paper. A de-
fault exception handling mechanism based on the concept of
graceful degradation is proposed. The concepts presented in
this paper are illustrated using the Java programming model
but can easily be generalized.
The reminder of the paper is structured as follows. In
Section 2 related work in the ﬁeld of exception analysis is
presented and discussed. Section 3 is threefold. It deals
with a novel graph-based static code analysis approach and
presents a generic approach to dynamic fault containment.
Furthermore some basic principles and concepts deﬁning
the underlying exception model are introduced. Section 4
brieﬂy summarizes and highlights the contribution of the
paper. Furthermore it gives an outlook on future work.
2
Related Work
Various static analysis tools and concepts have been pro-
posed to address problems related to exception handling in
different programming languages making different assump-
tions on execution types and programming model. In this
related work section Java related approaches analyzing syn-
chronous exceptions are discussed.
Of course, any Java
compiler has limited exception handling analysis capabil-
ities as well. For space reasons the discussion is limited to
more advanced approaches.
Ryder et al.[20] have developed the Java Exception
Static Proﬁler (JESP), a tool-suit meant to statically analyze
the frequency of exception handling construct-occurrences
in Java programs. Their studies show a frequent usage of
exception handling constructs in Java programs and empha-
sizes the need for a more systematic approach to handling
exceptions. Sinha and Herrold’s[22] study on the occur-
rence of try and throw statements in a set of seven different
Java programs conﬁrm this statement.
Robillard and Murphy[18] have developed JEX, a tool
for static code analysis of Java exception ﬂows. The Jex-
tool extracts information about the exception structure in
Java programs, providing views of the exception structure
3


and exception handlers that are present. Their approach in-
cludes checked exceptions as well as unchecked exceptions.
Jex aims at providing exception information at any point in
the program hierarchy and therefore is designed at state-
ment level.
Chang et al.[5, 13] have introduced an interprocedural
exception analyzer based on the set-based framework[8].
Their approach estimates uncaught exceptions indepen-
dently of exceptions declared in the method header. Their
analysis determines the types of exceptions propagated by
a method and proves to be more precise than the one of-
fered by the Java compiler. The analysis, however, does
not include the ﬂow of exceptions and is limited to checked
exceptions. In [4] Chang et al. have presented a tool to vi-
sualize exception propagation on method level in Java pro-
grams. For a selected method the visualization displays tex-
tual information on uncaught checked exceptions.
The set-based approaches presented in the related work
section are mostly limited to the analytical part supporting
developers in reasoning about exception propagation and
building more dependable and robust software. Static code
analysis is used to detect drawbacks related to exception
handling - solving the problems is still left up to the de-
veloper. The graph-based concepts proposed in this paper
go one step further and introduces a default exception han-
dling mechanisms as a fall-back strategy to cover uncaught
exceptions or exceptions handled inappropriately on the ap-
plication level.
3
Exception ﬂow analysis and fault contain-
ment
Software
developers
have
to
be
aware
of
type-
subsumption, potentially raised exceptions, exception han-
dlers and their interrelationship within the system’s calling
hierarchy at any arbitrary program point. Exception ﬂow,
exception dependencies or exception handling responsibil-
ities within a system and even beyond system boundaries
have to be transparently identiﬁable. The desired exception
transparency can only be achieved by computer-aided sup-
port mechanisms. The required tool-support would serve
software developers during the whole development process
of a software system, especially during implementation and
for failure analysis.
For exception ﬂow analysis several
aspects are of great importance – implicitly and explicitly
raised exceptions, exception handlers, the exception hier-
archy, the calling hierarchy of a component and especially
the interrelationship of these entities. This information can
directly be derived from a program’s source code. A pro-
gram’s abstract syntax tree (AST) is a logic tree represen-
tation (ﬁnite, labeled, directed tree) of a program’s source
code. Consequently, static code analysis based on an ab-
stract syntax tree representation is used to exactly relate
possible exception occurrences and corresponding excep-
tion handlers to code blocks in the calling hierarchy of a
software system. A graph representation of the informa-
tion given above can be derived by parsing a program’s
abstract syntax tree. This graph structure can be used to
gain exception-ﬂow information. A static analysis of this
graph can be applied to detect exception related problems
like uncaught exceptions, long propagation paths, unspe-
ciﬁc catches or exception incompatibilities between com-
ponents.
Today’s exception handling mechanisms exclusively lo-
cated on the application level are highly error prone as illus-
trated in the introduction. Consider an uncaught unchecked
arithmetic exception raised in a subcomponent (as it was the
case in the Ariane 5 accident). This exception would nor-
mally ﬂow to the system entry point and terminate the sys-
tem runtime. Consequently, some general fall-back mech-
anisms have to be established to back-up customized ap-
plication level exception handling mechanisms. In general,
these default exception handling mechanisms will not sub-
stitute customized application speciﬁc exception handlers
but restrict error impact in the overall system if customized
exception handlers are inappropriate or just missing.
In
the example given above the uncaught exception should be
detected immediately, caught automatically and access to
the data structures affected by the exception should be pre-
vented. Generic exception handling functionality has to be
provided by frameworks or has to be integrated into pro-
gramming language runtimes and compilers directly. These
runtime mechanisms have to cope with problem cases such
as uncaught exceptions based on a generically applicable
mechanism. Automatic fault containment is one approach
of generically handling errors and restricting their impact
on the overall system dynamically during runtime.
The problem cases detected by a static code analysis
can be tackled in different ways. Obviously, the problems
can be solved by ruling out the root cause and adapting or
changing the source code. This approach is mostly applica-
ble during development (optionally during maintenance) for
systems with full code access only. But at this point several
questions should be raised. Does a developer really want to
tackle all the problems by ruling out the root cause? Is it
reasonable to handle all kinds of exceptions by application
speciﬁc error handlers? Regarding these questions, at ﬁrst,
checked and unchecked exceptions have to be distinguished
conceptually. In Java for example checked exceptions are
usually handled in some way because the compiler enforces
checked exceptions to be treated - either locally or by up-
ward propagation. For some reason, exception handling is
often not considered high priority in a software develop-
ment process. Accordingly, even checked exceptions are
not handled appropriately resulting in runtime problems de-
scribed above (long propagation paths, imprecise catches,
4


etc.). In general unchecked exceptions such as runtime ex-
ceptions (e.g. null pointer exceptions or array out of bounds
exceptions) or system errors (e.g. io-exceptions) can hardly
be handled appropriately on the application level. Hence,
this type of exceptions is mostly ignored by developers re-
garding exception handling. Nevertheless an uncaught run-
time exception or system error will also lead to the prob-
lems discussed earlier such as system crashes. To avoid
these extensive consequences in both cases (for checked and
unchecked exceptions) exceptions should be analyzed and
a systematic and automatic default system-level exception
handling mechanism (i.e. on an abstraction layer below the
application level such as the programming language run-
time) has to be provided.
A systematic and automatic exception handling mech-
anism located on the system level calls for a generic ex-
ception handling approach. Consequently, this means that
recovery mechanisms such as application speciﬁc forward
recovery that require semantics are inappropriate.
Ap-
proaches based on semantic context information are hardly
applicable to the general case. A generic exception han-
dling mechanism gracefully degrading system functionality
by avoiding uncaught exceptions and improving fault con-
tainment by identifying and isolating affected code blocks
is required. When an exception is raised during runtime
the affected data structures have to be identiﬁed and access
to these data structures has to be restricted or completely
prevented. The question if a raised exception can be han-
dled by application speciﬁc handlers and the identiﬁcation
of affected data structures can be supported by using the
graph-structure resulting from the exception ﬂow analysis.
Access restriction can be achieved by dynamically activat-
ing pre-deployed protective wrappers during runtime. The
wrappers’ duty is to build a quarantine area around affected
data structures by restricting client access.
Both approaches – ”development”-tools and runtime
mechanisms are based on an analysis of the exception ﬂow.
Exception ﬂow information can be derived from a system’s
source code directly. Basically, both approaches are based
on a detailed abstract syntax tree analysis to detect excep-
tion related problem cases. During the analysis the abstract
syntax tree is transformed into a simpliﬁed and more ab-
stract graph representation containing exception ﬂow re-
lated information - calling hierarchy, exception hierarchy,
exceptions and exception handlers and their relationship (as
depicited in ﬁgure 2).
3.1
Exception Model
The concepts proposed in this paper are based on some
assumptions expressed in the underlying exception model
brieﬂy described in this section. Basically, the approach
presented in this paper is illustrated using Java (not includ-
Figure 2. Basic Strategy
ing multi-threading) as a reference programming language.
Consequently, the approach is based on the Java program-
ming and exception model but it can easily be adapted to
other programming languages. A detailed description of
the Java exception and programming model goes beyond
the scope of this work. The key assumptions are:
• Exceptions as objects (including type subsumption) [1]
• Termination model[3, 17]
• Checked and unchecked exceptions including pro-
grammed application speciﬁc exceptions, errors and
runtime exceptions (aka implicit and explicit excep-
tions)
• Synchronous exceptions (asynchronous exceptions
raised by concurrent threads for example are beyond
the scope of this paper)
3.2
Detailed Strategy
This section gives a detailed insight into graph-based ex-
ception handling analysis and a dynamic fault containment
approach in the presence of exceptions. Exception handling
analysis can be regarded as a compile-time issue while fault
containment is considered a runtime issue.
3.2.1
Compile-time Issues – Static code analysis
The basic idea is to analyze component code to detect
exception handling related problems during compile-time.
A transparent representation of possible exceptions raised,
handled and handed on at any arbitrary program point is
the outcome of such analysis. In object oriented program-
ming languages a reasonable scope for exception handling
analysis are methods synthesizing all exceptions encoun-
tered within the scope of the method, the exceptions caught
within the scope including subtypes and the exceptions
thrown or handed on beyond the scope of the method (in-
cluding uncaught or undeclared exceptions).
The static
code analysis is based on the abstract syntax tree of compo-
nent code. Information about exceptions required to iden-
tify exception ﬂow includes:
• method call dependencies – aka system calling hierar-
chy
5


• the scope and hierarchy of try blocks
• the expression raising the exception
• contains-relationships between method calls, expres-
sions and try blocks
• the exact location in the calling hierarchy where ex-
ceptions are raised
• exact location in the calling hierarchy of exception
handlers
• the exception identiﬁer and the exception hierarchy to
reason about type-subsumption
A graph containing and relating this information – from
now on called the exception call graph (ECG) – can be
directly derived from a component’s abstract syntax tree.
The ECG represents a component’s calling hierarchy related
to possibly raised exceptions and corresponding exception
handlers. Unfortunately there is no common AST in Java
provided by Sun. The proof of concept for the approach
proposed in this paper will be based on eclipse framework’s
DOM representation of Java code. To properly analyze the
ECG regarding exception related problems the ECG has to
be extended by exception propagation information. There-
fore every node and edge within the ECG is annotated with
exception information and exception propagation informa-
tion identifying the exception’s source and the propagation
path.
The annotated version of the exception call graph
(ECG) is known as the exception propagation graph (EPG).
Both, ECG and EPG, are directed labeled graphs potentially
containing cycles.
To support static and dynamic reasoning about exception
ﬂow in object oriented languages a general model of excep-
tion handling structures and their occurrence in a program’s
calling hierarchy is presented (hence referred to as excep-
tion call graph model - ECGM). The goal of the model is
to provide a uniﬁed and sound basis for discussing prob-
lems related to the design and implementation of exception
handling mechanisms. Furthermore it eases reasoning about
exception handling related problems by abstraction. The ex-
ception call graph’s and the exception propagation graph’s
structures are based on this model. The model is adapted
from the work by Schaefer and Bundy[21] and closely re-
lated to the work by Robillard and Murphy[19]. The focus
of the model is on the description of all entities required for
the modeling of exception propagation in a program. The
model is depicted in ﬁgure 3 and a detailed description is
given below.
In the structural exception call graph model (ECGM) ob-
ject oriented language constructs are mapped to model enti-
ties. Relationships between entities are modeled as directed
associations and compositions. Classes and methods are
Figure 3. Exception Call Graph Model
simply mapped to classes and methods in the model where
one class is composed of zero to n methods and a method
belongs to exactly one class. According to the UML-meta-
model all “has-a”-relationships in the model are strong as-
sociation relationships corresponding to compositions in the
UML meta-model. A composition has a strong life cycle
dependency between instances of the container entity and
instances of the contained entity. A method in the ECGM
always corresponds to exactly one scope. A scope is de-
ﬁned as an atomic control ﬂow sphere. Every exception
encountered within scope not associated to a handler ﬂows
to the boundary of the scope without further modifying the
control ﬂow of the program. In the following an expres-
sion potentially raising an exception is referred to as failable
expression - this includes e.g. arithmetic expressions rais-
ing arithmetic exceptions such as division by zero or throw
statements raising new exceptions. A scope consists of zero
to n method calls and zero to n failable expressions. A scope
potentially contains zero to n further guarded scopes. A
”guarded” scope is deﬁned as a scope explicitly preventing
(or catching) explicitly deﬁned exceptions from propagat-
ing to the enclosing scope. In the exception graph model a
guarded scope manifests itself by strongly associating one
to n exception handler entities. Handlers and failable ex-
pressions are assigned to exactly one scope and are directly
associated with an exception entity expressing the excep-
tion raised or handled respectively. Every handler contains
a new default scope. Exceptions are associated to them-
selves to represent the exception type hierarchy. A method
call is associated to exactly one method. Possibly excep-
tions propagated by a method call are mapped by the transi-
tive relation between method, scope and all containing enti-
ties. To ease the understanding of the model and to support
reasoning about exception propagation some deﬁnitions are
given below:
• scope s = (Cs, Fs, Ss, Hs) where Cs is the set of all
method calls directly contained in the scope s, Fs is the
set of all failable expressions directly contained in the
scope s, Ss is the set of all scopes directly contained
6


in the scope s, Hs is the set of all handlers associated
with scope s
• (sD) = the default scope not associated with a handler
• method m = (sD) where sD is the default scope
• handler h = (sD) where sD is the default scope
• failable expression f := expression potentially raising
an exception
• call c := control ﬂow transition to a method
• exception e := entity representing an exceptional con-
dition
• Ex = {e|e raised in the context of x}
Furthermore, some functions are deﬁned as follows:
encounters : S →E
(1)
encounters(s) =
raises(s) ∪propagates(s) ∪uncaught(s)
(2)
raises : S →E
(3)
raises(s) =
[
∀f∈Fs
raises(f)
(4)
where raises(f) = {e|e ∈Ef}
(5)
propagates : S →E
(6)
propagates(s) =
[
∀c∈Cs
propagates(c)
(7)
where propagates(c) = encounters(sD)
(8)
uncaught : S →E
(9)
uncaught(s) = encounters(s) −catch(s)
(10)
catches : S →E
(11)
catches(s) =
[
∀h∈Hs
chatches(s)
(12)
where catches(h) = {e|e ∈Eh}
(13)
To illustrate how the exception handling mechanisms
and the calling hierarchy of a real programming language
are mapped onto the general exception call graph model
and to ease the understanding of the concepts proposed in
the rest of this paper, the Java language constructs are de-
scribed in terms of the general model. In Java every class
and method corresponds to a class and method entity in the
exception call graph model. A Java method spans the de-
fault outer scope. Every try-block within the method (outer
scope) is mapped to a guarding scope associated to the cor-
responding exception handler entities. Every try-block may
contain further try-blocks expressed by nesting scopes in
the model. A handler in the model corresponds to a catch-
block in Java; the associated exception matches the excep-
tion caught by the catch expression. A handler spans a new
default scope possibly containing further guarded scopes
(aka try-blocks). A Java method or try-block in general con-
tains method calls or failable expressions. Failable expres-
sions in Java are expressions implicitly or explicitly rais-
ing exceptions. Explicitly raised exceptions correspond to
throw statements; implicitly raised exceptions correspond
to exceptions that can be raised by the runtime as shown in
the Java Language Speciﬁcation[7]. A method call propa-
gates all exceptions possibly encountered within a method‘s
scope and a method scope’s child scopes that are uncaught.
The mapping of Java language constructs to the exception
call graph model is informally summarized in the following:
• Java class →ECGM class
• Java method →ECGM method + ECGM scope
• Java try-block →ECGM scope
• Java catch →ECGM handler
• Java exception →ECGM exception
• Java potentially exception raising expression →
ECGM failable expression
• Java method call →ECGM method call
• Java ﬁnally-block →ECGM scope
• Java throw statement →ECGM failable expression
Basically, the ECG’s and EPG’s structure is based on the
exception call graph model. Graph node types correspond
to the entities described by the model. Graph edges are
modeled by associations within the ECGM. Deriving the
ECG from the abstract syntax tree is a straight forward ap-
proach. The abstract syntax tree is parsed and the required
information is extracted. According to the mapping rules
described above step by step the statements in the abstract
syntax tree are parsed and new nodes with corresponding
directed edges are inserted. The exception hierarchy is di-
rectly derived from the abstract syntax tree as well. Finally,
the ECG represents a program’s calling hierarchy consisting
of class, method and scope nodes mainly. Method calls are
represented by directed edges to the corresponding method
7


nodes. Exceptions raised explicitly or implicitly or caught
are embodied by directed edges to the adequate exception
nodes.
To support reasoning about exception propagation the
ECG containing the required exception and call structure
of a program as described above is analyzed and annotated
with exception path information (epi). Of course, the ex-
ception path information contains the exception type as well
as the exception source. If an exception is propagated the
exception path information includes the exception propaga-
tion path according to the calling hierarchy. According to
[4] the exception path information is formally described as:
epi = exception × propagation path
(14)
where exception = exception identiﬁer × expression
and propagation path = method*
(15)
To annotate the exception path information to the exception
call graph the following algorithm is applied. Starting from
the exception nodes the directed edges are traced back and
the exception path information is annotated to the edges.
Reaching a node, the exception path information contained
in all the node’s outgoing edges is subsumed and exceptions
handled by a corresponding handler are removed building a
node’s exception path information set (epis). Consequently,
every node is annotated with a set of potentially raised ex-
ceptions containing the exception source and propagation
path. All the node’s incoming edges are traced back again
and the edges are annotated with the exception path infor-
mation subsumed in the node’s exception path information
set. This algorithm is repeated until the system’s entry point
is reached. The exception propagation information set at
the root node (system entry point) exactly shows which ex-
ceptions are potentially propagated beyond the scope of the
system and exactly show the exceptions’ origins and prop-
agation paths. A pseudo code illustration of this simpliﬁed
algorithm is depicted in listing 1.
The algorithm described in listing 1 is simple and
straight forward and terminates for acyclic graphs. But gen-
eral calling hierarchies as represented by the ECG might
contain cyclic references – i.e. programs containing recur-
sive or cyclic method calls. If a graph contains cycles the
algorithm shown above will not terminate. An improved an-
notation algorithm has to mark already visited nodes to de-
tect cyclic relationships and stop to follow such paths again.
The exception call graph (ECG) and exception propagation
graph(EPG) respectively can be regarded as a deterministic
ﬁnite state machine or automata (DFA) represented by the
5-tupel A = (Q, Σ, δ, q0, F) [11], where
• Q is the ﬁnite set of states represented by methods
• Σ is the ﬁnite set of symbols represented by method
calls
1
Start at every exception node
2
Annotate the exception path information(-
sets) to all incoming edges
3
Trace back all incoming edges
4
Reaching a node, adapt and extend exception
path information according to:
5
switch (node.type) {
6
case failable expression:
7
add expression information
to the exception path
information
8
case method:
9
add method information to
the exception path
information
10
case handler:
11
negate exception path
information
12
}
13
Build a set from all incoming exception
path information(-sets) excluding
negated exception path information (
considering sub-typing!)
14
Continue with step in line 2
15
The algorithm stops when reaching the entry
point
Listing 1. Exception Propagation Information
– Annotation Algorithm
• δ is the transition function δ : Q × Σ →Q
• q0 is the start state
• F is a set of states of Q (i.e. F ⊆Q)
Finite state machines are closely related and correspond
to regular expressions. Regular expressions can be seen as
algebraic descriptions of languages. It can be proved that if
L = L(A) for an arbitrary DEA A there is a corresponding
regular expression R with L = L(R) where L is a language
over Σ [11]. Consequently, the propagation path expres-
sions can easily be expressed by using regular expressions
representing the potentially cyclic subgraph.
Basically, in this subsection a novel graph-based ap-
proach to exception ﬂow analysis was presented. A graph
representation (exception call graph) of a program’s calling
hierarchy, related exceptions and exception handlers are de-
rived from the abstract syntax tree. To support reasoning
about exception propagation this graph structure is anno-
tated with exception path information resulting in the ex-
ception propagation graph. This interrelation is depicted
schematically in ﬁgure 4.
8


Figure 4. Exception Flow Analysis
1
class MyDemo{
2
public static void main(String[] args )
throws E2 {
3
try {
4
myMethod1( );
5
} catch (E1 e) { ; }
6
. . .
7
myMethod3( );
8
}
9
void myMethod1( ) throws E1{
10
myMethod2( );
11
}
12
void myMethod2( ) throws E1{
13
throw new E1();
14
}
15
void myMethod3( ) throws E2 {
16
if (...) throw new E2();
17
if (...) myMethod3( );
18
}
19
}
Listing 2. Java Code Example
To ease the understanding of the static code analysis pro-
posed in this paper a small Java code fragment is given in
listing 2.
The annotated exception propagation graph correspond-
ing to the Java code fragment shown in listing 2 is illustrated
in ﬁgure 5.
3.2.2
Runtime Issues – Dynamic Fault Containment
As already illustrated there is a strong need for default ex-
ception handling mechanisms located on a software layer
below the application layer itself. These default mecha-
nisms are not meant not replace customized application spe-
ciﬁc exception handlers but complement them. When an ex-
ception is raised during runtime the possibly affected data
structures have to be detected directly. This means the iden-
tiﬁcation has to be performed before the exception objects
are created and especially before the exception objects are
propagated along the stack trace. It is not sufﬁcient to only
identify object types but speciﬁc object instances. During
runtime when the exception is raised object references to
all affected data structures have to be collected by a system
mechanism. This feature has to be supported by the pro-
Figure 5. Exception Propagation Path Exam-
ple
gram language’s runtime environment. The information on
the affected data structures are added to the information in
the exception objects. Today exception objects mainly in-
clude stack trace information used for debugging purposes
when an exception leads to a system crash. Extending ex-
ception objects with references to the affected data struc-
tures will help in developing reasonable exception handling
mechanisms. Often, context information to understand the
exception on a higher abstraction level is missing anyway.
Besides the information that something went wrong sig-
naled by an exception, information on affected data struc-
tures is essential.
After the data structures have been identiﬁed, client ac-
cess has to be prevented or restricted automatically. Pro-
tective wrappers guarding the access have to be built
around the quarantine areas dynamically during runtime.
In a ﬁrst prototype implementation the wrapping of data
structures can be achieved by providing or enhancing ob-
jects with constraints. These constraints implemented as
preconditions[10, 16] are true by default and can be adapted
during runtime. If the access to an object is to be prevented,
the precondition is simply changed to false. Between these
two extremes – full access and no access – arbitrary ac-
cess restrictions embodied by formal boolean expressions
are possible. If an exception can be assigned to client’s
wrong input parameters for example, further calls with the
same parameters can be blocked by including the parame-
ters into the precondition. The constraints deﬁned for each
object must be maintained during execution unless they are
explicitly waived by the application. If a client application’s
access to a guarded object is declined a default exception
has to be raised. Every client commits to catch and handle
this default exception.
For every exception raised during runtime an analysis
can be performed to check if a corresponding exception
handler exists on the exception’s way up the stack trace.
9


This runtime analysis is based on the exception propagation
graph (EPG) resulting from the static code analysis intro-
duced in the section on static code analysis. Basically, the
exception identiﬁer (of the exception currently raised) has
to be concatenated with the stack trace information repre-
senting the call path to the system point where the excep-
tion has been raised. Combining these two pieces of infor-
mation results in an expression type similar to the excep-
tion path information introduced above (epi = exception ×
propagation path). As described earlier every node in the
exception propagation path is annotated with a regular ex-
pression representing the exception path. To analyze if an
exception currently raised will be caught on it’s way up the
stack trace, this exception’s actual exception path simply
has to be matched to the set of exception path regular ex-
pressions (epis) at the root node of the system or component
respectively. The exception path information set contains
all exceptions with the corresponding exception sources and
propagation paths propagated beyond the analyzed node in
the calling hierarchy.
Consequently, if no match can be
found the exception is deﬁnitely caught by a correspond-
ing handler on the propagation path and vice versa. The
matching can be easily achieved by a generated ﬁnite state
machine representing the regular expression. The exception
path to be matched can be regarded as a word in the sense
of formal languages that has to be accepted by the ﬁnite
state machine describing the language[11]. If there is no
match at the root node of the system it is assured that the
exception is handled by an application-level exception han-
dler. In this case the exception is propagated up the stack
trace as usually done in today‘s exception handling mecha-
nisms. After handling the exception in the application-level
exception handler the automatic fault containment has to be
revoked by removing the guarding wrappers. If a match can
be found it is assured that the exception will not be caught
on it’s way up the stack trace. In this case two steps have
to be taken – graceful degradation by restricting access to
affected data structures and transforming the uncaught in-
compatible exception into a compatible default exception.
The former step has already been initialized directly after
the exception was raised. Transforming the exception into
a default exception and adding references to affected data
structures is straight forward. Again a client has to commit
to catch the default exception.
During the life cycle of a system fault containment data
accumulates. This data has to be cleaned up by a kind of
garbage collection. As already explained wrappers related
to exceptions already handled can be removed directly. Fur-
thermore a mechanism to store fault containment data is re-
quired to persist this information. Housekeeping and per-
sistence are in the scope of further investigation.
4
Conclusion
Exception handling is often not considered high priority
when developing software systems. Systematic exception
handling strategies and tool support for reasoning about ex-
ception ﬂow and exception compatibility between compo-
nents are rare. Accidents such as the Ariane 5 crash illus-
trate the possible impact of inappropriate exception han-
dling on the overall system dependability.
In program-
ming languages such as Java compilers help in reasoning
about exception ﬂow. Nevertheless many problems such as
unchecked exceptions or long exception propagation paths
have to be detected and resolved by the developers manu-
ally during the development process and even still persist
undetected in deployed software systems.
In this paper a novel approach to systematic exception
handling based on a sound exception model is presented.
Reasoning about exception propagation within applications
using a graph-based static code analysis approach is em-
phasized. The overall objective of the graph-based analysis
approach is the identiﬁcation of exception related problems
such as uncaught exceptions and long exception propaga-
tion paths. Based on a program’s abstract syntax tree the ex-
ception call graph (ECG) is derived – a graph representation
of the calling hierarchy, raised exceptions, the exception hi-
erarchy, exception handlers and their interrelationship. The
exception call graph is extended with annotations represent-
ing exception propagation paths resulting in the exception
propagation graph (EPG). The exception propagation graph
directly reveals problems such as uncaught exceptions. Fur-
thermore, the EPG supports dynamic fault containment dur-
ing runtime detecting, collecting and isolating ”infected”
data structures. The concepts proposed in this work are ap-
plicable to any object-oriented programming language that
deﬁnes exceptions as objects. The following listing brieﬂy
summarizes the contribution of this work:
• a novel graph-based exception analysis approach based
on static code analysis
• a novel concept improving current exception handling
mechanisms by extending programming language’s
exception handling constructs
• a novel generic fault containment approach proposed
as a system-level default exception handling mecha-
nism based on the concept of graceful degradation
Future investigations will focus on:
• the development of a graph-based static code analysis
tool,
• the implementation of the generic fault containment
mechanism and
10


• the evaluation of the concepts introduced in this paper
by applying them to sample applications tested under
various injected fault conditions.
References
[1] M. Abadi and L. Cardelli. A Theory of Objects. Monographs
in Computer Science. Springer, 1996.
[2] A. Avizienis, J.-C. Laprie, B. Randell, and C. E. Landwehr.
Basic concepts and taxonomy of dependable and secure
comput. IEEE Trans. Dependable Sec. Computing, 1(1):11–
33, 2004.
[3] P. A. Buhr and W. Y. R. Mok. Advanced exception han-
dling mechanisms. IEEE Trans. Softw. Eng., 26(9):820–836,
2000.
[4] B.-M. Chang, J.-W. Jo, and S. H. Her. Visualization of ex-
ception propagation for java using static analysis. page 173,
2002.
[5] B.-M. Chang, J.-W. Jo, K. Yi, and K.-M. Choe. Interproce-
dural exception analysis for java. In SAC ’01: Proceedings
of the 2001 ACM symposium on Applied computing, pages
620–625, New York, NY, USA, 2001. ACM.
[6] J. B. Goodenough. Exception handling: issues and a pro-
posed notation. Commun. ACM, 18(12):683–696, 1975.
[7] J. Gosling, B. Joy, G. Steele, and G. Bracha.
Java(TM)
Language Speciﬁcation, The (3rd Edition) (Java Series).
Addison-Wesley Professional, July 2005.
[8] N. Heintze and J. Jaffar. Set constraints and set-based anal-
ysis. pages 281–298, 1994.
[9] A. Hejlsberg, S. Wiltamuth, and P. Golde. C# Language
Speciﬁcation.
Addison-Wesley Longman Publishing Co.,
Inc., Boston, MA, USA, 2003.
[10] C. A. R. Hoare. An axiomatic basis for computer program-
ming. Commun. ACM, 12(10):576–580, 1969.
[11] J. E. Hopcroft, R. Motwani, and J. D. Ullman. Introduc-
tion to Automata Theory, Languages, and Computation (3rd
Edition). Addison-Wesley Longman Publishing Co., Inc.,
Boston, MA, USA, 2006.
[12] J.-M. J´ez´equel and B. Meyer.
Design by contract: The
lessons of ariane. Computer, 30(1):129–130, 1997.
[13] J.-W. Jo, B.-M. Chang, K. Yi, and K.-M. Choe.
An un-
caught exception analysis for java. J. Syst. Softw., 72(1):59–
69, 2004.
[14] N. G. Leveson and C. S. Turner. An investigation of the
therac-25 accidents. Computer, 26(7):18–41, 1993.
[15] J. Lions. Ariane 501: Report by the inquiry board. 1996.
[16] B. Meyer.
Applying ”design by contract”.
Computer,
25(10):40–51, 1992.
[17] R. Miller and A. Tripathi. Issues with exception handling
in object-oriented systems. Lecture Notes in Computer Sci-
ence, 1241:85–103, 1997.
[18] M. P. Robillard and G. C. Murphy. Analyzing exception ﬂow
in java programs. SIGSOFT Softw. Eng. Notes, 24(6):322–
337, 1999.
[19] M. P. Robillard and G. C. Murphy. Static analysis to support
the evolution of exception structure in object-oriented sys-
tems. ACM Trans. Softw. Eng. Methodol., 12(2):191–221,
2003.
[20] B. G. Ryder, D. Smith, U. Kremer, M. Gordon, and N. Shah.
A static study of java exceptions using jesp. In CC ’00: Pro-
ceedings of the 9th International Conference on Compiler
Construction, pages 67–81, London, UK, 2000. Springer-
Verlag.
[21] C. F. Schaefer and G. N. Bundy. Static analysis of exception
handling in ada. Softw. Pract. Exper., 23(10):1157–1174,
1993.
[22] S. Sinha and M. J. Harrold. Analysis and testing of pro-
grams with exception handling constructs.
IEEE Trans.
Softw. Eng., 26(9):849–871, 2000.
[23] B. Stroustrup.
The C++ Programming Language, Third
Edition.
Addison-Wesley Longman Publishing Co., Inc.,
Boston, MA, USA, 1997.
11


