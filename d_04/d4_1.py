from copy import deepcopy

test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def read_input():
    with open("input.txt", "r") as f:
        return f.read()


def parse_input(input):
    numbers = input.split("\n")[0]
    tickets = input.split()[1:]
    t = []
    for j in range(0, len(tickets), 25):
        ticket = []
        for i in range(j, j + 25, 5):
            ticket.append(tickets[i : i + 5])
        t.append(ticket)
    return numbers.split(","), t


def generate_tickets(tickets):
    generate_tickets = {}
    for i, rows in enumerate(tickets):
        columns = [[] for x in range(5)]
        for r in rows:
            for j in range(5):
                columns[j].append((r[j], False))
        generate_tickets[i] = {
            "rows": [[(r, False) for r in ro] for ro in rows],
            "columns": columns,
        }
    return generate_tickets


def check_number(number, tickets):
    for k, ticket in tickets.items():
        for row in ticket["rows"]:
            for i, n in enumerate(row):
                if n[0] == number:
                    row[i] = (n[0], True)
        for column in ticket["columns"]:
            for i, n in enumerate(column):
                if n[0] == number:
                    column[i] = (n[0], True)


def check_winner(tickets):
    winners = []
    for ticket_id, ticket in tickets.items():
        for row in ticket["rows"] + ticket["columns"]:
            if all([n[1] for n in row]):
                winners.append(ticket_id)
    return winners


def find_winner(numbers, tickets):
    all_winners = []
    last_winning_ticket_state = None
    last_number = None
    for n in numbers:
        check_number(n, tickets)
        current_winners = check_winner(tickets)
        for ticket_id in current_winners:
            if ticket_id not in all_winners:
                all_winners.append(ticket_id)
                last_number = n
                last_winning_ticket_state = deepcopy(tickets[ticket_id])
    return last_number, last_winning_ticket_state


def filter_unchecked(rows):
    all_numbers = []
    for row in rows:
        all_numbers += row
    return filter(lambda x: x[1] is False, all_numbers)


def bingo():
    numbers, rows = parse_input(read_input())
    # numbers, rows = parse_input(test)
    tickets = generate_tickets(rows)
    number, winning_ticket = find_winner(numbers, tickets)
    unchecked_numbers = [int(n[0]) for n in filter_unchecked(winning_ticket["rows"])]
    print(sum(unchecked_numbers) * int(number))


bingo()
