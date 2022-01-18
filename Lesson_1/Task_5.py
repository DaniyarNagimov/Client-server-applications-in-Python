import subprocess

"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтового в строковый
(предварительно определив кодировку выводимых сообщений).
"""

urls = ['yandex.ru', 'youtube.com']

for url in urls:
    args = ['ping', url]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
