from dataclasses import dataclass
@dataclass
class Chromosome:
    chromosome:int
    def __hash__(self):
        return hash(self.chromosome)