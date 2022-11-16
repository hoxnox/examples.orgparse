import orgparse, os

home = os.getenv('HOME')
notebooks = ["inbox", "home", "work", "payments", "reminders"]

def is_today(date):
    if orgparse.date.OrgDate((2022,11,16,0,0,0), (2022,11,16,23,59,59)).has_overlap(date):
        return True
    return False

def by_scheduled(node):
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
