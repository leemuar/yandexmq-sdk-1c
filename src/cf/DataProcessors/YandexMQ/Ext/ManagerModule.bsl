
Функция НовыйКлиентYandexMQ( Знач AccessKey, Знач SecretKey ) Экспорт
	
	УстановитьПривилегированныйРежим( Истина );
	
	Объект = Обработки.YandexMQ.Создать();
	Объект._Endpoint  = "https://message-queue.api.cloud.yandex.net/";
	Объект._Version   = "2012-11-05";
	Объект._Region    = "ru-central1";
	Объект._AccessKey = AccessKey;
	Объект._SecretKey = SecretKey;

	Возврат Объект;
	
КонецФункции


Функция НовыйКлиентAmazonSQS( Знач AccessKey, Знач SecretKey, Знач Region = "us-east-1", Знач Version = "2012-11-05" ) Экспорт
	
	УстановитьПривилегированныйРежим( Истина );
	
	Объект = Обработки.YandexMQ.Создать();
	Объект._Endpoint  = "https://sqs." + Region + ".amazonaws.com";
	Объект._Version   = "2012-11-05";
	Объект._Region    = Region;
	Объект._AccessKey = AccessKey;
	Объект._SecretKey = SecretKey;

	Возврат Объект;
	
КонецФункции
