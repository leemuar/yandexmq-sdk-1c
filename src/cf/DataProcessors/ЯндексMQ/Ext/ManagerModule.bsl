
Функция НовыйКлиент( Знач AccessKey, Знач SecretKey ) Экспорт
	
	УстановитьПривилегированныйРежим( Истина );
	
	Объект = Обработки.ЯндексMQ.Создать();
	Объект._Endpoint  = "https://message-queue.api.cloud.yandex.net/";
	Объект._Version   = "2012-11-05";
	Объект._Region    = "ru-central1";
	Объект._AccessKey = AccessKey;
	Объект._SecretKey = SecretKey;

	Возврат Объект;
	
КонецФункции

