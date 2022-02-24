# TheVoice
 My first Django project

### Here are the requirements:
You are a part of 'The Voice' TV show production team. 
you are in charge of developing a management system to monitor the participants performance in the show.
The show has 3 types of users: an admin, mentors, and candidates.
Each candidate belongs to one of the mentors teams, while mentors on the other hand can mentor more than one team.
Each candidate gains scores for songs he/she performs.
Each performance is scored by all the mentors on a scale of 0-100 The mentor can review the scores of the candidates in his teams The admin can review the scores of all the candidates in all the teamsNotes: The project should be developed using `**Django**` on the server side.

### Tasks:
Each activity is composed of : a song name, date of performance, each mentors' score, an average score.
Create a management command to **generate fake users of all types with all the needed relations**.
Upon authentication the mentor should get a page listing the candidates in each team he mentorsClicking a candidate will display a list of all his activities, his average score, and his team's average scoreWhen an admin logins, he will view all the teams and their average scoresThe admin will be able to filter the view so only some teams will be displayed, and will be able to click each team to see its candidates activitiesWe are looking for clean code and design nothing fancy, you should write code `fast`!
