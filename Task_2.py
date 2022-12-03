"""2) Реализовать функцию,
принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город
проживания, email, телефон. Функция
должна принимать параметры как
именованные аргументы. Реализовать
вывод данных о пользователе одной
строкой."""

def user_data(firstname, lastname, 
              birth_year, life_city, user_email, 
              mobile_number):
    print(f"{firstname} {lastname}: {birth_year}"
            f" год рождения, город {life_city},"
            f" электронная почта - {user_email},"
            f" номер телефона -"
            f" {mobile_number}")

user_data(firstname = input(
                        "Введите Ваше имя: "),
                    lastname = input(
                        "Введите Вашу фамилию: "),
                    birth_year = input(
                        "Введите Ваш год "
                        "рождения: "),
                    life_city = input(
                        "Введите Ваш город "
                        "проживания: "),
                    user_email = input(
                        "Введите Ваш действующий"
                        " email: "),
                    mobile_number = input(
                        "Введите Ваш действующий"
                        " номер телефона: "))