from os import system, name
import time


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def animate(str, int):
    while int > 0:
        str = " " + str
        print(str)
        int = int - 1
        if int > 0:
            time.sleep(0.005)
        else:
            clear()


animate(">", 1000)
import sqlite3
import random
import qiskit
import re
import sys, random
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

points = 0
bhp = 4000
uhp = 2000


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
    print(" ")
    print(" ")


print_slow("President of Hacktopia: Hello, welcome to Hacktopia.")
print(" ")
print_slow("President of Hacktopia: What is your name?")
user = str(input(">: "))
print("   ")
u = user + ": "


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
    print(" ")
    print(" ")


def print_slowln(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)


def get_question_from_db(question_id):
    conn = sqlite3.connect('hacktopia.db')
    cursor = conn.execute("SELECT * from Questions Where QuestionId=" +
                          str(question_id))

    result = {}
    for row in cursor:
        result["question"] = row[1]
        result["correct_answer"] = row[2]
        l = [row[2], row[3], row[4], row[5]]
        random.shuffle(l)
        result["answers"] = l
        result["points"] = row[6]

    conn.close()
    return result


def ask_question(question_id):
    global points

    clear()
    print("-----------------------------------------------")
    print_slow("POP QUIZ TIME!!!!!!!")
    question = get_question_from_db(question_id)
    key = ["a", "b", "c", "d"]
    correct_key = "z"
    print(question["question"])

    for a in zip(key, question["answers"]):
        print_slow(a[0] + " : " + a[1])
        if a[1] == question["correct_answer"]:
            correct_key = a[0]
    print_slow("Please type 'a', 'b', 'c', or 'd' to answer the question.")

    for i in range(2):
        ans1 = input(u)
        if ans1 == correct_key:
            print_slow("You are correct!")
            points = points + question["points"]
            print_slowln("You got " + str(points) + " points!")
            print("    ")
            break
        else:
            if i == 0:
                print_slow("You are wrong, try again.")
            else:
                print_slow("You are wrong. The correct answer is: 'c'")
                points = points - 1
                print_slow("You have")
                print(points)
                print("points!")
            print(" ", end='')


p = "President of Hacktopia:"
print_slowln("President of Hacktopia: Hello ")
print_slow(user)
print_slow(
    "You are the person I am looking for. A mad scientist is planning to collapse our nation's cyber security."
)
print_slowln("President of Hacktopia: And we need you,")
print_slowln(user)
print_slow(" to help us.")
print_slow(
    "President of Hacktopia: Do you accept? Please type 'y' for yes and 'n' for no."
)
u = user + ": "
yorn = str(input(u))
print(" ")
if yorn == "y":
    print_slow("President of Hacktopia: Let's get started!")
else:
    print_slow("President of Hacktopia: Ok, then")
    print_slow("Time to clear your memory!")
    time.sleep(3)
    clear()
    exit()
    quit()
print_slow(
    "President of Hacktopia: The mad scientist is planning to use a quantum computer to hack Hacktopia's cybersecurity system"
)
print_slow(
    "President of Hacktopia: Quantum Computers are computing devices that use qubits (quantum bits - which are the basic units of quantum computers) to compute certain specialized complex equations and algorthims way faster than classical computers"
)
print_slow("President of Hacktopia: but they are still fairly new to us.")
print_slow(
    "President of Hacktopia: Qubits, by the way, are the basic unit of information for quantum computation"
)
print_slowln(p), print_slow(
    "And when logic gates or operations are applied to the gates that interact, perform calculations, and get entangled"
)
print_slow(
    "President of Hacktopia: For example, a Hadamard gate and a CNOT gate, in sequence, can produce entanglement."
)
print_slow(
    "President of Hacktopia: The Hadamard gate is a gate that is used to form a random input."
)
print_slow(
    "President of Hacktopia: The CNOT gate is used to entangle qubits after entangling them."
)
print_slow(
    "Please type anything when you feel confident of the information provided above"
)
anything = input(u)
print(" ")
if anything == "dsfjkadsl":
    clear()
else:
    clear()

ask_question(2)

ask_question(3)

ask_question(4)

anything1 = input("Please type anything to clear the screen or press 'enter'.")
if anything1 == "dsfas":
    clear()
else:
    clear()
print_slow(
    "President of Hacktopia: One of the ways to make qubits entangle is where you apply a Hadamard gate to all of the qubits and apply CNOT gates that entangle the qubits"
)
print_slow(
    "President of Hacktopia: When qubits entangle, you can simulate randomness with equal probability outcomes or 'probabilities'. And based on the number of qubits you entangle, you simulate probabilties with different values. You can use the equation p = 2^q where p is the number of probabilites you want to simulate and q is the number of qubits in the quantum system. And by the way, the number of probabilites or qubits must be an integer!"
)
print_slow(
    "If you want to find the number of qubits you have to have in a quantum system with a probability that cannot be expressed as p = 2^q, you can find the next possible probability, and remove some probabilites."
)
print_slow(
    "Please type anything or press 'enter' to clear the screen and move on to the next info and course."
)
anything3 = input(u)
print(" ")
if anything3 == "dsfjkadsl":
    clear()
else:
    clear()

ask_question(5)

ask_question(6)

ask_question(7)

print_slow(
    "Please type anything or press 'enter' to clear the screen and move on to the next info and course."
)
anything4 = input(u)
print(" ")
if anything4 == "dsfjkadsl":
    clear()
else:
    clear()
print_slow(
    "President of Hacktopia: There are two famous algorithms in quantum computation. One is Shor's Algorithm and the other is Grover's Algorithm"
)
print_slow(
    "President of Hacktopia: Shor's Algorithm is an algorthim that factors a prime number efficently. Classical computers do not have an algorithm nearly as efficient as Shor's Algorithm which offers an exponential speedup compared to the best known classical counterpart. Shor's Algorithm can be used to decrypt much of the cryptography used today like RSA which are employed to secure things we use every day like credit card numbers."
)
print_slow(
    "President of Hacktopia: Grover's Algorithm is a search algorithim that makes search engines faster. It states that if you have N values, you have to search through an average square root of N values. And, for a classical computer, you have to search through N/2 values.  This is what is known as a quadratic speedup."
)
print_slow(
    "Please type anything or press 'enter' to clear the screen and move on to the next info and course."
)
anything5 = input(u)
print(" ")
if anything5 == "dsfjkadsl":
    clear()
else:
    clear()
ask_question(8)

print("   ")

ask_question(9)

ask_question(10)

ask_question(11)

anything6 = input(u)
print(" ")
if anything6 == "dsfjkadsl":
    clear()
else:
    clear()
print("-----------------------------------------------")
print_slow(
    "President of Hacktopia: Now, it is time to use your knowledge to code with Hadamard and CNOT gates. You can code anything you want! Be creative!"
)
yorn12 = "y"
while yorn12 == "y":
    print_slow(
        "President of Hacktopia: Please type the amount of qubits you want in your quantum system. Your answer should be a integer from 2-10"
    )
    q = str(input(u))
    num_format = re.compile(r'^\-?[1-9][0-9]*$')
    it_is = re.match(num_format, q)
    if it_is:
        q = float(q)
        itis = "true"
    else:
        itis = "false"
    while itis == "false":
        print("The input you typed is not a number")
        print_slow(
            "President of Hacktopia: Please type the amount of qubits you want in your quantum system. Your answer should be a integer from 2-10, if you pick number less than 2 it'll become 2, if you pick number more than 10 it'll become 10."
        )
        q = str(input(u))
        num_format = re.compile(r'^\-?[1-9][0-9]*$')
        it_is = re.match(num_format, q)
        if it_is:
            q = float(q)
            itis = "true"
        else:
            itis = "false"
    if q % 1 == 0:
        q = int(q)
    else:
        q = round(q)
        q = int(q)
    if q > 10:
        q = 10
    if q < 2:
        q = 2
    maxq = q - 1
    minq = 0
    simulator = QasmSimulator()
    circuit = QuantumCircuit(q, q)
    more = "y"
    while more == "y":
        print_slow(
            "What type of gate do you want to add? Type 'cnot' to add a CNOT gate or 'h' to add a Hadamard gate"
        )
        gate = input(u)
        if gate == "h":
            print_slow(
                "What qubit do you want to add your Hadamard gate to? Remember that the first qubit is qubit 0. Please put the qubit's number. For example, if you want to add a Hadamard gate to qubit 0, type 0. Please type a number from 0 - 9."
            )
            qubit = str(input(u))
            if qubit == "9":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "8":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "7":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "6":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "5":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "4":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "3":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "2":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "1":
                qubit = int(qubit)
                itis1 = "true"
            elif qubit == "0":
                qubit = int(qubit)
                itis1 = "true"
            else:
                print_slow("The input you typed in is not valid")
                print_slow("Please type in a integer between 0 and 9.")
                itis1 = "false"
                qubit = str(input(u))
                while itis1 == "false":
                    if qubit == "9":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "8":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "7":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "6":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "5":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "4":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "3":
                        itis1 = "true"
                        qubit = int(qubit)
                    elif qubit == "2":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "1":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "0":
                        qubit = int(qubit)
                        itis1 = "true"
                    else:
                        itis1 = "false"
                        print_slow("The input you typed in is not valid")
                        print_slow("Please type in a integer between 0 and 9.")
                        qubit = str(input(u))
            circuit.h(qubit)
        elif gate == "cnot":
            print_slow(
                "What is the first qubit that you will entangle as the control qubit of the CNOT gate? Remember that the very first qubit in the register is qubit 0. Please put the qubit's number. Also, this qubit should have the least qubit number of the two. For example, if you are entangling qubit 0 and 1, type 0. Please type a number from 0-9.")
            qubit = str(input(u))
            if qubit == "9":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "8":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "7":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "6":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "5":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "4":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "3":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "2":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "1":
                qubit = int(qubit)
                itis1 = "true"
            if qubit == "0":
                qubit = int(qubit)
                itis1 = "true"
            else:
                print_slow("The input you typed in is not valid")
                print_slow("Please type in a integer between 0 and 9.")
                itis1 = "false"
                qubit = str(input(u))
                while itis1 == "false":
                    if qubit == "9":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "8":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "7":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "6":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "5":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "4":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "3":
                        itis1 = "true"
                        qubit = int(qubit)
                    elif qubit == "2":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "1":
                        qubit = int(qubit)
                        itis1 = "true"
                    elif qubit == "0":
                        qubit = int(qubit)
                        itis1 = "true"
                    else:
                        itis1 = "false"
                        print_slow("The input you typed in is not valid")
                        print_slow("Please type in a intger between 0 and 9.")
                        qubit = str(input(u))
            print_slow(
                "What is the second qubit that you will entangle as the target qubit of the CNOT gate? Remember that the very first qubit is qubit 0. Please put the qubit's number. Also, this qubit should have the most qubit number of the two. For example, if you are entangling qubit 0 and 1, type 1 Please type a number from 0-9."
            )
            qubit1 = int(input(u))
            circuit.cx(qubit,qubit1)          
        print_slow("Do you want to add more gates to your quantum circuit? Type 'y' for yes and anything else for no.")
        more = input(u)
        if more == "y":
            yorn = 1
        else:
            asfdsa = 1
    circuit.measure_all()
    compiled_circuit = transpile(circuit, simulator)
    print_slow(
        "How many times do you want to simulate the circuit? Tip: The more tries or 'shots' you run, the more you accurate your results are. Please type a postive integer from 1 - 10000"
    )
    ashots = int(input(u))
    job = simulator.run(compiled_circuit, shots=ashots)
    result = job.result()
    counts = result.get_counts(compiled_circuit)
    print_slow("Your counts are...")
    print(counts)
    print_slow("Congrats! You have created a quantum circuit!")
    print_slow(
        "Do you want to create a quantum circuit again? Please type 'y' for yes and anything else for no."
    )
    yorn12 = input(u)
print_slow("Clearing...")
time.sleep(2)
clear()
animate(">", 1000)
print_slow(
    "Mad Scientist: How dare you try to stop me! I will hack Hacktopia this instant because of you!"
)
print_slow(
    "Mad Scientist: Hmmm, what is the least amount of qubits I need for entanglement?"
)
print_slow("Hacking...")
print_slow(
    "President of Hacktopia: Hack into his code and stop him from entangling his qubits!"
)
print_slow("What do you do!?")
print_slow("a:Cry and leave")
print_slow("b:Say your problem not mine and leave.")
print_slow("c:Add a qubit")
print_slow("d:Delete a qubit")
bd = input("")
if bd == "d":
    print_slow("Mad Scientist: Stop this right now!!!")
    bhp = bhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")
else:
    print_slow("Mad Scientist: Yes")
    uhp = uhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")
#dhanvin, comment questions here...
print_slow(
    "Mad Scientist: Hmmm, what is the amount of probabilities I can calculate with 5 qubits!"
)
print_slow("Hacking...")
print_slow(
    "President of Hacktopia: Hack into his code and stop him from calculating probabilities!"
)
print_slow("What do you do!?")
print_slow("a:Cry louder")
print_slow("b:Do nothing, what can a Mad Scientist do?")
print_slow("c:Add more probabilities.")
print_slow("d:Delete some probabilities.")
bc = input("")
if bc == "c":
    print_slow("Mad Scientist: Stop this you madman!!!")
    bhp = bhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")
else:
    print_slow("Mad Scientist: Ohhhhhh yeah")
    uhp = uhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")

if uhp == 0:
    print_slow("Mad Scientist:Yessss, I have defeated your security system!")
    print_slow(
        "President of Hacktopia: Noooo, my master plan will never happend due to that useless hacker!!!"
    )
    time.sleep(3)
clear()
print(user)
print_slowln(":")
print_slow("Lets entangle some qubits!")
print_slow("Hacking...")
print_slow("President of Hacktopia: Entangle some qubits!")
print_slow("What do you make!?")
print_slow(
    "a:You can do entanglement with two qubits by applying 2 Hadamard gates followed by a CNOT gate."
)
print_slow(
    "b:You can do entanglement with two qubits by applying 2 CNOT gates followed by a hadamard gate"
)
print_slow("c:Cry as loud as you can.")
print_slow("d:IDK, and I don't want to know at all!!!")
bb=input("")
if bb == "a":
    print_slow(
        "Mad Scientist: Stop this do you have nothing better to do with your life!!!"
    )
    bhp = bhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")
else:
    print_slow("Mad Scientist: Take that!")
    uhp = uhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")

if uhp == 0:
    print_slow("Mad Scientist:Yessss, I have defeated your security system!")
    print_slow(
        "President of Hacktopia: Noooo, my master plan will never happend due to that useless hacker!!!"
    )
    time.sleep(3)
clear()

print(user)
print_slowln(":")
print_slow("Lets get some probabilities!")
print_slow("Hacking...")
print_slow(
    "President of Hacktopia: How many qubits do you need for 32768 probabilities?"
)
print_slow("a:31")
print_slow("b:10?")
print_slow("c:15")
print_slow("d:Why do I need to know?!?!?!?")
ba=input
if ba == "c":
    print_slow(
        "Mad Scientist: Get out of my face and stop you deranged lunatic!!!")
    bhp = bhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")
else:
    print_slow("Mad Scientist: Take that!")
    uhp = uhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")

if uhp == 0:
    print_slow("Mad Scientist:Yessss, I have defeated your security system!")
    print_slow(
        "President of Hacktopia: Noooo, my master plan will never happend due to that useless hacker!!!"
    )
time.sleep(3)
clear()
quit()

if bhp == 0:
    print_slow(
        "Mad Scientist: Noooo, you deranged hacker helped him get the computer which can help him destroy the world."
    )
    print_slow(
        "President of Hacktopia:Yes, now I can rule the world, muhahhahahhahahahhahahahhaha."
    )
    animate(">", 1000)
    time.sleep(3)
clear()
quit()

print(user)
print_slowln(":")
print_slow("Lets get some probabilities!")
print_slow("Hacking...")
print_slow(
    "President of Hacktopia: How many probabilities can 31 qubits calculate?")
print_slow("a:31")
print_slow("b:8913")
print_slow("c:2147483648")
print_slow("d:Why do I need to know?!?!?!?")
bz=input("")
if bz == "c":
    print_slow(
        "Mad Scientist: Get out of my face and stop you deranged lunatic!!!")
    bhp = bhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")
else:
    print_slow("Mad Scientist: Take that!")
    uhp = uhp - 1000
    print_slowln("Boss:")
    print(bhp)
    print_slow("hp")
    print_slowln(user)
    print_slowln(":")
    print(bhp)
    print_slow("hp")

if uhp == 0:
    print_slow("Mad Scientist:Yessss, I have defeated your security system!")
    print_slow(
        "President of Hacktopia: Noooo, my master plan will never happened due to that useless hacker!!!"
    )
    time.sleep(3)
clear()

if bhp == 0:
    print_slow(
        "Mad Scientist: Noooo, you deranged hacker helped him get the computer which can help him destroy the world."
    )
    print_slow(
        "President of Hacktopia:Yes, now I can rule the world, muhahhahahhahahahhahahahhaha."
    )
    animate(">", 1000)
    time.sleep(3)
clear()