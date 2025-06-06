from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(AKnight)),
    Or(AKnave, AKnight),
    Biconditional(AKnight,And(AKnight,AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),
    Or(BKnave,BKnight),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),
    Or(BKnave,BKnight),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    #A
    Implication(AKnight,And(AKnight,BKnight)),
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnight,BKnight))),
    Implication(AKnave,Not(And(AKnave,BKnave))),
    #B
    Implication(BKnight,Not(And(AKnight,BKnight))),
    Implication(BKnight,Not(And(AKnave,BKnave))),
    Implication(BKnave,And(AKnight,BKnight)),
    Implication(BKnave,And(AKnave,BKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Or(BKnave,BKnight),
    Or(CKnave, CKnight),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(AKnight)),
    Implication(BKnight,Not(BKnave)),
    Implication(BKnave,Not(BKnight)),
    Implication(CKnight,Not(CKnave)),
    Implication(CKnave,Not(CKnight)),

    #A
    Biconditional(Or(AKnight,AKnave),Or(AKnight,AKnave)),
    #B
    Biconditional(BKnight,Biconditional(AKnave,AKnight)),
    Biconditional(BKnight,CKnave),
    #C
    Biconditional(CKnight, AKnight)
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
