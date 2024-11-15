**TRANSLATOR**

This Project was created to implement CI workflows as part of the repository. 

**IDEA:**

The main idea behind creating this package is to use poetry to install all the dependencies, create a test.yml to test whether the changes are working as expected. 

**HOW TO USE:**

1. Open Visual Studio Code. 
2. Clone the repository.
3. Install docker in your system. (Either through WSL or directly in your Unix Machine - https://medium.com/@tomer.klein/step-by-step-tutorial-installing-docker-and-docker-compose-on-ubuntu-a98a1b7aaed0)
4. Open the devcontainer.json
5. Use poetry install to install all the dependencies.
6. Run poetry run uvicorn translate.main:app --reload
7. You should be getting something similar to the below image

![image](https://github.com/user-attachments/assets/027fdbcc-5438-4bb0-92a6-e24df1160fec)

 
