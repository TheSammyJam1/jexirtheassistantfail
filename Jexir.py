from random import *
import webbrowser
print('Hello, I am Jexir your Assistant')


def jexir():
    def anny():
        anelse = input('anything else?\nY/N\n')
        if anelse == 'Y' or 'y':
            jexir()
        if anelse == 'N' or 'n':
            qit = input('Quit?\n(Y/N)\n')
            if qit == 'Y' or 'y':
                quit()
            if qit == 'N' or 'n':
                jexir()

    print('\nHow may I help you?\nType which number collates with your Reply')

    def jexirqa():
        jexirq = input(' - cant help me(1)\n - quit(2)\n - get me water(3)\n - tell me a joke(4)\n - math(5)\n - more(0)\n-')
        # 1 Cant Help You
        if jexirq == '1':
            print('Sorry')
            jexir()
        # 2 quit
        if jexirq == '2':
            print('Quited')
            quit()
        # 3 get me water
        if jexirq == '3':
            print('No Can Do\nCant get you water\nSorry')
            anny()
        # 4 tell me a joke
        if jexirq == '4':
            def joke():
                num = randint(0, 15)
                if num == 0:
                    print('What do dentists call their x-rays?\nTooth pics!')
                if num == 1:
                    print('There’s a fine line between a numerator and a denominator.')
                if num == 2:
                    print('Did you hear about the first restaurant to open on the moon?')
                    print('It had great food, but no atmosphere.')
                if num == 3:
                    print('What did one ocean say to the other ocean?\nNothing, it just waved.')
                if num == 4:
                    print('Do you want to hear a construction joke?\nSorry, I’m still working on it.')
                if num == 5:
                    print('Did you hear about the fire at the circus?\nIt was in tents!')
                if num == 6:
                    print('Why do ducks have feathers?\nTo cover their butt quacks!')
                if num == 7:
                    print('Why should you never trust stairs?\nThey’re always up to something.')
                if num == 8:
                    print('When does a joke become a ‘dad’ joke?\nWhen it becomes apparent.')
                if num == 9:
                    print('I entered ten puns in a contest to see which would win.\nNo pun in ten did.')
                if num == 10:
                    print('Why is Peter Pan always flying?\nBecause he Neverlands.')
                    print('(I love this joke because it never grows old.)')
                if num == 11:
                    print('Two windmills are standing on a wind farm.\nOne asks, ‘What’s your favorite kind of music?’')
                    print('The other replies, ‘I’m a big metal fan.’')
                if num == 12:
                    print('I took the shell off of my racing snail, thinking it would make him faster.')
                    print('But if anything, it made him more sluggish.')
                if num == 13:
                    print('You know, it was so cold in D.C. the other day, I saw a politician with his hands in his own pockets.')
                if num == 14:
                    print('How many tickles does it take to get an octopus to laugh?\nTen tickles')
                if num == 15:
                    print('My teachers told me I’d never amount to much since I procrastinate so much.\nI told them, “Just you wait!”')
                nex = input('\nanother?\ny/n\n')
                if nex == 'y':
                    joke()

            joke()
            anny()
        # 5 math
        if jexirq == '5':
            mathi = int(input('What math?\nAdd(1)\nSubtract(2)\nMultiply(3)\nDivide(4)\nPoop(5)\n'))
            if mathi == 1:
                print('Addition')
                n1 = int(input('first number?'))
                n2 = int(input('second number'))
                print(n1+n2)
            if mathi == 2:
                print('Subtraction')
                n1 = int(input('first number?'))
                n2 = int(input('second number'))
                print(n1-n2)
            if mathi == 3:
                print('Multiplication')
                n1 = int(input('first number?'))
                n2 = int(input('second number'))
                print(n1*n2)
            if mathi == 4:
                print('Division')
                n1 = int(input('first number?'))
                n2 = int(input('second number'))
                print(n1/n2)
            if mathi == 5:
                input('What Were you thinking that would do?')
            anny()
        if jexirq == '0':
            jexirq = 'a'+input('Back(0)\nOpen Website(1)\nLeave Feedback(2)\nDo My laundry!(3)')
            # Back
            if jexirq == 'a0':
                jexirqa()
            # Website
            if jexirq == 'a1':
                web = input('Which Website\nNetflix(1)\nSearch Engine(2)\nGitHub(3)\nWiki(4)\nCustom(0)\n')
                if web == '1':
                    webbrowser.open('http://netflix.com', new=2)
                if web == '2':
                    webbrowser.open('https://duckduckgo.com/', new=2)
                if web == '3':
                    webbrowser.open('https://github.com/TheSammyJam1/jexirtheassistant', new=2)
                if web == '0':
                    cus = 'https://' + input('Web Address\nex:duckduckgo.com\n')
                    webbrowser.open(cus, new=2)
            # Leave Feedback
            if jexirq == 'a2':
                webbrowser.open('https://github.com/TheSammyJam1/jexirtheassistant/issues')
                print('Thank You for Leaving Feedback!')
            # Do
            if jexirq == 'a3':
                yn = input('Do You Think I am Your Servant?!?!\nY/N')
                if yn == 'y' or 'Y':
                    print('Why\nI am incapable')
                if yn == 'n' or 'N':
                    print('Good.\nThen why did you choose 3')
    jexirqa()


jexir()
