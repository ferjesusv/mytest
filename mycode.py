
import pandas as pd
import matplotlib

a = pd.DataFrame({"colA":[1,2,3,4],
                    "colB":[.2,.3,.4,.6] },
                    index = ['Ene', 'Feb', 'Mar', 'Abr']
                )
b = pd.DataFrame({"colA":[5,6,7,8],
                    "colC":[.5,.6,.7,.8]
                    },
                    index = ['Feb', 'Mar', 'Abr', 'May']
                )

#b = pd.read_excel("miExcel.xls")

print(a['colA'] / b['colA'])
