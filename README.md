# stripe_test
1. запустите БД 
- docker_compose up -d
2. Перейти в папку проекта stripe_test
- cd stripe_test
3. Установите зависимости
- pip install -r requirements.txt
4. Создайте и примините миграции
- python manage.py makemigrations
- python manage.py migrate
5. Скопируйте файл .env_example под именем .env
- cp .env_example .env
6. Напишите туда свои stripe ключи (приватный и публичный)
7. Запустите проект
- python manage.py runserver 
8. Для создания superuser'a, скопируйте файл .env_example, который возле docker-compose под именем .env
- cp .env_example .env