SET log_file=%cd%\logfile.txt
call C:\Users\Patran\Anaconda3\Scripts\activate.bat
conda activate Beehive
cd C:\Users\Patran\Desktop\Projects\Beehive\Beehive
python manage.py runscript reminder_email
pause
