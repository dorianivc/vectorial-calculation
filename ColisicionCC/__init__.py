import logging
import math
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    ax=int(req.params.get('ax'))
    bx=int(req.params.get('bx'))
    ay=int(req.params.get('ay'))
    by=int(req.params.get('by'))
    r1=int(req.params.get('r1'))
    r2=int(req.params.get('r2'))
    Pass=True
    if  ((not ax) or (not bx) or (not ay) or  (not by) or  (not r1) or (not r2) ):
        Pass=False
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ax=req_body.get('ax')
            bx=req_body.get('bx')
            ay=req_body.get('ay')
            by=req_body.get('by')
            r1=req_body.get('r1')
            r2=req_body.get('r2')
    if Pass:
        distancia=math.sqrt((ax-bx)*(ax-bx) + (ay-by)*(ay-by))
        if((distancia+2*r1) >= (r1 + r2)):
            return func.HttpResponse(f"{1}")
        else:
            return func.HttpResponse(f"{0}")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
