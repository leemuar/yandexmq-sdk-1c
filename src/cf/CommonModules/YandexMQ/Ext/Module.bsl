
Функция DeleteMessage( Знач QueueUrl, Знач ReceiptHandle ) Экспорт

	
КонецФункции

Функция RecieveMessage( Знач Endpoint, Знач Version, Знач login, Знач secret, Знач QueueUrl ) Экспорт
	
	ПараметрыЗапроса = Новый Структура;
	Ответ = КоннекторHTTP.Post( 
		Endpoint, 
	);
	
КонецФункции
