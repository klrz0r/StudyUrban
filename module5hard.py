import time


class UrTube:
    database_users = []
    database_videos = []
    def __init__(self, current_user=None):
        self.current_user = current_user

# Функция для авторизации пользователя
    def log_in(self, nickname, password):
        for user in self.database_users:
            if user.nickname == nickname:
                if user.password == password:
                    print(f'Добро пожаловать {user}')
                    return user
                else:
                    print(f'Пользователь {nickname} уже существует')
                    return self.current_user
        if self.current_user == None:
            #print('Пользователь не найден')
            return None


#Функция регистрации пользователя
    def register(self, nickname, password, age):
        user_login = None
        user_login = self.log_in(nickname, password)
        if user_login == None:
            new_user = User(nickname, password, age)
            self.database_users.append(new_user)
            self.current_user = new_user
            #print(f'Пользователь создан! Добро пожаловать, {self.current_user.nickname}')


#Функция для разлогинивания пользователя
    def log_out(self):
        self.current_user = None
#Функция для добавления видео
    def add(self, *other):
        for video in other:
            self.database_videos.append(video)
            #print(f'Добавлено видео {video.title}')
#Функция для поиска видео
    def get_videos(self, search_word):
        search_word = search_word.lower()
        video_list = []
        for video in self.database_videos:
            if search_word in video.title:
                video_list.append(video.title)
        return video_list

#Функция для просмотра видео
    def watch_video(self, video_name):
        if self.current_user != None:
            #print(self.current_user)
            for video in self.database_videos:
                if video_name.lower() == video.title:
                    if self.current_user.age > 18 or not video.adult_mode:
                        #print(self.current_user.nickname, video.title, video.adult_mode)
                        for i in range(1, video.duration + 1):
                            time.sleep(1)
                            print("Просмотр видео на ", i, "секунде")
                        print(f'Конец видео!')
                        break
                    else:
                        print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                        break
        else:
            print("Войдите в аккаунт, чтобы смотреть видео.")





class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title.lower()
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.nickname



class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


if __name__ == '__main__':
    #user = User(input("Введите имя пользователя: "), input("Введите пароль: "), input("Укажите возраст: "))
    #print(user.nickname, user.password, user.age)
    #ut = UrTube()
    #ut.register(user.nickname, user.password, user.age)
    #print(ut.current_user.nickname)
    #ut.log_out()
    #print(ut.current_user)
    #ut.log_in(user.nickname, user.password)
    #print(ut.current_user.nickname)

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')