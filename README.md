# websocketreplacer
Берп и овасп зап не позволяют матчить и подменять параметры в вебсокет запросах.
С помощью mitmproxy мы можем это исправить

#Команда для старта
mitmdump -s mitmproxywebsockets.py -p 8070 -k --mode upstream:https://localhost:8080
-p 8070 - прокси на порту 8070
-k insecure подключение к апстрим прокси
--mode подключение к апстрим прокси на порту 8080 - например burp suite
