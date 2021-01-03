import pyautogui
import Instadata2
import DM2_structured

pyautogui.alert('You will now be prompted to login to Instagram to continue.')
user = pyautogui.prompt('Enter your username below.')
pas = pyautogui.password('Enter your password. Text will be hidden.')
pyautogui.alert('You will now be prompted to enter the username for the target account.')
targ = pyautogui.prompt('Enter the username for the target account.')

test = Instadata2.InstaData(user, pas, targ)

while True:
    getInp = pyautogui.confirm('Please choose an action.', buttons=['Get followers', 'Get Posts','DM Bot', 'Exit'])
    if getInp == 'Get followers':
        print('Working')
        test.get_followers()
    if getInp == 'Get Posts':
        test.get_posts()
    if getInp == 'DM Bot':
        pyautogui.alert('Write usernames in file \'t_usernames.txt\'. See a sample at \'contact_sample.txt\'. Press \'Ok\' when complete.')
        pyautogui.alert('You will now be required to enter a message to be sent.')
        mes = pyautogui.prompt('Please enter a message to be sent to each specified individual.')
        DMbot = DM2_structured.DM(user, pas, mes)
        DMbot.messenger()
    if getInp == 'Exit':
        break
