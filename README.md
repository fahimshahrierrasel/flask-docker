# Flask with Docker Boilerplate (For Development)

**Philosophy:**
People does not need to download and install and configure your environment they just need one tool called `Docker` and `Terminal` to run your app. All the environment complexity is hide behind the docker configuration.


**How to run:**
1. First need to install `Docker` obviously 
2. Open any terminal app.
3. Execute `docker-compose up --build`. (Use this command if your dependencies changed)
4. All other time just `docker-compose up`.
5. For close the app `ctrl + C` and execute `docker-compose down`.

##### App will run in [localhost:5000](http://localhost:5000)