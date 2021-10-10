from random import random, choice
import sys


class Ecosystem:
    def __init__(self, length, num_of_fish, num_of_bear):
        self.river = ['N/A'] * length
        self.num_of_fish = num_of_fish
        self.num_of_bear = num_of_bear
        cnt = 0
        while cnt < num_of_bear + num_of_fish:
            pos = choice(range(length))
            if self.river[pos] == 'N/A':
                self.river[pos] = 'Bear' if cnt < num_of_bear else 'Fish'
                cnt += 1

    def simulation(self, steps):
        def generate(anm, lst):
            avail = [ps for ps in range(len(lst)) if lst[ps] == 'N/A']
            if avail:
                lst[choice(avail)] = anm
            else:
                print(f'There is no room to generate a new {anm}!')
                self.result()
                sys.exit()
            return lst

        for i in range(steps):
            a = 0
            new_anim = []
            while a < len(self.river):
                if self.river[a] != 'N/A':
                    new_pos = [a-1, a, a+1]
                    if a == 0:
                        tmp = choice(new_pos[1:])
                    elif a == len(self.river) - 1:
                        tmp = choice(new_pos[:2])
                    else:
                        tmp = choice(new_pos)
                    if tmp != a:
                        if self.river[tmp] == 'N/A':
                            self.river[tmp], self.river[a]\
                                = self.river[a], self.river[tmp]
                            a += 1
                        elif self.river[tmp] == self.river[a]:
                            new_anim.append(self.river[a])
                        else:
                            self.river[tmp] = self.river[a] = 'N/A'
                            self.river[tmp] = 'Bear'
                rs = set(self.river)
                if len(rs) == 1 or (len(rs) == 2 and 'N/A' in rs):
                    print('There is only one kind of animal in the river!')
                    self.result()
                    sys.exit(0)
                a += 1
            for new in new_anim:
                generate(new, self.river)
        self.result()

    def result(self):
        print('-'.join(self.river))


def main():
    promp = 'Input length of river, #Fish, #Bear and #simulation:'
    while True:
        try:
            l, f, b, s = list(map(int, input(promp).split()))[:]
            if f + b > l:
                raise TypeError
        except ValueError:
            print('Check your input!')
        except TypeError:
            print('Animal number exceeds length of river!')
        else:
            break
    Ecosystem(l, f, b).simulation(s)


if __name__ == '__main__':
    main()
