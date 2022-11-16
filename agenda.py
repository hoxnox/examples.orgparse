import orgparse, os, datetime

home = os.getenv('HOME')
notebooks = ["inbox", "home", "work", "payments", "reminders"]

def is_today(date) -> bool:
    if not date:
        return False
    if not date.is_active:
        return False
    return orgparse.date.OrgDate(datetime.datetime(1970, 1, 1), datetime.datetime.now().replace(hour=23,minute=59,second=59)).has_overlap(date)

def by_scheduled(node) -> datetime.datetime:
    return node.scheduled.start

agenda = []
for notebook in notebooks:
    root = orgparse.load("%s/todo/%s.org" % (home, notebook))
    for i in root[1:]:
        if is_today(i.scheduled) and not i.closed:
            agenda.append(i)

agenda.sort(key=by_scheduled)
for i in agenda:
    print(i)
