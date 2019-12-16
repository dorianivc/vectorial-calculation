import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    raquetaX=int(req.params.get('raquetaX'))
    raquetaY=int(req.params.get('raquetaY'))
    raquetaH=int(req.params.get('raquetaH'))
    raquetaW=int(req.params.get('raquetaW'))
    puntoX=int(req.params.get('puntoX'))
    puntoY=int(req.params.get('puntoY'))
    radio=int(req.params.get('radio'))
    Pass=True
    if ((not raquetaX) or (not raquetaY) or (not raquetaH) or  (not raquetaW) or  (not puntoX) or (not puntoY) ):
        Pass=False
    if Pass:
        X=puntoX-max(raquetaX,min(puntoX,raquetaX+raquetaW))
        Y=puntoY-max(raquetaY,min(puntoY,raquetaY+raquetaH))
        if(X*X+Y*Y)<(radio*radio):
            return func.HttpResponse(f"{1}")
        else:
            return func.HttpResponse(f"{0}")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
