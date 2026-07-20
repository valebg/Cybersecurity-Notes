# 🛡️ Blue Team Labs Online - Secure Shell (Writeup)

**Ссылка на достижение:** [BTLO Achievement](https://blueteamlabs.online/achievement/share/challenge/164988/17)

## 📝 Описание сценария
В системе с запущенной службой SSH было замечено аномальное увеличение размера лог-файла. Цель расследования (Incident Response) — проанализировать артефакты лога `sshlog.log`, определить вектор атаки, скомпрометированные учетные записи и таймштампы активности.

---

## 🔍 Ход расследования и использованные команды

### 1. Первичный анализ структуры лога
```bash
head -n 20 sshlog.log

Вывод команды указал на инициализацию процесса C:\OpenSSH-Win64\sshd.exe и наличие отладочных сообщений уровня debug3, что позволило определить ОС (Windows) и уровень логирования.

2. Определение источника и типа атакиBashgrep -i "connection from" sshlog.log | head -n 20

Был зафиксирован IP-адрес 192.168.1.17, принадлежащий к диапазону частных подсетей, что указывает на внутренний вектор атаки.

3. Поиск скомпрометированных учетных записейBashgrep "Accepted" sshlog.log | grep "192.168.1.17"

Команда вернула две строки с успешным входом для учетной записи sophia.

4. Определение временных рамок инцидентаBashgrep "192.168.1.17" sshlog.log | head -n 5

## 🎯 Ответы на вопросы лабораторной работы

| # | Вопрос | Ответ |
| :--- | :--- | :--- |
| **1** | Is it an internal or external attack, what is the attacker IP? | `internal, 192.168.1.17` |
| **2** | How many valid accounts did the attacker find, and what are the usernames? | `1, sophia` |
| **3** | How many times did the attacker login to these accounts? | `2` |
| **4** | When was the first request from the attacker recorded? | `2021-04-29 23:41:56` |
| **5** | What is the log level for the log file? | `DEBUG3` |
| **6** | Where is the log file located in Windows? | `C:\ProgramData\ssh\logs\sshd.log` |

---

## 🛠️ Заключение и выводы (Lessons Learned)
* **Избыточное логирование:** Уровень `DEBUG3` производит слишком много информации. Рекомендуется перевести `LogLevel` в режим `INFO`.
* **Контроль учетных записей:** Учетная запись `sophia` была скомпрометирована брутфорсом. Необходимо внедрить политику сложных паролей.