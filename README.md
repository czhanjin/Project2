# BE5140 Project2 Social robot

cronjob -a

0 20 * * * export DISPLAY=:0 && export XAUTHORITY=/home/awsuvarna/.Xauthority && /usr/bin/python3 /home/awsuvarna/Project2/luckycat_dailyquestionnaire.py >> /home/awsuvarna/Project2/questionnaire_log.txt 2>&1
0 8,9,10,12,19,20 * * * export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/control-servo.py >> ~/Project2/questionnaire_log.txt 2>&1
0 12 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Activity_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
0 8,19 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Teeth_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
0 9 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Shower_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
0 10 * * * export DISPLAY=:0 && export XAUTHORITY=~/.Xauthority && /usr/bin/python3 ~/Project2/Medicine_reminder_final.py >> ~/Project2/questionnaire_log.txt 2>&1
