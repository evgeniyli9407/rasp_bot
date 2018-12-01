import config
import telebot


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "/понедельник":
        bot.send_message(message.chat.id, "Сегодня работают:" + '\r\n'+ "Женя Ли (с 8 до 17)  @Mamayavtelegrame" + "\r\n"+
                                          "Алеся Шахназарова (с 8 до 17) @lesya_shahnazarova" + "\r\n"+
                                          "Забелин Алексей(с 12 до 21) @Trikse4eg" + "\r\n"+
                                          "Никита Парадис (с 12 до 21) @mukuta88"+ "\r\n"+
                                          "Валерия Павлович (с 10 до 19) @valerka_p22"+ "\r\n"+
                                          "Артур Сайфулин (с 10 до 19) @artsayf"+ "\r\n"+
                                          "Валентин Копыцкий (с 12 до 21) @KopytskiValentin"+ "\r\n"+
                                          "Александр Алексюк (с 14 до 23) @DannyDerden")
    if message.text == "/вторник":
            bot.send_message(message.chat.id, "Сегодня работают:" + '\r\n'+
        "Женя Ли (с 8 до 17)  @Mamayavtelegrame" + "\r\n" +
        "Алеся Шахназарова (с 8 до 17) @lesya_shahnazarova" + "\r\n" +
        "Антон Петренко(с 8 до 17) @Petrosanton" + "\r\n" +
        "Инесса Имнадзе (с 9 до 18) @imnadze" + "\r\n" +
        "Владислав Ермолаев (c 12 до 21) @AsceticDream"+ "\r\n" +
        "Кристина Страшевская (c 12 до 21) @strashevskaya"+ "\r\n" +
        "Валерия Павлович (с 10 до 19) @valerka_p22" + "\r\n" +
        "Артур Сайфулин (с 10 до 19) @artsayf" + "\r\n" +
        "Валентин Копыцкий (с 12 до 21) @KopytskiValentin" + "\r\n" +
        "Александр Алексюк (с 14 до 23) @DannyDerden"

        )
    if message.text == "/среда":
        bot.send_message(message.chat.id, "Сегодня работают:" + '\r\n' +
                         "Женя Ли (с 8 до 17)  @Mamayavtelegrame" + "\r\n" +
                         "Алеся Шахназарова (с 8 до 17) @lesya_shahnazarova" + "\r\n" +
                         "Антон Петренко(с 8 до 17) @Petrosanton" + "\r\n" +
                         "Владислав Варенцов (c 8 до 17) @vverennayavamterritoriya" + "\r\n" +
                         "Инесса Имнадзе (с 9 до 18) @imnadze" + "\r\n" +
                         "Валерия Павлович (с 10 до 19) @valerka_p22" + "\r\n" +
                         "Артур Сайфулин (с 10 до 19) @artsayf" + "\r\n" +
                         "Алексей Стрелко (c 12 до 21) @alexstrel" + "\r\n" +
                         "Владислав Ермолаев (c 12 до 21) @AsceticDream" + "\r\n" +
                         "Кристина Страшевская (c 12 до 21) @strashevskaya" + "\r\n" +
                         "Валентин Копыцкий (с 12 до 21) @KopytskiValentin" + "\r\n" +
                         "Александр Алексюк (с 14 до 23) @DannyDerden")
    if message.text == "/четверг":
        bot.send_message(message.chat.id, "Сегодня работают:" + '\r\n' +
                         "Женя Ли (с 8 до 17)  @Mamayavtelegrame" + "\r\n" +
                         "Алеся Шахназарова (с 8 до 17) @lesya_shahnazarova" + "\r\n" +
                         "Антон Петренко(с 8 до 17) @Petrosanton" + "\r\n" +
                         "Владислав Варенцов (c 8 до 17) @vverennayavamterritoriya" + "\r\n" +
                         "Инесса Имнадзе (с 9 до 18) @imnadze" + "\r\n" +
                         "Валерия Павлович (с 10 до 19) @valerka_p22" + "\r\n" +
                         "Артур Сайфулин (с 10 до 19) @artsayf" + "\r\n" +
                         "Алексей Стрелко (c 12 до 21) @alexstrel" + "\r\n" +
                         "Владислав Ермолаев (c 12 до 21) @AsceticDream" + "\r\n" +
                         "Забелин Алексей(с 12 до 21) @Trikse4eg" + "\r\n" +
                         "Никита Парадис (с 12 до 21) @mukuta88" + "\r\n" +
                         "Кристина Страшевская (c 12 до 21) @strashevskaya" + "\r\n" +
                         "Валентин Копыцкий (с 12 до 21) @KopytskiValentin" + "\r\n" +
                         "Александр Алексюк (с 14 до 23) @DannyDerden")
    if message.text == "/пятница":
        bot.send_message(message.chat.id, "Сегодня работают:" + '\r\n' +
                         "Женя Ли (с 8 до 17)  @Mamayavtelegrame" + "\r\n" +
                         "Алеся Шахназарова (с 8 до 17) @lesya_shahnazarova" + "\r\n" +
                         "Антон Петренко(с 8 до 17) @Petrosanton" + "\r\n" +
                         "Владислав Варенцов (c 8 до 17) @vverennayavamterritoriya" + "\r\n" +
                         "Инесса Имнадзе (с 9 до 18) @imnadze" + "\r\n" +
                         "Алексей Стрелко (c 12 до 21) @alexstrel" + "\r\n" +
                         "Владислав Ермолаев (c 12 до 21) @AsceticDream" + "\r\n" +
                         "Кристина Страшевская (c 12 до 21) @strashevskaya" + "\r\n" +
                         "Забелин Алексей(с 12 до 21) @Trikse4eg" + "\r\n" +
                         "Никита Парадис (с 12 до 21) @mukuta88")
    if message.text == "/суббота":
        bot.send_message(message.chat.id, "Сегодня работают:" + '\r\n' +
                         "Антон Петренко(с 8 до 17) @Petrosanton" + "\r\n" +
                         "Владислав Варенцов (c 8 до 17) @vverennayavamterritoriya" + "\r\n" +
                         "Инесса Имнадзе (с 9 до 18) @imnadze" + "\r\n" +
                         "Алексей Стрелко (c 12 до 21) @alexstrel" + "\r\n" +
                         "Владислав Ермолаев (c 12 до 21) @AsceticDream" + "\r\n" +
                         "Забелин Алексей(с 12 до 21) @Trikse4eg" + "\r\n" +
                         "Никита Парадис (с 12 до 21) @mukuta88" + "\r\n" +
                         "Кристина Страшевская (c 12 до 21) @strashevskaya")
    if message.text == "/воскресенье":
        bot.send_message(message.chat.id, "Сегодня работают:" + '\r\n' +
                         "Владислав Варенцов (c 8 до 17) @vverennayavamterritoriya" + "\r\n" +
                         "Валерия Павлович (с 10 до 19) @valerka_p22" + "\r\n" +
                         "Артур Сайфулин (с 10 до 19) @artsayf" + "\r\n" +
                         "Алексей Стрелко (c 12 до 21) @alexstrel" + "\r\n" +
                         "Забелин Алексей(с 12 до 21) @Trikse4eg" + "\r\n" +
                         "Никита Парадис (с 12 до 21) @mukuta88" + "\r\n" +
                         "Валентин Копыцкий (с 12 до 21) @KopytskiValentin" + "\r\n" +
                         "Александр Алексюк (с 14 до 23) @DannyDerden")



if __name__ == '__main__':
    bot.polling(none_stop=True)