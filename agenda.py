import orgparse, os, datetime

home = os.getenv('HOME')
notebooks = ["inbox", "home", "work", "payments", "reminders"]

def is_today(date) -> bool:
    if not date or not date.start:
        return False
    return orgparse.date.is_same_day(datetime.datetime.now(), date.start)

def by_scheduled(node) -> datetime.datetime:
    return node.scheduled.start

agenda = []
for notebook in notebooks:
    root = orgparse.load("%s/todo/%s.org" % (home, notebook))
    for i in root[1:]:
        if is_today(i.scheduled):
            agenda.append(i)

agenda.sort(key=by_scheduled)
for i in agenda:
    print(i)
