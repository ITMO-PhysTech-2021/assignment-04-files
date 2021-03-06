# Задание #04. Файлы

## Правила

Задачи разбиваются на две категории:

- [`practice`](practice) &ndash; задания практики, частично разбираются на практике
- [`homework`](homework) &ndash; задания ДЗ для самостоятельного решения

Дедлайны и прочая инфа как обычно будут в Telegram канале.

Убедительная просьба писать код **самостоятельно**! Вы можете решать сложные задания вместе и обсуждать решения друг с
другом, но навык реализации своих идей в коде особо не разовьется от простого переписывания чужого кода.

Не редактируйте файлы в папке `.github`, а также файлы, заканчивающиеся на `_test.py`, если у вас есть желание получить
ненулевые баллы :)

## Первоначальная настройка

Если у вас все еще есть проблемы с гитом, питоном или пайтестом, обратитесь к файлу [SETUP.md](SETUP.md).

## Репозиторий

Склонируйте этот репозиторий, если у него имя `assignment-04-files-ваш-никнейм`.

Если у этого репозитория имя `assignment-04-files`, вместо этого

- не клонируйте этот репозиторий (ну пожалуйста)
- не форкайте этот репозиторий
- вообще не трогайте этот репозиторий

### Upstream

Репозиторий `assignment-04-files` &ndash; это общий репозиторий, в котором у всех есть права на чтение и нет прав на
запись. Это означает, что с ним вы можете делать `git pull` (загрузить себе новые изменения), но не можете
делать `git push` (отправить свои изменения на GitHub).

В этот раз вы будете активно пользоваться опцией `git pull`, если нам понадобится внести некоторые изменения во ВСЕ ваши
репозитории (например, залить домашку). Для этого надо настроить доступ к общему репозиторию на чтение. В папке проекта
выполните следующую команду:

```shell
git remote add upstream git@github.com:ITMO-PhysTech-2021/assignment-04-files.git
```

Теперь у вас есть два удаленных репозитория, с которыми вы можете работать:

- `origin` &ndash; ваш репозиторий, в который вы будете заружать свои решения
- `upstream` &ndash; общий репозиторий, из которого можно выгружать изменения, предназначенные для всех

Чтобы синхронизировать историю коммитов, сразу после этого выполните

```shell
git pull upstream
git reset --hard upstream/master
git push --force origin master
```

## Процесс выполнения заданий

Все условия находятся в файлах `_legend.md` в соответствующих папках `practice/TASKNAME` или `homework/TASKNAME`.

**Важно:** перед тестированием любого задания подгрузите изменения из общего репозитория:

```shell
git pull upstream master
```

### Практика

**Перейдите на ветку `practice`!**. Иначе ваши решения не будут автоматически тестироваться, и у вас есть шанс не
получить баллы.

```shell
git checkout -b practice
```

Протестировать задание можно запустив файл с тестами из PyCharm или запустив одну из следующих команд в терминале:

```shell
pytest practice/TASKNAME
python -m pytest practice/TASKNAME
```

Сделав какое-то задание, выполните команды, чтобы добавить изменения в Git, собрать их в один коммит и отправить на
GitHub:

```shell
git add practice/TASKNAME
git commit -m "practice TASKNAME finished"
git push origin practice
```

#### Pull Request

После того, как все задания практики сделаны, создайте Pull Request из ветки `practice` в ветку `master` и укажите своего
преподавателя в качестве Reviewer. **Не надо делать Merge** до того, как ваш код будет проверен преподавателем.

Pull Request можно сделать по ссылке, которая появляется, если вы делаете `git push origin practice`, либо в меню Pull
Requests на GitHub.