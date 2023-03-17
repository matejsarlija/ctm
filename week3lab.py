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
        #print(x.split())
        senator_dict[x.split()[0]] = [int(y) for y in x.split()[3:]]
    return senator_dict



# Task 2.12.2: Write a procedure policy compare(sen a, sen b, voting dict) that,
# given two names of senators and a dictionary mapping senator names to lists representing
# voting records, returns the dot-product representing the degree of similarity between two
# senators’ voting policies.
def compare(sen_a, sen_b, voting_dict):
    return list_dot(voting_dict[sen_a], voting_dict[sen_b])



# Task 2.12.3: Write a procedure most similar(sen, voting dict) that, given the name
# of a senator and a dictionary mapping senator names to lists representing voting records,
# returns the name of the senator whose political mindset is most like the input senator
# (excluding, of course, the input senator him/herself).
def most_similar(sen, voting_dict):
    out_dict = {}
    for x in voting_dict.keys():
        if sen != x:
            dot_dot = list_dot(voting_dict[sen], voting_dict[x])
            out_dict[dot_dot] = x
    return out_dict[max(out_dict)]

# Task 2.12.4: Write a very similar procedure least similar(sen, voting dict) that
# returns the name of the senator whose voting record agrees the least with the senator whose
# name is sen.
def least_similar(sen, voting_dict):
    out_dict = {}
    for x in voting_dict.keys():
        if sen != x:
            dot_dot = list_dot(voting_dict[sen], voting_dict[x])
            out_dict[dot_dot] = x
    return out_dict[min(out_dict)]


# A list of all the senator from the file
senators = senator_votes(mylist)

"""
Let's also fish out a set of democrats
"""
democrats = [x.split()[0] for x in mylist if x.split()[1] == 'D']

# Task 2.12.7: Write a procedure find average similarity(sen, sen set, voting dict)
# that, given the name sen of a senator, compares that senator’s voting record to the voting
# records of all senators whose names are in sen set, computing a dot-product for each, and
# then returns the average dot-product.
# Use your procedure to compute which senator has the greatest average similarity with
# the set of Democrats (you can extract this set from the input file).
def find_average_similarity(sen, sen_set, voting_dict):
    out_list = []

    for x in sen_set:
        if x != sen:
            dot_dot = list_dot(voting_dict[sen], voting_dict[x])
            out_list.append(dot_dot)
    return sum(out_list)/len(out_list)


"""
Add two vectors
"""
def addn(u, v):
    return [u[i]+v[i] for i in range(len(u))]

"""
Task 2.12.8: Write a procedure find average record(sen set, voting dict) that,
given a set of names of senators, finds the average voting record. That is, perform vector
addition on the lists representing their voting records, and then divide the sum by the number
of vectors. The result should be a vector.
Use this procedure to compute the average voting record for the set of Democrats, and
assign the result to the variable average Democrat record. Next find which senator’s
voting record is most similar to the average Democrat voting record. Did you get the same
result as in Task 2.12.7? Can you explain?
"""
def find_average_record(sen_set, voting_dict):
    voting_dict_democrat_values = [voting_dict[x] for x in sen_set]
    result_vec = [0] * len(voting_dict[sen_set[0]])
    #print([x for x in voting_dict_democrat_values])

    # ok ovo sada radi
    for x in voting_dict_democrat_values:
        result_vec = addn(result_vec, x)

    result_vec_avg = [x/len(voting_dict_democrat_values) for x in result_vec]

    return result_vec_avg

average_democrat_record = find_average_record(democrats, senators)


senators_avg_dem = {}

for x,y in senators.items():
    print(x)
    dot_dot = list_dot(y, average_democrat_record)
    senators_avg_dem[dot_dot] = x

# Biden again
print(max(senators_avg_dem), senators_avg_dem[max(senators_avg_dem)])

#print(addn(senators['Bayh'], senators['Biden']))

#print(senator_votes(mylist).keys())
#print(compare('Bond', 'Bayh', senator_votes(mylist)))
#print(most_similar('Bond', senators ))
#print(least_similar('Bond', senators ))
#print(democrats)

"""
similar_to_democrats = {}
for x in senators.keys():
    sim = find_average_similarity(x, democrats, senators)
    print(sim)
    similar_to_democrats[sim] = x


for x in similar_to_democrats.items():
    print(x)
"""

# omg it's Biden
#print("The senator most similar to democrats is ", similar_to_democrats[max(similar_to_democrats)], " With a score of", max(similar_to_democrats) )
#print("Bayh sim is ", find_average_similarity('Bayh', democrats, senators))
