# Instructions

## Structure of Kit

In each kit, there are three possible paths. The game starts with a case summary, and then presents a riddle to the user.
Each of the answers to the riddle are correct; however, they each lead down a different path: science, technology, and engineering.
Each of the paths has an ample amount of math throughout. The answers to the riddle are the three possible passwords to the "central computer".
Depending on which password is used, a different set of files will be provided.

### Central Computer
The username to the computer will be clearly provided via a sticky note on the back fo the case summary. Users will see the below 
sign in screen when starting the game.

![](/images/login_screen.png)

Once the username "ecarter1997" is entered, the program will prompt the user for a password. One of the three possible passwords
are entered, and then the user is signed in to a "fake" terminal environment. Possible commands can be displayed by typing `help`

The user will see the following output:
```aiignore
AVAILABLE COMMANDS

help              Show available commands
ls                List files
cd <folder>       Change directory
view <file>       View a file in the terminal
unlock <file>     Unlock a protected file (prompts for a password)
clear             Clear the terminal
logout            Log out
```

The terminal environment allows the user to become familiar with a real UNIX-based terminal. Commands are almost the same,
with only `view` being different than its real counterpart, `cat`. Also, `unlock` is not a real command in a UNIX terminal,
but is integral to the mechanics of the game.

#### Example:
When the user loads in to the terminal environment, it is possible to type on a line that looks like:
```aiignore
ecarter1997@subterranean:/>
```
This structure mimics a real terminal. The recommended first command to type is `help`, followed by the `ls` command.
when the user uses the `ls` command, they will see the readout:
```aiignore
ecarter1997@subterranean:/> ls
[FOLDER] 1-messages
[FOLDER] 2-protocols
```

Using the `cd <folder>` command, we can enter different directories. For example, we can use the command to enter the `1-messages` 
directory and then use `ls` to see what's inside:
```aiignore
ecarter1997@subterranean:/> cd 1-messages
ecarter1997@subterranean:/1-messages> ls
[FILE]   RE_the_thing.txt
[LOCKED] last_email.txt
[LOCKED] material_req_1.txt
```
Now, we see the contents of the `1-messages` directory. We also see that two of the `.txt` files are LOCKED. This is where the 
`unlock` command comes into play. If the user tried to `view` one of the locked files, they would get the output:
```aiignore
ecarter1997@subterranean:/1-messages> view last_email.txt

ACCESS DENIED
This file is password protected.
Try: unlock last_email.txt
```

Following the provided `Try: unlock last_email.txt`, we get prompted to enter a password. The actual password for the file 
is found through clues found in the documents provided at the beginning of the puzzle. Here's the output:
```aiignore
ecarter1997@subterranean:/1-messages> unlock last_email.txt
PASSWORD: password

ACCESS GRANTED
last_email.txt unlocked.
```
Now, we see in the `ls` output that teh file is no longer LOCKED:
```aiignore
ecarter1997@subterranean:/1-messages> ls
[FILE]   RE_the_thing.txt
[FILE]   last_email.txt
[LOCKED] material_req_1.txt
```
Therefore, the view command will now work:
```aiignore
ecarter1997@subterranean:/1-messages> view last_email.txt

Item Content
===============

*Secret Game Content*

===============
End of Item Content
```
This is a general overview of the features of the program.
