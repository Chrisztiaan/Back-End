from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":

    # Functions here

    # 1

    def unique_koala_facts(number):
        i = 1
        unique_facts = []
        while i <= number:
            # print(i)
            random_fact = random_koala_fact()
            i += 1
            if random_fact not in unique_facts:
                unique_facts.append(random_fact)
            if i == number:
                break
        print(unique_facts)
        print(len(unique_facts))

    unique_koala_facts(5)

    # 2
    particular_fact = random_koala_fact()
    list_of_facts = []
    joey_facts = []

    def num_joey_facts():
        while list_of_facts.count(particular_fact) < 11:
            fact = random_koala_fact()
            if "joey" in fact:
                if fact not in joey_facts:
                    joey_facts.append(fact)
                list_of_facts.append(fact)
            else:
                list_of_facts.append(fact)
        return len(joey_facts)

    print(num_joey_facts())

    # 3
    def koala_weight():
        a = 1000
        b = 1
        while b < 1000:
            random = random_koala_fact()
            if "kg" in random:
                weight = int(random[-5:-3])
                return weight
            else: 
                b += 1

    print(koala_weight())
