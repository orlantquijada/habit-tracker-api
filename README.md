# habit-tracker-api

---

### Start server

`docker-compose up`

---

### Install docker and docker-compose

1. `sudo pacman -Syu`
2. `sudo pacman -S docker`
3. `sudo systemctl start docker.service`
4. `sudo systemctl enable docker.service`
5. `sudo pacman -S docker-compose`

---

### Migrate db

`docker exec -it backend_web_1 python manage.py migrate`

---

### Create superuser

`docker exec -it backend_web_1 python manage.py migrate`
