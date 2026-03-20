import pexpect
import time

child = pexpect.spawn('python3 /app/app.py', timeout=180)
child.logfile = open('output.log', 'wb')

while True:
    try:
        index = child.expect([
            'Choose option:',
            'Total.*Mixed:',
            'Enter account.*prefix:',
            'Enter password prefix:',
            'Rarity.*Put',
            'Recommended.*:',
            'Press Enter',
            'press enter',
            'continue',
            'Continue',
            pexpect.EOF,
            pexpect.TIMEOUT
        ], timeout=180)

        if index == 0:
            print("Menu → sending 1")
            child.sendline('1')
            time.sleep(3)

        elif index == 1:
            print("Mixed → sending 50")
            child.sendline('50')
            time.sleep(2)

        elif index == 2:
            print("Account prefix → sending Tin")
            child.sendline('Tin')
            time.sleep(2)

        elif index == 3:
            print("Password prefix → sending Sn")
            child.sendline('Sn')
            time.sleep(2)

        elif index == 4:
            print("Rarity → sending 2")
            child.sendline('2')
            time.sleep(2)

        elif index == 5:
            print("Speed → sending 2")
            child.sendline('2')
            time.sleep(2)

        elif index == 6 or index == 7 or index == 8 or index == 9:
            print("Continue → pressing Enter")
            child.sendline('')
            time.sleep(3)

        elif index == 10:
            print("✅ Done!")
            break

        elif index == 11:
            print("⚠️ Timeout → pressing Enter")
            child.sendline('')
            time.sleep(2)

    except Exception as e:
        print(f"❌ Error: {e}")
        break
