people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: "{} {}".format(x.split()[0], x.split()[-1]))(person))

#option 2
print(list(map(split_title_and_name, people)) == list(map(lambda x: "{} {}".format(x.split()[0], x.split()[-1]), people)))
