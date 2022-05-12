# Cyberpunk-Runner
This is a web app that I'm making to help run Cyberpunk Red. I plan to use this to keep the game fast paced and not have to rely on constantly looking through the book

# Activating the virtual Environment
These commands are ran in WSL Ubuntu. Run these commands in this order

1: python3 -m venv venv...............Creates virtual environment

2: source venv/bin/activate...........Activates virtual environment

3: uvicorn main:app --reload.......... Activates Uvicorn server (--reload makes it so server refreshed upon commit)

To deactivate the virtual environment, just type in ctrl-c and it will stop.
