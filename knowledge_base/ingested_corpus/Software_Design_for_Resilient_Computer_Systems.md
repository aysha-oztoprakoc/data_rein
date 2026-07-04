# Software Design for Resilient Computer Systems.pdf

Accessibility Information
Authors:
Overview
Igor Schagaev , Eugene Zouev , Kaegi Thomas
15k Accesses
3 Citations
Log in
Outlines potential critical faults in the modern computer systems and what is required to
change them
Explains how to design system software for next generation computers with wider
applications and greater efficiency
Presents how implemented system software support makes maintenance easier, while
reliability and performance increase
With new chapters on computer system performance, resilience and resilient architecture
simulators and system software
Software Design for Resilient Computer Systems
Book
© 2020
2nd edition
View latest edition
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
1/10


 This is a preview of subscription content, log in via an institution
 to check access.
Access this book
eBook
USD 89.99
Price excludes VAT (Brazil)
Tax calculation will be finalised at checkout
Other ways to access
Licence this eBook for your library 
Institutional subscriptions 
About this book
This book addresses the question of how system software should be designed to
account for faults, and which fault tolerance features it should provide for highest
reliability. With this second edition of Software Design for Resilient Computer
Log in via an institution
Available as EPUB and PDF
Read on any device
Instant download
Own it forever
Buy eBook 
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
2/10


Systems the book is thoroughly updated to contain the newest advice regarding
software resilience. With additional chapters on computer system performance
and system resilience, as well as online resources, the new edition is ideal for
researchers and industry professionals.
The authors first show how the system software interacts with the hardware to
tolerate faults. They analyze and further develop the theory of fault tolerance to
understand the different ways to increase the reliability of a system, with special
attention on the role of system software in this process. They further develop the
general algorithm of fault tolerance (GAFT) with its three main processes:
hardware checking, preparation for recovery, andthe recovery procedure. For each
of the three processes, they analyze the requirements and properties theoretically
and give possible implementation scenarios and system software support
required. Based on the theoretical results, the authors derive an Oberon-based
programming language with direct support of the three processes of GAFT. In the
last part of this book, they introduce a simulator, using it as a proof of concept
implementation of a novel fault tolerant processor architecture (ERRIC) and its
newly developed runtime system feature-wise and performance-wise.
Due to the wide reaching nature of the content, this book applies to a host of
industries and research areas, including military, aviation, intensive health care,
industrial control, and space exploration.
Explore related subjects
Discover the latest articles, books and news in related subjects.
Communications Engineering, Networks
Electronic Circuits and Systems
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
3/10


Hardware Performance and Reliability
Software Engineering
Security Science and Technology
Fault Tolerance Techniques in Computing Systems
Search within this book
Table of contents (20 chapters)
Search
Front Matter
Pages i-xviii
Download chapter PDF 
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 1-6
Introduction
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 7-10
Hardware Faults
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 11-23
Fault Tolerance: Theory and Concepts
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
4/10


Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 25-46
Generalized Algorithm of Fault Tolerance (GAFT)
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 47-57
GAFT Generalization: A Principle and Model of Active System Safety
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 59-69
System Software Support for Hardware Deficiency: Functions and Features
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 71-110
Testing, Checking, and Hardware Syndrome
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 111-140
Recovery Preparation
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 141-152
Recovery: Searching and Monitoring of Correct Software States
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Recovery Algorithms: An Analysis
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
5/10


Pages 153-164
Eugene Zouev
Pages 165-175
Programming Languages for Safety-Critical Systems
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 177-192
Proposed Runtime System Structure with Support of Resilient Concurrency
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 193-195
Proposed Runtime System Versus Existing Approaches
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 197-205
Hardware: The ERRIC Architecture
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 207-213
Architecture Comparison and Evaluation
Igor Schagaev, Eugene Zouev, Kaegi Thomas
Pages 215-219
ERRIC Reliability
On Performance: From Hardware up to Distributed Systems
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
6/10


Authors and Affiliations
IT-ACS Ltd, Stevenage, UK
Igor Schagaev, Kaegi Thomas
Department of Informatics, Technopolis, Innopolis, Kazan, Russia
Eugene Zouev
About the authors
Dr. Igor Schagaev is a Professor and Director of IT-ACS Ltd (UK). He is a Fellow of
the Institute of Analyst and Programmers (UK), Fellow of British Computer
Society (UK). His career has started  as an Electromechanical Engineer at the 
Igor Schagaev, Hao Cai, Simon Monkman
Pages 221-247
Igor Schagaev
Pages 249-266
Distributed Systems: Maximizing Resilience
Igor Schagaev, Stephen Farrell
Pages 267-292
Distributed Systems: Resilience, Desperation
1
2
Next
Back to top
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
7/10


Smolensk aviation factory, USSR, a Senior Programmer and Design Engineer at
the Institute of Advanced Computations, Central Bureau, Smolensk Branch, and a
Senior Design Engineer and System Programmer for Avionics. Completed PhD in
Russian Academy of Science (Institute of Control Science) and involvement in
projects of hardware and software for submarines, satellites and aircrafts  enables
Igor to absorb an experience which he share with Boeing in 98-99. In 1994 Igor 
has established   ATLAB Ltd Bristol now transformed into IT-ACS Ltd.  He has
published 7 books in three languages, over 60 papers, since 2006 holds
international patent on New Active System Control and supportive  mathematical 
models. ProfessorSchagaev  has been honoured with several industry awards,
achievements, and grants.
Prof Eugene Zouev is currently a professor in Innopolis University, Russia. Eugene
has graduated and defended his PhD in Moscow State University (1976 and 1999,
respectively). He was involved in many research and industrial projects in system
software, programming languages and their compilers.
Among his achievements were full ISO-compliant C++ compiler (2000, Moscow,
Russia), Zonnon language compiler for .NET (ETH Zurich 2000-2006) with and
under supervision of Prof Niklaus Wirth (Turing Award) and Prof J. Gutknecht,
and many other projects. His involvement in EU funded project (ONBASS 2004-
09) became a next step in research and development summarised to some extent
in this book.
Dr. Thomas Kaegi-Trachsel received his PhD in 2012 in ETH Zurich in the area of
system software for embedded systems (under supervision of Prof. Schagaev). He
is currently a Senior Researcher atErgon Informatics, Switzerland.
Accessibility Information
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
8/10


Accessibility information for this book is coming soon. We're working to make it
available as quickly as possible. Thank you for your patience.
Bibliographic Information
Book Title
Software Design for
Resilient Computer Systems
Authors
Igor Schagaev, Eugene
Zouev, Kaegi Thomas
DOI
https://doi.org/10.1007/97
8-3-030-21244-5
Publisher
Springer Cham
eBook Packages
Engineering, Engineering
(R0)
Copyright Information
The Editor(s) (if applicable)
and The Author(s), under
exclusive license to Springer
Nature Switzerland AG
2020
eBook ISBN
978-3-030-21244-5
Published: 09 July 2019
Edition Number
2
Number of Pages
XVIII, 308
Number of Illustrations
42 b/w illustrations, 133
illustrations in colour
Topics
Communications
Engineering, Networks,
Circuits and Systems,
Software Engineering,
Performance and Reliability,
Quality Control, Reliability,
Safety and Risk
Keywords
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
9/10


ERRIC architecture
Extreme reliability
Fault tolerance
Hardware and software reliability
Hardware and software resilience
Hardware deficiency
Hardware faults
Reliability engineering
Software for hardware efficiency
quality control, reliability, safety and risk
Publish with us
Policies and ethics
Back to top
7/2/26, 11:12 AM
Software Design for Resilient Computer Systems | Springer Nature Link
https://link.springer.com/book/10.1007/978-3-030-21244-5
10/10


