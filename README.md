# BE5140 Project2 Social robot

Latest Arduino code: [Cat_dec13](https://github.com/czhanjin/Project2/tree/master/Cat_dec13)

[CAD files](https://github.com/czhanjin/Project2/tree/master/LUCKE-CAD/Frame)

[Demo Video](https://www.youtube.com/watch?v=4yg1J_LsbSY) 

To set up cron jobs in RPi, run this CLI command `cronjob -a` and fill in the following commands to set up reminders with scheduled time. Arm waving is executed simultaneously with scheduled reminders.
```
0 20 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/luckycat_dailyquestionnaire.py >> ~/Project2/questionnaire_log.txt 2>&1
0 8,9,10,12,19,20 * * * export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/control-servo.py >> ~/Project2/questionnaire_log.txt 2>&1
0 12 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Activity_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
0 8,19 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Teeth_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
0 9 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Shower_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
0 10 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Medicine_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
```
To demo a reminder with arm waving, use this cron jobs to see the behaviors every minutes:
```
* * * * * export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/control-servo.py >> ~/Project2/questionnaire_log.txt 2>&1
* * * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Medicine_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
```
