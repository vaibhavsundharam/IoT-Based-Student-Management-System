# IoT-Based-Student-Management-System

Project Idea

A college is a massive institution and keeping track of daily activates can be a cumbersome task, especially if paper documentation is required. We observed similar challenges in our college, where the faculties had to maintain the timetables as well as the student count. Thus, documentation on a daily basis, aggregated for all such universities like ours leads to a massive paper wastage, which saliently results in a major climatic change. Also, we observed that any important notice had to be conveyed personally, by the faculties to the students. So, we thought to develop a dulpex system that can address these challenges and also automate the procedure such that documentation and management overhead can be reduced and also saliently heal the environment. 

Objective

In this work, we propose a duplex communication system that is capable of transmitting information regarding changes in the timetable or upcoming seminar/notices to the lecture theatres. Additionally, a Graphical User Interface (GUI) will be developed from where the faculties can directly make a change and intimate students about important matters. Also, the student count will be automatically aggregated and translated back to the control room, where the faculty and Head of Department’s (HoDs) can view the number of students in each classroom. The communication channel will be established using the Internet of Things (IoT) and RF technologies to transmit the information.

Time Table Management-

•	It is vital for students to know about changes in classes and upcoming seminars.
•	But the faculties have to personally come and inform the students about these changes. 
•	Reducing the management’s overhead is one of the objectives of this project.

STUDENT COUNT-

•	In our college, the student count is documented after each lecture.
•	But going to each and every classroom can be a tedious and cumbersome work for the faculties.
•	Hence the project objective also includes addressing this challenge.

CLASSROOM MODULE-
Each classroom will be equipped with the following hardware.
1. Raspberry Pi-3
2. Atmega-8 microcontroller
3. RF transmitter and receiver module
4. Encoder IC-HT12E
5. Decoder IC-HT12D
6. LCD display
7. Switches

The switches are connected to every seat in the classroom such that if any student sits on any given seat a trigger will be received by the Atmega microcontroller.This property is exploited to make the microcontroller aware about the current student count in the classrooms. After processing this information the data is encoded by the encoder IC-HT12E. In the project we have considered a total of 8 seats/switches.This data is then transmitted across the wireless channel using a 434 kHz ASK RF modulation. At the receiver the signal is down converted to baseband frequency and decoded using IC-HT12D. The decoded information is then processed by Raspberry Pi and translated to the end user through the internet where he/she can view the student count on the GUI that we have developed. 

END USER-

The end user can be anybody, the faculties in EC control room or Head of Departments. All one require is the internet connection and he/she can get access to instantaneous student count of each classroom and also can alter the time-table and/or send some important notice to the students in the classrooms without any of the hassle. This is achieved through a Graphical User Interface (GUI) that we have developed using python coding on Pycharm software. Additionally, two separate databases are developed one on the remote PC, where the time-table entries are stored and the other on Raspberrry Pi-3 from where the student count is fetched.


