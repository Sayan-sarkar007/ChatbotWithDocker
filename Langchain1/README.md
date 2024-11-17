*** Over view or Simple documentry for langchain ( used in this project ) ***


1. Fist of all i have intalled **poetry** to have that **pyporoject.toml** file. And to have this whole Langcahin1 project. poetry helps to have all the dependency handy in .toml file. It is same as java pom file. With python everytime we have to install every librery using pip install command and later if we need something we will for surley have problem to run those using another machine and to organise everything. Insted of that we have a .toml file that exactly works as pom file. 
    To create a project with this follow the below -
    1. Open powershell(as i have installed poetry through powershell)
    2. Go to the expected folder/directory then give command **poetry new Project_Name**
    3. Open the folder using VS code and that's it. 

2. Create a .py file which you want to add the main programe. Most of the time we faced a problem as we have installed the librery using poetry still it not installed porperly rather we can say it didn't sync properly. For that just go that .py file. then follow the below steps - 
    1. below on the status bar you can find a just beside the {}python as 3.12.3... something. just click on that it will open the "Enterpreter path on search bar"
    2. type in the terminal( check if you are in the expected directory or not ) **poetry shell**, you will find a long path. just copy and paste that on the search bar in the Enterpreter section. It will automatically set up the sync.

3. create a .env file. and to install dotenv librery go for the pip install, don't know why it is not working with poetry.
    In this .env file we will sote the API keys with porper naming convension. in the time of coding we can import dotenv librery just go through the ChatbotGemin.py app you will understand. 