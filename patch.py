with open("src/cf/DataProcessors/ЯндексMQ2/Ext/ObjectModule.bsl", "r", encoding="utf-8-sig", newline='') as f:
    content = f.read()

# Replace Russian wrappers
content = content.replace("Возврат RecieveMessage( ПараметрыЗапроса )", "Возврат ReceiveMessage( ПараметрыЗапроса )")
content = content.replace("Возврат RecieveMessageResponse( ПараметрыЗапроса )", "Возврат ReceiveMessageResponse( ПараметрыЗапроса )")

# Also replace references in comments
content = content.replace("Вызывает метод RecieveMessage", "Вызывает метод ReceiveMessage")


s1 = "Функция RecieveMessage( Знач QueryParams ) Экспорт\r\n\t\r\n\tОтвет = RecieveMessageResponse( QueryParams );\r\n\tЕсли 200 <> Ответ.КодСостояния Тогда\r\n\t\tВозврат Неопределено;\r\n\tКонецЕсли;\r\n\t\r\n\tДанныеОтвета = КакJson( Ответ, Новый Структура( \"ПрочитатьВСоответствие\", Ложь ) );\r\n\t\r\n\tЕсли НЕ ДанныеОтвета.Свойство( \"Messages\" ) Тогда\r\n\t\tВозврат Новый Массив;\r\n\tКонецЕсли;\r\n\t\r\n\tВозврат ДанныеОтвета[ \"Messages\" ];\r\n\t\r\nКонецФункции"

r1 = "Функция ReceiveMessage( Знач QueryParams ) Экспорт\r\n\t\r\n\tОтвет = ReceiveMessageResponse( QueryParams );\r\n\tЕсли 200 <> Ответ.КодСостояния Тогда\r\n\t\tВозврат Неопределено;\r\n\tКонецЕсли;\r\n\t\r\n\tДанныеОтвета = КакJson( Ответ, Новый Структура( \"ПрочитатьВСоответствие\", Ложь ) );\r\n\t\r\n\tЕсли НЕ ДанныеОтвета.Свойство( \"Messages\" ) Тогда\r\n\t\tВозврат Новый Массив;\r\n\tКонецЕсли;\r\n\t\r\n\tВозврат ДанныеОтвета[ \"Messages\" ];\r\n\t\r\nКонецФункции\r\n\r\n\r\n\r\n// DEPRECATED\r\n//\r\n// Получает одно или несколько сообщений из указанной очереди\r\n//\r\n// Вызывает метод ReceiveMessage сервиса\r\n//\r\n// Параметры:\r\n//  QueryParams - Структура:\r\n//\t\t* QueueUrl\t-\tСтрока\t-\t(обязательный) URL очереди\r\n//\t\t* MaxNumberOfMessages\t-\tЧисло\t-\t(опционально) Максимальное количество сообщений, которое будет принято\r\n//\t\t* AttributeNames\t-\tМассив из Строка\t-\t(опционально) Массив имен атрибутов сообщения, которые требуется вернуть в ответе на запрос\r\n//\t\t* ReceiveRequestAttemptId\t-\tСтрока\t-\t(опционально) дентификатор для повтора попытки получения сообщений из FIFO-очереди\r\n//\t\t* VisibilityTimeout\t-\tЧисло\t-\t(опционально) Таймаут видимости получаемого сообщения\r\n//\t\t* WaitTimeSeconds\t-\tЧисло\t-\t(обязательный) Время ожидания доставки сообщения в очередь в секундах\r\n// \r\n// Возвращаемое значение:\r\n//  Неопределено - если не удалось получить сообщения\r\n//  Массив - Массив из Структур с данными полученных сообщений\r\n//\r\nФункция RecieveMessage( Знач QueryParams ) Экспорт\r\n\t\r\n\tВозврат ReceiveMessage( QueryParams );\r\n\t\r\nКонецФункции"

s2 = "Функция RecieveMessageResponse( Знач QueryParams ) Экспорт\r\n\t\r\n\tВозврат ВыполнитьЗапросAwsJson( \"ReceiveMessage\", QueryParams );\r\n\t\r\nКонецФункции"

r2 = "Функция ReceiveMessageResponse( Знач QueryParams ) Экспорт\r\n\t\r\n\tВозврат ВыполнитьЗапросAwsJson( \"ReceiveMessage\", QueryParams );\r\n\t\r\nКонецФункции\r\n\r\n\r\n\r\n// DEPRECATED\r\n//\r\n// Получает одно или несколько сообщений из указанной очереди\r\n//\r\n// Вызывает метод ReceiveMessage сервиса\r\n//\r\n// Параметры:\r\n//  QueryParams - Структура:\r\n//\t\t* QueueUrl\t-\tСтрока\t-\t(обязательный) URL очереди\r\n//\t\t* MaxNumberOfMessages\t-\tЧисло\t-\t(опционально) Максимальное количество сообщений, которое будет принято\r\n//\t\t* AttributeNames\t-\tМассив из Строка\t-\t(опционально) Массив имен атрибутов сообщения, которые требуется вернуть в ответе на запрос\r\n//\t\t* ReceiveRequestAttemptId\t-\tСтрока\t-\t(опционально) дентификатор для повтора попытки получения сообщений из FIFO-очереди\r\n//\t\t* VisibilityTimeout\t-\tЧисло\t-\t(опционально) Таймаут видимости получаемого сообщения\r\n//\t\t* WaitTimeSeconds\t-\tЧисло\t-\t(обязательный) Время ожидания доставки сообщения в очередь в секундах\r\n//  \r\n// Возвращаемое значение:\r\n//  См. ВызватьМетод\r\n//\r\nФункция RecieveMessageResponse( Знач QueryParams ) Экспорт\r\n\t\r\n\tВозврат ReceiveMessageResponse( QueryParams );\r\n\t\r\nКонецФункции"

if s1 in content and s2 in content:
    content = content.replace(s1, r1)
    content = content.replace(s2, r2)
    print("Replaced successfully")
else:
    print("Did not find substrings!")

with open("src/cf/DataProcessors/ЯндексMQ2/Ext/ObjectModule.bsl", "w", encoding="utf-8-sig", newline='') as f:
    f.write(content)
