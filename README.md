# Project "World.It-Messenger"
## Navigation | Навігація:
> [!TIP]
> - [Team Members | Delevopers](#team-members--delevopers--склад-команді)
> - [Purpose of creating the project](#purpose-of-creating-the-project--мета-створення-проекту)
> - [Technologies](#technologies--технології)
> - [Why Project "World.IT-Messenger" if useful](#why-project-worldit-messenger-if-useful--чому-проект-worldit-messenger-корисний)
____
> [!TIP]
> - [Склад команді](#team-members--delevopers--склад-команді)
> - [Мета створення проекту](#purpose-of-creating-the-project--мета-створення-проекту)
> - [Технології](#technologies--технології)
> - [Чому Проект "World.IT-Messenger" корисний](#why-project-worldit-messenger-if-useful--чому-проект-worldit-messenger-корисний)
## Team Members | Delevopers | Склад команді:
- [__Shramko Ilia__](https://github.com/IllyaShramko/World.IT-Messenger) - __Teamlead__
- [__Halkin Yehor__](https://github.com/EgorGalkinORG/Worldit-Messager)
- [__Petrenko Davyd__](https://github.com/Davidptn/WorldIt_Messenger)
- [__Koshel' Timur__](https://github.com/kosheltimur)
____
- [__Шрамко Іл'я__](https://github.com/IllyaShramko/World.IT-Messenger) - __Teamlead__
- [__Галкін Єгор__](https://github.com/EgorGalkinORG/Worldit-Messager)
- [__Петренко Давид__](https://github.com/Davidptn/WorldIt_Messenger)
- [__Кошель Тимур__](https://github.com/kosheltimur)

## Purpose of creating the project | Мета створення проекту:
### EN:
The purpose of creating this project is to practice & improve the newly learned skills of Django Framework: Django Forms, Django Class Views, Django channels (for working with WebSocket), ajax (jquery) for sending data to the backend in real time with an instant response from the server, as well as working with the iso date format to format it in local time.
____
### UA:
Мета створення цього проекту - вдосконалення навичок, які ми щонедавно почали вивчати у фреймворці Django: Django Forms, Django Class Views, Django channels (Для праці з WebSocket), ajax (jquery) для відправки даних на бек-енд у реальному часі з мгновеною відповіддю від серверу, а також робота з iso-форматом дат для форматування його у локальний час
## Technologies | Технології:
> [!NOTE]
> - Django (Python framework)
> - pillow (Python module)
> - os (Python module)
> - daphne (Python module for async work)
> - channels (Python module for websockets)
> - SQLite (Database)
> - Jquery 
> - Ajax
> - WebSocket
> - Figma (Design)
> - git 
> - GitHub
## Why Project "World.IT-Messenger" if useful | Чому Проект "World.IT-Messenger" корисний:
### EN:
- You can write & publish your ideas, thoughts and emotions
- You can create albums & upload photo in them, also you can hide any albums if you want it
- You can send a friend invitation to any user, you can also delete any user who has become your friend
- You can create groups with your friends & manage them, also you can delete any group if you is admin of group
- You can chatting with your friends in your group or personal chat in real time!
- Also you can send messeges with any photo which you upload
- You can change any your account settings: first name, surname, avatar, email, password etc.
____
### UA:
- Ви можете записувати та публікувати свої ідеї, думки та емоції.
- Ви можете створювати альбоми та завантажувати в них фотографії, а також можете приховувати будь-які альбоми, якщо хочете.
- Ви можете надіслати запрошення до друзів будь-якому користувачеві, а також видалити будь-якого користувача, який став вашим другом.
- Ви можете створювати групи зі своїми друзями та керувати ними, а також можете видалити будь-яку групу, якщо ви є адміністратором групи.
- Ви можете спілкуватися з друзями у своїй групі або особистому чаті в режимі реального часу!
- Також ви можете надсилати повідомлення з будь-якою фотографією, яку завантажуєте.
- Ви можете змінити будь-які налаштування свого облікового запису: ім'я, прізвище, аватар, електронну пошту, пароль тощо.

## Design & Structure of project | Дизайн та струтура проекту:
- ![](imgs_for_readme/Figma.png) [Figma Design](https://www.figma.com/design/20TZphWNufeAQYOe7E1sze/%D0%A1%D0%BE%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0-%D0%BC%D0%B5%D1%80%D0%B5%D0%B6%D0%B0-World-IT?node-id=6-26&t=6FcZEGOAfhm7mSQr-1)
- ![](imgs_for_readme/Figma.png) [FigJam Structure Project](https://www.figma.com/board/mj00RE7J6heFJIns5p0ybI/Untitled?node-id=0-1&p=f&t=f77Z4xYiwBP9IkS4-0)
____
- ![](imgs_for_readme/Figma.png) [Фігма Дизайн](https://www.figma.com/design/20TZphWNufeAQYOe7E1sze/%D0%A1%D0%BE%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0-%D0%BC%D0%B5%D1%80%D0%B5%D0%B6%D0%B0-World-IT?node-id=6-26&t=6FcZEGOAfhm7mSQr-1)
- ![](imgs_for_readme/Figma.png) [Фігджєм Структура Проекту](https://www.figma.com/board/mj00RE7J6heFJIns5p0ybI/Untitled?node-id=0-1&p=f&t=f77Z4xYiwBP9IkS4-0)

## Functionality of each application | Функціонал кожного додатка:
<details>
  <summary><b>📁 Home_app</b></summary>
  
  ---
  > 🏠 Home_app is the home page where you can find the main information about yourself and other users. You can also create a new post and attach several images to it on the topic of the post.
  --- 
  > 🏠 Home_app - це головна сторінка, де розміщується головна інформація, як про вас, так і про інших користувачів. Також на головній ви можете створити новий пост та прикріпити до нього декілька зображень на тему поста.
</details>

<details>
  <summary><b>📁 User_app</b></summary>
  
  ---
  > 👤 User_app - This application is responsible for registration, authorization, and logout. With it's help, you can see the registration and authorization pages.
  --- 
  > 👤 User_app - Цей додаток відповідає за реєстрацію, авторизацію та вихід з аккаунту. За допомогу ньому ви можете бачити сторінкі реєстрації та авторизації.
</details>

<details>
  <summary><b>📁 Chat_app</b></summary>
  
  ---
  > 💬 Chat_app - This is the main page of chats and chats themselves. By going to any chat, in the contact list, or on the right in the group list, you can write to other users and send any photos in real time using WebSocket. Also, if you are a group administrator, you can edit the name, avatar, and group users.
  
   To send a message with an attached image, we wrote the following code snippet:
    On the frontend in __chat.js__:
  ```js
    const reader = new FileReader();
    reader.onload = function(event){
        webSocket.send(JSON.stringify({
            'message': messageText,
            'img':reader.result.split(',')[1],
            'imgType':file.type.split('/')[1]
        }))
        document.getElementById("attaImg").src = ''
    }
    reader.readAsDataURL(file) 
  ```
  > Here we receive a message and an image, which we send in bits to the backend
  __consumers.py__:
  ```python
    @database_sync_to_async
    def save_message_to_db(self, text_data):
        data = json.loads(text_data)
        message_text = str(data["message"])
        try:
            img = base64.b64decode(data.get('img'))
            img_type = data.get('imgType')
            django_file = ContentFile(img, name=f'fileo.{img_type}')
            return ChatMessage.objects.create(
                content=message_text,
                author=Profile.objects.get(user=self.scope['user']),
                chat_group=ChatGroup.objects.get(pk=self.room_group_name),
                attached_image = django_file
            )
        except:
            return ChatMessage.objects.create(
                content=message_text,
                author=Profile.objects.get(user=self.scope['user']),
                chat_group=ChatGroup.objects.get(pk=self.room_group_name)
            )
  ```
  > Here we get our message and its properties from text_data. Then we try to decode the image, if there is none we create a standard message without the image. If the decoding is successful, we create a file object with its name and type. We pass this file object to attached_image
  --- 
  > 💬 Chat_app - Це головна сторінка чатів та саме чати. Перейшовши в будь-який чат, у списку контактів, або справа у списку груп, ви можете писати іншим користувачам та відправляти будь-які фото у реальному часі за допомогую WebSocket. Також ви, якщо є адміністратором групи, можете редагувати ім'я, аватар, користувачів групи.
  
   Щоб відправляти повідомлення з прикріпленним зображенням, ми написали такий фрагмент коду:
   На фронтенді у __chat.js__:
  ```js
    const reader = new FileReader();
    reader.onload = function(event){
        webSocket.send(JSON.stringify({
            'message': messageText,
            'img':reader.result.split(',')[1],
            'imgType':file.type.split('/')[1]
        }))
        document.getElementById("attaImg").src = ''
    }
    reader.readAsDataURL(file) 
  ```
  > Тут ми отримуємо повідомлення та картинку, яку відправляємо у бітах на бекенд
  __consumers.py__:
  ```python
    @database_sync_to_async
    def save_message_to_db(self, text_data):
        data = json.loads(text_data)
        message_text = str(data["message"])
        try:
            img = base64.b64decode(data.get('img'))
            img_type = data.get('imgType')
            django_file = ContentFile(img, name=f'fileo.{img_type}')
            return ChatMessage.objects.create(
                content=message_text,
                author=Profile.objects.get(user=self.scope['user']),
                chat_group=ChatGroup.objects.get(pk=self.room_group_name),
                attached_image = django_file
            )
        except:
            return ChatMessage.objects.create(
                content=message_text,
                author=Profile.objects.get(user=self.scope['user']),
                chat_group=ChatGroup.objects.get(pk=self.room_group_name)
            )
  ```
  > Тут ми отримуємо з text_data наше повідомлення та його властивості. Потім ми пробуємо декодувати зображення, якщо його немає ми створюємо стандартне повідомлення без зображення. якщо декодування має успіх, ми створюємо об'єкт файла з його ім'ям та типом. Цей об'єкт файла ми передаємо у attached_image
</details>

<details>
  <summary><b>📁 My_posts_app</b></summary>
  
  ---
  > 🗒 My_posts_app - This is the page of your posts that you have created over time. On this page you can edit or delete any post you have created.
  --- 
  > 🗒 My_posts_app - Це сторінка ваших постів, які ви створювали за весь час. На цій сторінці ви можете редагувати, або видалити будь-який створенний вами пост.
</details>

<details>
  <summary><b>📁 friends_app</b></summary>
  
  ---
  > 👥 friends_app - On this page you can see your friends, as well as other users who are not your friends yet. If you click on another user's card, you can see their full profile (Albums, posts).
  --- 
  > 👥 friends_app - На цій сторінці ви можете побачити ваших друзів, а також інших користувичів, які ще не стали вашими друзями. Якщо натиснете на карточку іншого користувача, ви можете побачити його повний профіль (Альбоми, пости).
</details>

<details>
  <summary><b>📁 Settings_app</b></summary>
  
  ---
  > ⚙ Settings_app - Here you can change any of your settings: avatar, first name, last name, email, password, birthday - all of this can be changed according to your wishes. 
  > You can also go to your albums page from the settings. There you can create new albums, or vice versa, edit or delete existing albums. You can attach as many images as you want to the albums.
  --- 
  > ⚙ Settings_app - Тут ви можете змінювати будь-які ваши налаштування: аватар, ім'я, прізвище, пошту, пароль, день народження - це все можно змінити за вашим побажанням.
  > Також з налаштувань ви можете перейти на сторінку ваших альбомів. Там ви можете створювати нові альбоми, або навпаки, редагувати, видалити вже існуючи альбоми. До альбомів ви можете прикріпити кілька завгодно зображень.
</details>

## How to launch a project on your own PC | Як самостійно запустити проект на власному комп'ютері:
