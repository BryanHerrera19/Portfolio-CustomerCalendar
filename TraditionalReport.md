# Magneton Calendar
Authored by    
  - Bryan Herrera - Scrum Master - Assured that all stories were created and added to Zenhub. Also assured that each story had acceptance criteria as well as short information on its functionality.
  - Marissa Morones - Team member
  - Andrei Pelera - 
  - Kevin Lin - Team member
# Project Objectives
This project is aimed to provide a time management and study tool for students to effectively manage their time.
# Project Design
Our team goal is to create a functional calendar with features such as setting up events and reminders, a built-in study timer and tips, and saving events onto the local workstation.

Final Zenhub board:

![image](https://user-images.githubusercontent.com/43161217/236715772-31947c85-dfd9-4a1e-9736-ef0ecac2f6fe.png)

![image](https://user-images.githubusercontent.com/43161217/236720936-24187696-a50e-499b-9cb4-827f5e314455.png)

# Implementation
This project uses Python 3.10 with the tkinter and tkcalendar libraries that power the core graphical user interface and features. We also utilized Pylint to check for coding errors.     
### Challenges and Solutions
  - Having issues with certain features using Calendar module
    - Dropped the feature or found another way
    - UI would not scale properly when resized but eventually figured it out
    - Ex: Couldn’t add multiple event colors on calendar, so we left the days with events having one color
  - Pylint errors were a major problem, and we had to re-edit the code to fix said errors
    - A fix for this was that we disabled a couple of the errors
  - Difficulty ensuring all Buttons Fit
    - Buttons would overlap each other
    - Including “padx” and “pady”

# Testing
[Testing.md](Testing.md)

# Project Highlights :smiling_face_with_three_hearts:
### Our calendar and some features we are proud of:
![image](https://user-images.githubusercontent.com/43161217/236724236-80b36412-7c8c-4957-8249-d3ca50614c58.png)
<img width="466" alt="image" src="https://user-images.githubusercontent.com/55124638/232838944-343e70c5-6dc1-4535-b0b3-2ee1c9ef8283.png">
<img width="466" alt="image" src="https://user-images.githubusercontent.com/55124638/236640810-d9389808-1c6c-4434-b681-c063a40a7881.png">
### What we thought worked really well
- Great communication
- Worked to complete majority of our stories
- Helped each other 
  
### Troubles we ended up solving or finding
- Fixing and correcting Pylint errors
- Troubleshooting and resolving bugs with some features such as UI implementation and event menues.

# Retrospective
### What parts of our program we would improve
- Be able to add more QOL features a modern calendar has such as grouping events by categories or switching between dark and light mode
- when opening a menu, change ruleset to not bury the submenu when opened
### What parts of our teamwork/process that we would improve
- Be consistent with our standups
- workload more consistently spread out of the sprint rather than doing everything at the back end of the sprint

# Lessons Learned
(Advice for future COMP 129 students)

An advice we have for future COMP 129 students is to manage your sprint (and time) well. Be diligent with time management to avoid procrastination or unneeded stress if a feature implemented causes bugs the day before a demo. Giving yourselves more time to check and fix for bugs at the end of the sprint greatly increases workflow productivity and stress to all team members.
