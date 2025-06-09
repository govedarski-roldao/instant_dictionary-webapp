import pandas


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv("data.csv")
        filter_df = df.loc[df['word'] == self.term]
        v2 = filter_df["definition"]
        result = tuple(v2)
        print(result[0])
        return result


defe = Definition("sun").get()
print(defe)