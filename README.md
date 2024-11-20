**TRANSLATOR**

This Project was created to implement CI workflows as part of the repository

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
8. The number of languages supported at this point of time is 50 ("Arabic","Czech","German","English","Spanish","Estonian","Finnish","French","Gujarati","Hindi","Italian","Japanese","Kazakh","Korean","Lithuanian","Latvian","Burmese","Nepali","Dutch","Romanian","Russian","Sinhala","Turkish","Vietnamese","Chinese","Afrikaans","Azerbaijani","Bengali","Persian","Hebrew","Croatian","Indonesian","Georgian","Khmer","Macedonian","Malayalam","Mongolian","Marathi","Polish","Pashto","Portuguese","Swedish","Swahili","Tamil","Telugu","Thai","Tagalog","Ukrainian","Urdu","Xhosa","Galician","Slovene")

![image](https://github.com/user-attachments/assets/eda24f9f-4901-416e-9bf1-367989803569)
