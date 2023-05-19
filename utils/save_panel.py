import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NumpyEncoder, self).default(obj)

def save_panel(fig, name_panel):
    with open(f"figures/{name_panel}.json", "w") as file:
        json.dump(fig.to_dict(), file, cls=NumpyEncoder)