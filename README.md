# habit-tracker-api

---

### Start server

`docker-compose up`

---

### Install docker and docker-compose

1. `sudo pacman -Syu`
2. `sudo pacman -S docker`
3. `sudo systemctl start docker`
4. `sudo systemctl enable docker`
5. `sudo pacman -S docker-compose`
6. `sudo usermod -aG docker $USER`
7. reboot

---

### Migrate db

`docker exec -it backend_web_1 python manage.py migrate`

---

### Create superuser

`docker exec -it backend_web_1 python manage.py migrate`
