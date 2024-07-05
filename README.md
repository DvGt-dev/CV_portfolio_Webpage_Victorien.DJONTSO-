#
# My Personal Portfilio Website (Django)

Personal portfolio website made with Django framework in the backend, and with CSS, JS, and Bootstrap for the frontend. It is a dynamic site so that you can control the content of the site through the admin area

## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode


## Demo

(https://user-images.githubusercontent.com/104616403/210330707-c8607c2b-6929-435f-bb58-d3176454b4fa.gif)


## Screenshots





![image](https://github.com/DvGt-dev/CV_portfolio_Webpage_Victorien.DJONTSO-/blob/main/staticfiles/img/Capture%20d'%C3%A9cran%202024-05-22%20120847.png)

![image](https://github.com/DvGt-dev/CV_portfolio_Webpage_Victorien.DJONTSO-/blob/main/staticfiles/img/Capture%20d'%C3%A9cran%202024-05-21%20134208.png)
![image](https://github.com/DvGt-dev/CV_portfolio_Webpage_Victorien.DJONTSO-/blob/main/staticfiles/img/Capture%20d'%C3%A9cran%202024-05-19%20125227.png)




## 🔗 Links
[![linkedin](https://www.linkedin.com/feed/)](www.linkedin.com/in/djontsovictorien)


## 🛠 Skills
python, Django, Javascript, HTML, CSS...


# Hi, I'm Djontso victorien ! 👋


## Feedback

If you have any feedback, please reach out to us at dvrchipro@gmail.com


## Tech Stack

**Client:** Html, css, Bootstrap

**Server:** python, Django


## Run Locally

Clone the project

```bash
  git clone https://github.com/BurhanMohammad/Django-portfilio-website.git
```

Go to the project directory

```bash
  cd Django-portfilio-websitet
```

MAKE  Migration

```bash
  python manage.py makemigrations
```

MAKE  Migration

```bash
  python manage.py migrate     
```
Start the server

```bash
  python manage.py runserver     
```

## Docker Users

```yaml


services:

  django:
    build:
      context: /mnt/c/ggggg/dvrch/Documents/docker_directory/Django-Portfolio-website
      dockerfile: djdkf
    image: Django_Portfilio_MohammadBurhan
    ports:
      - "8000:8000"
    volumes:
      - /mnt/c/Users/gggg/Documents/docker_directory/Django-Portfolio-website:/app
    command: [python, manage.py, runserver, 0.0.0.0:8000]
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    privileged: true

  jupyter:
    build:
      context: /mnt/c/gggg/dvrch/Documents/docker_directory/jupyter
      dockerfile: jpdkf
    image: Django_Portfilio_MohammadBurhan-jupyter
    ports:
      - "8888:8888"
    volumes:
      - /mnt/c/Users/gggg/Documents/docker_directory/jupyter:/notebooks
    command: [jupyter, notebook, --ip, 0.0.0.0, --no-browser, --allow-root, --NotebookApp.token='']
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    privileged: true


# docker compose -f /mnt/c/Users/dvrch/Documents/docker_directory/Django-Portfolio-website/djcps.yml up -d
````
```Dockerfile
    FROM python:3.10.7
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install --upgrade pip setuptools wheel
    COPY . .
    RUN pip install --no-cache-dir -r requirements.txt
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

````


## Authors

- [@DJontso victorien ](https://github.com/dvgt-dev)

"# CV_portfolio_Victorien--DJONTSO" 
