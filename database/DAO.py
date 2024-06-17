from database.DB_connect import DBConnect
from model.chromosome import Chromosome


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getChromosomes():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct g.Chromosome
from genes_small.genes g
where g.Chromosome !=0
                    """
        cursor.execute(query)
        for row in cursor:
            result.append(Chromosome(row["Chromosome"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi():
            conn = DBConnect.get_connection()
            result = []
            cursor = conn.cursor(dictionary=True)
            query = """select g.Chromosome as c1, g2.Chromosome as c2, sum(distinct(i.Expression_Corr)) as peso
from interactions i 
join genes g on g.GeneID = i.GeneID1 
join genes g2 on g2.GeneID = i.GeneID2 
where g2.Chromosome !=0 and g.Chromosome!=0 and g2.Chromosome != g.Chromosome
group by g.Chromosome, g2.Chromosome 
                        """
            cursor.execute(query)
            for row in cursor:
                result.append((row["c1"], row["c2"], row["peso"]))
            cursor.close()
            conn.close()
            return result
