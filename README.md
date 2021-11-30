# Mastermind Challenge by LSC
## To Run
You have two options:
1)  Navigate to the 'mastermind_by_LSC' folder
	Install with 'pip install .' 
	then run with 'mastermind-terminal'
2)  Navigate to the 'mastermind_by_LSC\mastermind' folder
	then run 'pip3 install -r requirements.txt'
	then run with 'python mastermind_teminalUI.py'

## Build and Thought Process

My build Process:

1. Think through the major components that I wanted to have in the program
2. Build the basic components
3. Improve the user experience
4. Refactor the code for efficiency
5. Add more features as time permits

I originally wanted to build in more features right from the onset. After starting a build that had server capabilities, I realized that it was more important to ship a working product rather than something that may contain bugs. Thus, my process focused on creating a simple functioning version. I looked at the requirements and refactored my thinking accordingly.

For the user-interface I decided to go with terminal input to make sure that a usable product would be sent on time. The intent was to avoid a broken program due to user interface. However, I did write the code so that classes, modules, and functions could be used by user-interface program when it was built.

The final step for me was going through and refactoring my code. I tried to encapsulate more of the stand-alone functions into classes. I also looked for ways to make the code as efficient as possible. Both of these processes were part of the redesign aimed to be used by a UI program. To this end, I broke the code into the core and the terminalUI.


## Features I would like to add:
1.  Implement the UI component. (This is mostly built but shipping the code was more important.)
	* The first two components are first on the list so that my son can easily play the game.
2. Add the ability to change to colors or even symbols. 
	* Built out a UI version of the colors but struggled with getting the letters to show up on the pegs. 
	** This was important to me, because my father-in-law is color blind and I want the game to be more accessible.

3. Add the option to add more difficulty. 

4. Add the ability for two players to play remotely. (Server)
	* Local remote option (local server)
	* True remote (remote server)
5. Add a computer opponent that guesses
6. Package the game to be playable via .exe 
7. Create a web-based version
