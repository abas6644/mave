class Human_rights:
    def __init__(self,contents,laws):
        self.contents=contents
        self.laws=laws

# History of human rights
    def history(self):
        print("The principle of sovereignty which has long become a custom in international law was traditionally given a wide interpretation to accomodate all aspects of a state's treatment of it's citizens as a matter within it's domestic jurisdiction")

    def humanitarian_intervention(self):
        print("Notwithstanding the classical disposition of the concept of sovereignty,it was a recognised exception that foreigners were entitled to minimum standard of treatment, a breach of which inculcated international responsibility. Intervention in this sense means dictational intervention amounting to a denial of the independence of a state.")

    def restrictions_on_use_of_force(self):
        print("As international community became organised,restrictive controls were developed for the use of force in international law. A good example was the second hague convention 1907 which prohibited the use of force for debt collection except the debtor refuses to submit to arbitration. The third hague convention required that war must be specifically and formally declared and must be preceded by ultimatum.")

sections=Human_rights("customs","international")
sections.restrictions_on_use_of_force()







