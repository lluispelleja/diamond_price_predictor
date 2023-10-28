
import pickle

def price_prediction(weight, cut, length, width, color, depth, clarity, table):
    
    cut_quality = {"Fair": 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}
    color_quality = {"D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
    clarity_quality = {"I1": 1, "SI2": 2, "SI1": 3, "VS2": 4, "VS1": 5, "VVS2": 6, "VVS1": 7, "IF": 8}
    
    n_cut = cut_quality[cut]
    n_color = color_quality[color]
    nclarity = clarity_quality[clarity]
    
    var1_d = depth / ((length + width) / 2)
    
    with open('../notebooks_and_model/RF_model.pkl', 'rb') as archivo:
        RF_model = pickle.load(archivo)
    
    X = [[weight, length, width, depth, n_cut, nclarity, n_color, var1_d, table]]
    
    prediction = RF_model.predict(X)
    pred = str(prediction)
    convert = pred[1:-1]
    flot = float(convert)
    conversion = "{:.2f}".format(flot)
    
    return conversion
        