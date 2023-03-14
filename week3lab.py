from week3 import list_dot


f = open('voting_record_dump109.txt')
mylist = list(f)


# Task 2.12.1: Write a procedure create voting dict(strlist) that, given a list of
# strings (voting records from the source file), returns a dictionary that maps the last name
# of a senator to a list of numbers representing that senator’s voting record. You will need to
# use the built-in procedure int(·) to convert a string representation of an integer (e.g. ‘1’)
# to the actual integer (e.g. 1).
def senator_votes(strlist):
    senator_dict = {}
    for x in strlist:
        print(x.split())
        senator_dict[x.split()[0]] = [int(y) for y in x.split()[3:]]
    return senator_dict

# Task 2.12.2: Write a procedure policy compare(sen a, sen b, voting dict) that,
# given two names of senators and a dictionary mapping senator names to lists representing
# voting records, returns the dot-product representing the degree of similarity between two
# senators’ voting policies.
def compare(sen_a, sen_b, voting_dict):
    return list_dot(voting_dict[sen_a], voting_dict[sen_b])


print(senator_votes(mylist))
print(compare('Bond', 'Bayh', senator_votes(mylist)))
